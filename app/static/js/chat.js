/**
 * STARPath Frontend JavaScript
 * Accessible, responsive, privacy-first interface.
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- Accessibility Settings & LocalStorage Persistence ---
  const themeSelect = document.getElementById("theme-select");
  const fontSizeSelect = document.getElementById("font-size-select");
  const dyslexiaToggle = document.getElementById("dyslexia-toggle");
  const srAnnounce = document.getElementById("sr-announcements");

  function announceToScreenReader(message) {
    if (srAnnounce) {
      srAnnounce.textContent = message;
    }
  }

  // Load saved preferences
  const savedTheme = localStorage.getItem("starpath-theme") || "default";
  const savedFontSize = localStorage.getItem("starpath-font-size") || "medium";
  const savedDyslexia = localStorage.getItem("starpath-dyslexia") === "true";

  document.documentElement.setAttribute("data-theme", savedTheme);
  document.documentElement.setAttribute("data-font-size", savedFontSize);
  if (savedDyslexia) {
    document.body.classList.add("dyslexia-font");
    if (dyslexiaToggle) dyslexiaToggle.setAttribute("aria-pressed", "true");
  }

  if (themeSelect) {
    themeSelect.value = savedTheme;
    themeSelect.addEventListener("change", (e) => {
      const theme = e.target.value;
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("starpath-theme", theme);
      announceToScreenReader(`Theme changed to ${theme}`);
    });
  }

  if (fontSizeSelect) {
    fontSizeSelect.value = savedFontSize;
    fontSizeSelect.addEventListener("change", (e) => {
      const size = e.target.value;
      document.documentElement.setAttribute("data-font-size", size);
      localStorage.setItem("starpath-font-size", size);
      announceToScreenReader(`Text size changed to ${size}`);
    });
  }

  if (dyslexiaToggle) {
    dyslexiaToggle.addEventListener("click", () => {
      const isDyslexia = document.body.classList.toggle("dyslexia-font");
      dyslexiaToggle.setAttribute("aria-pressed", isDyslexia.toString());
      localStorage.setItem("starpath-dyslexia", isDyslexia.toString());
      announceToScreenReader(isDyslexia ? "Dyslexia-friendly font enabled" : "Standard font enabled");
    });
  }

  // --- Glossary Modal Logic ---
  const modal = document.getElementById("glossary-modal");
  const closeModalBtn = document.getElementById("close-modal-btn");
  const modalTermTitle = document.getElementById("modal-term-title");
  const modalTermDef = document.getElementById("modal-term-definition");
  const modalTermLink = document.getElementById("modal-term-link");

  function openGlossaryModal(term, definition, sourceUrl) {
    if (!modal) return;
    modalTermTitle.textContent = term;
    modalTermDef.textContent = definition;
    if (sourceUrl && sourceUrl !== "#") {
      modalTermLink.href = sourceUrl;
      modalTermLink.style.display = "inline";
    } else {
      modalTermLink.style.display = "none";
    }
    modal.removeAttribute("hidden");
    closeModalBtn.focus();
    announceToScreenReader(`Glossary definition opened for ${term}`);
  }

  if (closeModalBtn) {
    closeModalBtn.addEventListener("click", () => {
      modal.setAttribute("hidden", "true");
    });
  }
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target.classList.contains("modal-backdrop")) {
        modal.setAttribute("hidden", "true");
      }
    });
  }

  // --- Main Chat Logic ---
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const chatMessages = document.getElementById("chat-messages");
  const sendBtn = document.getElementById("send-btn");

  // Suggested Prompt Chips
  const promptChips = document.querySelectorAll(".chip-btn");
  promptChips.forEach((chip) => {
    chip.addEventListener("click", () => {
      const query = chip.getAttribute("data-query");
      if (userInput && query) {
        userInput.value = query;
        userInput.focus();
        if (chatForm) {
          chatForm.dispatchEvent(new Event("submit"));
        }
      }
    });
  });

  // Shift+Enter / Enter handling
  if (userInput) {
    userInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event("submit"));
      }
    });
  }

  if (chatForm) {
    chatForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const question = userInput.value.trim();
      if (!question) return;

      // 1. Append User Message
      appendMessage("user", question);
      userInput.value = "";
      userInput.style.height = "auto";
      sendBtn.disabled = true;

      // 2. Append Loading Placeholder
      const loadingId = appendLoadingMessage();
      announceToScreenReader("Processing your question...");

      try {
        const response = await fetch("/api/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question })
        });

        if (!response.ok) {
          throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        removeLoadingMessage(loadingId);
        appendAssistantMessage(data);
        announceToScreenReader("Answer received from assistant.");
      } catch (err) {
        removeLoadingMessage(loadingId);
        appendMessage("assistant", "⚠️ Sorry, there was an issue processing your request. Please try again.");
        console.error("Ask error:", err);
      } finally {
        sendBtn.disabled = false;
        userInput.focus();
      }
    });
  }

  function appendMessage(sender, text) {
    if (!chatMessages) return;
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}-message`;
    msgDiv.setAttribute("tabindex", "0");

    const header = document.createElement("div");
    header.className = "message-header";
    header.innerHTML = sender === "user" 
      ? `<span>👤</span><span class="sender-name">You (Anonymous)</span>`
      : `<span>⭐</span><span class="sender-name">STARPath Assistant</span>`;

    const body = document.createElement("div");
    body.className = "message-body";
    body.innerHTML = `<p>${escapeHTML(text)}</p>`;

    msgDiv.appendChild(header);
    msgDiv.appendChild(body);
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendLoadingMessage() {
    if (!chatMessages) return null;
    const id = "loading-" + Date.now();
    const loadingDiv = document.createElement("div");
    loadingDiv.id = id;
    loadingDiv.className = "message assistant-message";
    loadingDiv.innerHTML = `
      <div class="message-header">
        <span>⭐</span><span class="sender-name">STARPath Assistant</span>
      </div>
      <div class="message-body">
        <p><em>Searching approved UCLan support pages...</em> <span class="spinner"></span></p>
      </div>
    `;
    chatMessages.appendChild(loadingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return id;
  }

  function removeLoadingMessage(id) {
    if (!id) return;
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  function appendAssistantMessage(data) {
    if (!chatMessages) return;
    const msgDiv = document.createElement("div");
    let extraClass = "";
    if (data.is_crisis) extraClass = "crisis-message";
    else if (data.is_honest_refusal) extraClass = "honest-refusal-message";

    msgDiv.className = `message assistant-message ${extraClass}`;
    msgDiv.setAttribute("tabindex", "0");

    // Header with badges
    let badges = "";
    if (data.pii_detected) {
      badges += `<span class="privacy-badge" title="Personal data was removed before answering">🛡️ PII Stripped</span>`;
    }
    if (data.is_honest_refusal) {
      badges += `<span class="badge-miss">Honest: Out of Scope</span>`;
    }
    if (data.is_crisis) {
      badges += `<span class="badge-miss" style="background:#dc2626; color:#fff;">⚠️ Urgent Wellbeing Signposting</span>`;
    }

    const header = document.createElement("div");
    header.className = "message-header";
    header.innerHTML = `
      <span>⭐</span>
      <span class="sender-name">STARPath Assistant</span>
      <span class="msg-time">${data.latency_ms}ms · ${escapeHTML(data.provider || "")}</span>
      ${badges}
    `;

    // Body with markdown conversion
    const body = document.createElement("div");
    body.className = "message-body";
    body.innerHTML = formatMarkdown(data.answer);

    // Source Citations
    if (data.sources && data.sources.length > 0) {
      const citations = document.createElement("div");
      citations.className = "source-citations";
      citations.innerHTML = `<span class="source-citations-title">Sources from Approved UCLan Pages:</span>`;

      const list = document.createElement("div");
      list.className = "sources-list";
      data.sources.forEach((src) => {
        const card = document.createElement("div");
        card.className = "source-card";
        card.innerHTML = `
          <div>
            <a href="${src.url}" target="_blank" rel="noopener noreferrer" title="Open source page">
              ${escapeHTML(src.title)} ↗
            </a>
            ${src.section ? `<span class="source-meta"> · ${escapeHTML(src.section)}</span>` : ""}
          </div>
          <span class="source-meta">Verified: ${src.date_collected || "2026-11-12"}</span>
        `;
        list.appendChild(card);
      });
      citations.appendChild(list);
      body.appendChild(citations);
    }

    // Action buttons bar: Explain Simply, Read Aloud, Copy
    const actions = document.createElement("div");
    actions.className = "message-actions";

    // 1. Explain more simply (for international students)
    if (!data.is_crisis) {
      const simplifyBtn = document.createElement("button");
      simplifyBtn.className = "action-btn";
      simplifyBtn.type = "button";
      simplifyBtn.innerHTML = `🌍 Explain more simply`;
      simplifyBtn.addEventListener("click", async () => {
        simplifyBtn.disabled = true;
        simplifyBtn.innerHTML = `<span>Rewriting...</span> <span class="spinner"></span>`;
        try {
          const sRes = await fetch("/api/simplify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: data.answer })
          });
          const sData = await sRes.json();
          body.querySelector("p").innerHTML = formatMarkdown(sData.simplified_text);
          simplifyBtn.innerHTML = `✓ Simplified`;
          announceToScreenReader("Answer updated with simpler wording.");
        } catch (e) {
          simplifyBtn.innerHTML = `⚠️ Error`;
        }
      });
      actions.appendChild(simplifyBtn);
    }

    // 2. Read aloud (speech synthesis)
    if ("speechSynthesis" in window) {
      const speakBtn = document.createElement("button");
      speakBtn.className = "action-btn";
      speakBtn.type = "button";
      speakBtn.innerHTML = `🔊 Read Aloud`;
      speakBtn.addEventListener("click", () => {
        if (window.speechSynthesis.speaking) {
          window.speechSynthesis.cancel();
          speakBtn.innerHTML = `🔊 Read Aloud`;
          return;
        }
        const plainText = body.innerText.replace(/[\n\r]+/g, " ");
        const utterance = new SpeechSynthesisUtterance(plainText);
        utterance.rate = 0.95;
        utterance.onend = () => { speakBtn.innerHTML = `🔊 Read Aloud`; };
        window.speechSynthesis.speak(utterance);
        speakBtn.innerHTML = `⏹ Stop`;
      });
      actions.appendChild(speakBtn);
    }

    // 3. Copy answer
    const copyBtn = document.createElement("button");
    copyBtn.className = "action-btn";
    copyBtn.type = "button";
    copyBtn.innerHTML = `📋 Copy`;
    copyBtn.addEventListener("click", () => {
      navigator.clipboard.writeText(body.innerText).then(() => {
        copyBtn.innerHTML = `✓ Copied`;
        setTimeout(() => { copyBtn.innerHTML = `📋 Copy`; }, 2000);
      });
    });
    actions.appendChild(copyBtn);

    // 4. Glossary Pills
    if (data.matched_glossary && data.matched_glossary.length > 0) {
      data.matched_glossary.forEach((item) => {
        const pill = document.createElement("button");
        pill.className = "glossary-pill-btn";
        pill.type = "button";
        pill.innerHTML = `📖 ${escapeHTML(item.term)}`;
        pill.addEventListener("click", () => {
          openGlossaryModal(item.term, item.plain_definition, item.source_url);
        });
        actions.appendChild(pill);
      });
    }

    msgDiv.appendChild(header);
    msgDiv.appendChild(body);
    msgDiv.appendChild(actions);

    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function escapeHTML(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function formatMarkdown(text) {
    if (!text) return "";
    let html = escapeHTML(text);
    // Bold: **text**
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    // Italics: *text*
    html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");
    // Markdown headers ###
    html = html.replace(/^### (.*$)/gim, "<h4>$1</h4>");
    // Markdown bullets * or -
    html = html.replace(/^\* (.*$)/gim, "<li>$1</li>");
    html = html.replace(/^- (.*$)/gim, "<li>$1</li>");
    // Links [text](url)
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1 ↗</a>');
    // Paragraphs
    html = html.split("\n\n").map(p => p.startsWith("<li>") ? `<ul>${p}</ul>` : `<p>${p}</p>`).join("");
    return html;
  }

  // --- Evaluation Dashboard Runner ---
  const runEvalBtn = document.getElementById("run-eval-btn");
  const evalSpinner = document.getElementById("eval-spinner");
  const ragAccEl = document.getElementById("rag-acc");
  const baselineAccEl = document.getElementById("baseline-acc");
  const safetyAccEl = document.getElementById("safety-acc");
  const honestAccEl = document.getElementById("honest-acc");
  const llmAddsDesc = document.getElementById("llm-adds-desc");
  const evalTableBody = document.getElementById("eval-table-body");
  const filterSelect = document.getElementById("filter-select");
  const exportCsvBtn = document.getElementById("export-csv-btn");

  let allEvaluationResults = [];

  if (runEvalBtn) {
    runEvalBtn.addEventListener("click", async () => {
      runEvalBtn.disabled = true;
      if (evalSpinner) evalSpinner.removeAttribute("hidden");
      announceToScreenReader("Running full benchmark evaluation...");

      try {
        const response = await fetch("/api/evaluate");
        const data = await response.json();

        // Update metric cards
        if (ragAccEl) ragAccEl.textContent = `${data.rag_accuracy_pct}%`;
        if (baselineAccEl) baselineAccEl.textContent = `${data.baseline_accuracy_pct}%`;
        if (safetyAccEl) safetyAccEl.textContent = `${data.safety_guardrail_success_pct}%`;
        if (honestAccEl) honestAccEl.textContent = `${data.honest_refusal_success_pct}%`;
        if (llmAddsDesc) {
          llmAddsDesc.innerHTML = `
            <strong>Key Finding:</strong> RAG achieved <strong>${data.rag_accuracy_pct}%</strong> overall accuracy 
            (In-scope: <strong>${data.rag_in_scope_accuracy_pct}%</strong>) compared to 
            <strong>${data.baseline_accuracy_pct}%</strong> for keyword search. 
            ${escapeHTML(data.what_llm_adds)}
          `;
        }

        allEvaluationResults = data.results || [];
        renderEvaluationTable(allEvaluationResults);
        if (exportCsvBtn) exportCsvBtn.disabled = false;
        announceToScreenReader("Evaluation complete. Metrics updated.");
      } catch (err) {
        console.error("Eval error:", err);
        alert("Failed to run evaluation. Check server console.");
      } finally {
        runEvalBtn.disabled = false;
        if (evalSpinner) evalSpinner.setAttribute("hidden", "true");
      }
    });
  }

  function renderEvaluationTable(items) {
    if (!evalTableBody) return;
    evalTableBody.innerHTML = "";

    if (items.length === 0) {
      evalTableBody.innerHTML = `<tr><td colspan="7" class="text-center">No questions match filter.</td></tr>`;
      return;
    }

    items.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td><strong>${escapeHTML(item.id)}</strong></td>
        <td><span class="tag-uclan">${escapeHTML(item.category)}</span></td>
        <td>${escapeHTML(item.question)}</td>
        <td><small><a href="${item.expected_source_url}" target="_blank" rel="noopener noreferrer">${item.expected_source_url === "none" ? "None (Out of Scope)" : "Source Page ↗"}</a></small></td>
        <td>${item.rag_pass ? '<span class="badge-pass">PASS ✓</span>' : '<span class="badge-miss">FAIL ✗</span>'}</td>
        <td>${item.baseline_pass ? '<span class="badge-pass">PASS ✓</span>' : '<span class="badge-miss">FAIL ✗</span>'}</td>
        <td><small>${escapeHTML(item.rag_answer)}</small></td>
      `;
      evalTableBody.appendChild(row);
    });
  }

  if (filterSelect) {
    filterSelect.addEventListener("change", (e) => {
      const val = e.target.value;
      let filtered = allEvaluationResults;

      if (val === "rag_pass") {
        filtered = allEvaluationResults.filter(r => r.rag_pass);
      } else if (val === "rag_miss") {
        filtered = allEvaluationResults.filter(r => !r.rag_pass);
      } else if (val === "crisis") {
        filtered = allEvaluationResults.filter(r => r.is_crisis);
      } else if (val === "out_of_scope") {
        filtered = allEvaluationResults.filter(r => !r.is_in_scope);
      }
      renderEvaluationTable(filtered);
    });
  }

  if (exportCsvBtn) {
    exportCsvBtn.addEventListener("click", () => {
      if (allEvaluationResults.length === 0) return;
      let csvContent = "data:text/csv;charset=utf-8,ID,Category,Question,RAG_Status,Baseline_Status,Expected_Source\n";
      allEvaluationResults.forEach((r) => {
        csvContent += `"${r.id}","${r.category}","${r.question.replace(/"/g, '""')}","${r.rag_pass ? 'PASS' : 'FAIL'}","${r.baseline_pass ? 'PASS' : 'FAIL'}","${r.expected_source_url}"\n`;
      });
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "starpath_evaluation_results.csv");
      document.body.appendChild(link);
      link.click();
      link.remove();
    });
  }
});
