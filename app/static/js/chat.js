/**
 * STARPath Frontend JavaScript — Accessible, Human-Centred Edition
 * CO2007 Agile Team Project · BSc (Hons) AI & Data Science
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- Accessibility Settings & LocalStorage Persistence ---
  const themeSelect = document.getElementById("theme-select");
  const fontSizeSelect = document.getElementById("font-size-select");
  const dyslexiaToggle = document.getElementById("dyslexia-toggle");
  const soundToggle = document.getElementById("sound-toggle");
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
  let soundEnabled = localStorage.getItem("starpath-sound") === "true";

  document.documentElement.setAttribute("data-theme", savedTheme);
  document.documentElement.setAttribute("data-font-size", savedFontSize);
  if (savedDyslexia) {
    document.body.classList.add("dyslexia-font");
    if (dyslexiaToggle) dyslexiaToggle.setAttribute("aria-pressed", "true");
  }

  if (soundToggle) {
    soundToggle.setAttribute("aria-pressed", soundEnabled.toString());
    soundToggle.innerHTML = soundEnabled ? `<span>🔔</span> Sound On` : `<span>🔕</span> Sound Off`;
    soundToggle.addEventListener("click", () => {
      soundEnabled = !soundEnabled;
      localStorage.setItem("starpath-sound", soundEnabled.toString());
      soundToggle.setAttribute("aria-pressed", soundEnabled.toString());
      soundToggle.innerHTML = soundEnabled ? `<span>🔔</span> Sound On` : `<span>🔕</span> Sound Off`;
      announceToScreenReader(soundEnabled ? "Audio chime enabled" : "Audio chime muted");
      if (soundEnabled) playChimeTone(587.33, 0.1); // D5 test beep
    });
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

  // Soft Web Audio Chime Generator
  function playChimeTone(frequency = 523.25, duration = 0.15) {
    if (!soundEnabled) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(frequency, ctx.currentTime);
      gain.gain.setValueAtTime(0.08, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {
      console.warn("Audio chime unavailable:", e);
    }
  }

  function playSuccessChime() {
    if (!soundEnabled) return;
    playChimeTone(523.25, 0.1); // C5
    setTimeout(() => playChimeTone(659.25, 0.15), 100); // E5
  }

  // Format humanized time
  function getFormattedTime() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
  }

  // Update welcome time if present
  const welcomeTimeEl = document.getElementById("welcome-time");
  if (welcomeTimeEl) {
    welcomeTimeEl.textContent = getFormattedTime();
  }

  // --- Interactive Packing Checklist Logic ---
  const packingChecklist = document.getElementById("packing-checklist");
  const checklistCounter = document.getElementById("checklist-counter");

  if (packingChecklist && checklistCounter) {
    let savedChecklist = {};
    try {
      savedChecklist = JSON.parse(localStorage.getItem("starpath-packing-checklist") || "{}");
    } catch (e) {
      savedChecklist = {};
    }

    const checkInputs = packingChecklist.querySelectorAll(".check-input");
    
    function updateCounter() {
      let checkedCount = 0;
      checkInputs.forEach((input) => {
        const key = input.getAttribute("data-item");
        if (input.checked) {
          checkedCount++;
          input.closest(".check-item").classList.add("completed");
        } else {
          input.closest(".check-item").classList.remove("completed");
        }
        savedChecklist[key] = input.checked;
      });
      checklistCounter.textContent = checkedCount === checkInputs.length
        ? `${checkedCount}/${checkInputs.length} packed! 🎉`
        : `${checkedCount}/${checkInputs.length} packed`;
      localStorage.setItem("starpath-packing-checklist", JSON.stringify(savedChecklist));
    }

    checkInputs.forEach((input) => {
      const key = input.getAttribute("data-item");
      if (savedChecklist[key] === true) {
        input.checked = true;
      }
      input.addEventListener("change", () => {
        updateCounter();
        if (input.checked) playChimeTone(880, 0.08); // A5 tick sound
      });
    });

    updateCounter();
  }

  // --- Sidebar Category Tabs Filter ---
  const promptTabs = document.querySelectorAll(".tab-chip");
  const chipButtons = document.querySelectorAll(".prompt-chips .chip-btn");

  if (promptTabs.length > 0 && chipButtons.length > 0) {
    promptTabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        promptTabs.forEach(t => {
          t.classList.remove("active");
          t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("active");
        tab.setAttribute("aria-selected", "true");

        const targetCategory = tab.getAttribute("data-tab");
        chipButtons.forEach((btn) => {
          const btnCat = btn.getAttribute("data-category");
          if (targetCategory === "all" || btnCat === targetCategory || btnCat === "all") {
            btn.style.display = "flex";
          } else {
            btn.style.display = "none";
          }
        });
      });
    });
  }

  // --- Glossary Modal Logic ---
  const modal = document.getElementById("glossary-modal");
  const closeModalBtn = document.getElementById("close-modal-btn");
  const modalOkBtn = document.getElementById("modal-ok-btn");
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

  function closeGlossaryModal() {
    if (modal) modal.setAttribute("hidden", "true");
  }

  if (closeModalBtn) closeModalBtn.addEventListener("click", closeGlossaryModal);
  if (modalOkBtn) modalOkBtn.addEventListener("click", closeGlossaryModal);
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target.classList.contains("modal-backdrop")) closeGlossaryModal();
    });
  }

  // --- Main Chat Logic ---
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const chatMessages = document.getElementById("chat-messages");
  const sendBtn = document.getElementById("send-btn");
  const clearChatBtn = document.getElementById("clear-chat-btn");

  // Clear Chat Button
  if (clearChatBtn && chatMessages) {
    clearChatBtn.addEventListener("click", () => {
      if (confirm("Reset conversation and start fresh?")) {
        const welcomeMsg = chatMessages.querySelector(".welcome-message");
        chatMessages.innerHTML = "";
        if (welcomeMsg) chatMessages.appendChild(welcomeMsg);
        announceToScreenReader("Chat cleared.");
      }
    });
  }

  // Wire prompt chips & starter chips
  function wireQueryTriggers() {
    const allQueryBtns = document.querySelectorAll(".chip-btn, .starter-chip");
    allQueryBtns.forEach((btn) => {
      btn.onclick = () => {
        const query = btn.getAttribute("data-query");
        if (userInput && query) {
          userInput.value = query;
          userInput.focus();
          if (chatForm) {
            chatForm.dispatchEvent(new Event("submit"));
          }
        }
      };
    });
  }
  wireQueryTriggers();

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

      // 2. Append Natural Typing Indicator
      const loadingId = appendTypingIndicator();
      announceToScreenReader("Searching approved UCLan support pages...");

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
        playSuccessChime();
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
      ? `<span>👤</span><span class="sender-name">You (Anonymous)</span><span class="msg-time">${getFormattedTime()}</span>`
      : `<span>⭐</span><span class="sender-name">STARPath Assistant</span><span class="msg-time">${getFormattedTime()}</span>`;

    const body = document.createElement("div");
    body.className = "message-body";
    body.innerHTML = `<p>${escapeHTML(text)}</p>`;

    msgDiv.appendChild(header);
    msgDiv.appendChild(body);
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendTypingIndicator() {
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
        <div class="typing-indicator-container">
          <div class="typing-dots" aria-hidden="true">
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
          </div>
          <span class="typing-label">Checking official UCLan pages...</span>
        </div>
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
      badges += `<span class="privacy-notice" style="padding:2px 8px; font-size:0.72rem; border-left-width:3px;" title="Personal details were redacted">🛡️ PII Redacted</span>`;
    }
    if (data.is_honest_refusal) {
      badges += `<span class="badge-miss">Honest: Out of Scope</span>`;
    }
    if (data.is_crisis) {
      badges += `<span class="badge-miss" style="background:#dc2626; color:#fff;">🚨 Immediate Wellbeing Signposting</span>`;
    }

    const header = document.createElement("div");
    header.className = "message-header";
    header.innerHTML = `
      <span>⭐</span>
      <span class="sender-name">STARPath Assistant</span>
      <span class="msg-badge">Snapshot 12 Nov 2026</span>
      ${badges}
      <span class="msg-time">${getFormattedTime()}</span>
    `;

    // Body with markdown conversion
    const body = document.createElement("div");
    body.className = "message-body";
    body.innerHTML = formatMarkdown(data.answer);

    // Source Citations Card
    if (data.sources && data.sources.length > 0) {
      const citations = document.createElement("div");
      citations.className = "source-citations";
      citations.innerHTML = `<span class="source-citations-title"><span>🛡️</span> Verified Official UCLan Sources:</span>`;

      const list = document.createElement("div");
      list.className = "sources-list";
      data.sources.forEach((src) => {
        const card = document.createElement("div");
        card.className = "source-card";
        card.innerHTML = `
          <div>
            <a href="${src.url}" target="_blank" rel="noopener noreferrer" title="Open verified official UCLan page">
              ${escapeHTML(src.title)} ↗
            </a>
            ${src.section ? `<span class="source-meta"> · ${escapeHTML(src.section)}</span>` : ""}
          </div>
          <span class="source-meta">Checked: ${src.date_collected || "2026-11-12"}</span>
        `;
        list.appendChild(card);
      });
      citations.appendChild(list);
      body.appendChild(citations);
    }

    // Dynamic Follow-up Suggestions
    const followUps = generateFollowUps(data.answer);
    if (followUps.length > 0) {
      const followUpWrap = document.createElement("div");
      followUpWrap.className = "quick-starter-chips";
      followUpWrap.style.marginTop = "14px";
      followUps.forEach((q) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "starter-chip";
        btn.setAttribute("data-query", q.query);
        btn.innerHTML = `${q.icon} ${escapeHTML(q.label)}`;
        btn.addEventListener("click", () => {
          userInput.value = q.query;
          chatForm.dispatchEvent(new Event("submit"));
        });
        followUpWrap.appendChild(btn);
      });
      body.appendChild(followUpWrap);
    }

    // Action toolbar: Explain Simply, Read Aloud, Copy, Reactions
    const actions = document.createElement("div");
    actions.className = "message-actions";

    // 1. Explain more simply
    if (!data.is_crisis) {
      const simplifyBtn = document.createElement("button");
      simplifyBtn.className = "action-btn";
      simplifyBtn.type = "button";
      simplifyBtn.innerHTML = `🌍 Explain simply`;
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

    // 4. Plain-English Glossary Pills
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

    // 5. Tactile Feedback Reactions
    const reactions = document.createElement("div");
    reactions.className = "feedback-actions";
    reactions.innerHTML = `
      <button type="button" class="reaction-btn" title="Helpful answer">👍 Helpful</button>
      <button type="button" class="reaction-btn" title="Learned something new">💡 Learned</button>
    `;
    reactions.querySelectorAll(".reaction-btn").forEach((rBtn) => {
      rBtn.addEventListener("click", () => {
        rBtn.classList.toggle("reacted");
        playChimeTone(784, 0.08); // G5 feedback chime
      });
    });
    actions.appendChild(reactions);

    msgDiv.appendChild(header);
    msgDiv.appendChild(body);
    msgDiv.appendChild(actions);

    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function generateFollowUps(answerText) {
    const text = (answerText || "").toLowerCase();
    const suggestions = [];

    if (text.includes("accommodation") || text.includes("room") || text.includes("hall") || text.includes("bedroom")) {
      suggestions.push({ icon: "👨‍👩‍👦", label: "Can parents stay overnight?", query: "Can parents stay overnight in halls during the STAR residential?" });
      suggestions.push({ icon: "🎒", label: "What should I pack?", query: "What should I pack for the 3-day STAR residential?" });
    } else if (text.includes("isp") || text.includes("inclusive support plan") || text.includes("exam") || text.includes("disability")) {
      suggestions.push({ icon: "🎓", label: "What does DSA funding cover?", query: "What is Disabled Students' Allowance (DSA) and is it a loan?" });
      suggestions.push({ icon: "💡", label: "ADHD and dyslexia support?", query: "What support is available at UCLan for students with dyslexia or ADHD?" });
    } else if (text.includes("cost") || text.includes("free") || text.includes("meal") || text.includes("food")) {
      suggestions.push({ icon: "📍", label: "Where do I register on Day 1?", query: "Where do I check in on the first day of the STAR programme?" });
      suggestions.push({ icon: "🛏️", label: "Are bedrooms en-suite?", query: "Are the accommodation rooms during STAR en-suite and do I get my own bedroom?" });
    }
    return suggestions.slice(0, 2);
  }

  function escapeHTML(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function formatMarkdown(text) {
    if (!text) return "";
    let html = escapeHTML(text);
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");
    html = html.replace(/^### (.*$)/gim, "<h4>$1</h4>");
    html = html.replace(/^\* (.*$)/gim, "<li>$1</li>");
    html = html.replace(/^- (.*$)/gim, "<li>$1</li>");
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1 ↗</a>');
    html = html.split("\n\n").map(p => p.startsWith("<li>") ? `<ul>${p}</ul>` : `<p>${p}</p>`).join("");
    return html;
  }

  // --- Copy Share URL on About Page ---
  const copyShareBtn = document.getElementById("copy-share-url-btn");
  if (copyShareBtn) {
    copyShareBtn.addEventListener("click", () => {
      const shareUrl = window.location.origin;
      navigator.clipboard.writeText(shareUrl).then(() => {
        copyShareBtn.innerHTML = `✓ Link Copied!`;
        playSuccessChime();
        setTimeout(() => { copyShareBtn.innerHTML = `🔗 Copy Assistant Link`; }, 2500);
      });
    });
  }

  // --- Evaluation Dashboard Runner & Live Search ---
  const runEvalBtn = document.getElementById("run-eval-btn");
  const evalSpinner = document.getElementById("eval-spinner");
  const ragAccEl = document.getElementById("rag-acc");
  const baselineAccEl = document.getElementById("baseline-acc");
  const safetyAccEl = document.getElementById("safety-acc");
  const honestAccEl = document.getElementById("honest-acc");
  const ragBarEl = document.getElementById("rag-bar");
  const baselineBarEl = document.getElementById("baseline-bar");
  const safetyBarEl = document.getElementById("safety-bar");
  const honestBarEl = document.getElementById("honest-bar");
  const llmAddsDesc = document.getElementById("llm-adds-desc");
  const evalTableBody = document.getElementById("eval-table-body");
  const filterSelect = document.getElementById("filter-select");
  const tableSearch = document.getElementById("table-search");
  const tableCountLabel = document.getElementById("table-count-label");
  const exportCsvBtn = document.getElementById("export-csv-btn");

  let allEvaluationResults = [];

  if (runEvalBtn) {
    runEvalBtn.addEventListener("click", async () => {
      runEvalBtn.disabled = true;
      if (evalSpinner) evalSpinner.removeAttribute("hidden");
      announceToScreenReader("Running full benchmark evaluation across 35 scenarios...");

      try {
        const response = await fetch("/api/evaluate");
        const data = await response.json();

        // Update metric values and animate progress bars
        if (ragAccEl) ragAccEl.textContent = `${data.rag_accuracy_pct}%`;
        if (ragBarEl) ragBarEl.style.width = `${data.rag_accuracy_pct}%`;

        if (baselineAccEl) baselineAccEl.textContent = `${data.baseline_accuracy_pct}%`;
        if (baselineBarEl) baselineBarEl.style.width = `${data.baseline_accuracy_pct}%`;

        if (safetyAccEl) safetyAccEl.textContent = `${data.safety_guardrail_success_pct}%`;
        if (safetyBarEl) safetyBarEl.style.width = `${data.safety_guardrail_success_pct}%`;

        if (honestAccEl) honestAccEl.textContent = `${data.honest_refusal_success_pct}%`;
        if (honestBarEl) honestBarEl.style.width = `${data.honest_refusal_success_pct}%`;

        if (llmAddsDesc) {
          llmAddsDesc.innerHTML = `
            <strong>Empirical Finding:</strong> Grounded RAG achieved <strong>${data.rag_accuracy_pct}%</strong> overall accuracy 
            (In-scope: <strong>${data.rag_in_scope_accuracy_pct}%</strong>) compared to 
            <strong>${data.baseline_accuracy_pct}%</strong> for simple keyword matching. 
            <p style="margin-top:8px;">${escapeHTML(data.what_llm_adds)}</p>
          `;
        }

        allEvaluationResults = data.results || [];
        renderEvaluationTable(allEvaluationResults);

        if (filterSelect) filterSelect.disabled = false;
        if (tableSearch) tableSearch.disabled = false;
        if (exportCsvBtn) exportCsvBtn.disabled = false;
        playSuccessChime();
        announceToScreenReader("Evaluation complete. 35 scenarios verified.");
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

    if (tableCountLabel) {
      tableCountLabel.textContent = `Showing ${items.length} of ${allEvaluationResults.length} scenarios`;
    }

    if (items.length === 0) {
      evalTableBody.innerHTML = `<tr><td colspan="7" class="text-center empty-state"><p>No questions match your filter.</p></td></tr>`;
      return;
    }

    items.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td><strong>${escapeHTML(item.id)}</strong></td>
        <td><span class="tag-uclan">${escapeHTML(item.category)}</span></td>
        <td><strong>${escapeHTML(item.question)}</strong></td>
        <td><small><a href="${item.expected_source_url}" target="_blank" rel="noopener noreferrer">${item.expected_source_url === "none" ? "None (Out of Scope)" : "Source Page ↗"}</a></small></td>
        <td>${item.rag_pass ? '<span class="badge-pass">PASS ✓</span>' : '<span class="badge-miss">FAIL ✗</span>'}</td>
        <td>${item.baseline_pass ? '<span class="badge-pass">PASS ✓</span>' : '<span class="badge-miss">FAIL ✗</span>'}</td>
        <td><small>${escapeHTML(item.rag_answer)}</small></td>
      `;
      evalTableBody.appendChild(row);
    });
  }

  function applyFilters() {
    if (!allEvaluationResults.length) return;
    const catVal = filterSelect ? filterSelect.value : "all";
    const searchVal = tableSearch ? tableSearch.value.trim().toLowerCase() : "";

    let filtered = allEvaluationResults.filter((r) => {
      let matchesCat = true;
      if (catVal === "rag_pass") matchesCat = r.rag_pass;
      else if (catVal === "rag_miss") matchesCat = !r.rag_pass;
      else if (catVal === "crisis") matchesCat = r.is_crisis;
      else if (catVal === "out_of_scope") matchesCat = !r.is_in_scope;

      let matchesSearch = true;
      if (searchVal) {
        matchesSearch = r.question.toLowerCase().includes(searchVal) ||
                        r.category.toLowerCase().includes(searchVal) ||
                        (r.rag_answer && r.rag_answer.toLowerCase().includes(searchVal));
      }
      return matchesCat && matchesSearch;
    });

    renderEvaluationTable(filtered);
  }

  if (filterSelect) filterSelect.addEventListener("change", applyFilters);
  if (tableSearch) tableSearch.addEventListener("input", applyFilters);

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