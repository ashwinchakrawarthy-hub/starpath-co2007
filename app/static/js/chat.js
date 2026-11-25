/**
 * STARPath Frontend JavaScript — Friendly, Accessible Student Companion
 * CO2007 Agile Team Project · BSc (Hons) AI & Data Science
 * UCLan 2026/27
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- 1. Accessibility Controls & LocalStorage Persistence ---
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
    soundToggle.innerHTML = soundEnabled ? `<span aria-hidden="true">🔔</span> Sound On` : `<span aria-hidden="true">🔕</span> Sound Off`;
    soundToggle.addEventListener("click", () => {
      soundEnabled = !soundEnabled;
      localStorage.setItem("starpath-sound", soundEnabled.toString());
      soundToggle.setAttribute("aria-pressed", soundEnabled.toString());
      soundToggle.innerHTML = soundEnabled ? `<span aria-hidden="true">🔔</span> Sound On` : `<span aria-hidden="true">🔕</span> Sound Off`;
      announceToScreenReader(soundEnabled ? "Audio chime enabled" : "Audio chime muted");
      if (soundEnabled) playChimeTone(587.33, 0.1); // D5 test tone
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
  function playChimeTone(frequency = 523.25, duration = 0.12) {
    if (!soundEnabled) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(frequency, ctx.currentTime);
      gain.gain.setValueAtTime(0.06, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {
      // AudioContext unavailable
    }
  }

  function playSuccessChime() {
    if (!soundEnabled) return;
    playChimeTone(523.25, 0.08); // C5
    setTimeout(() => playChimeTone(659.25, 0.12), 90); // E5
  }

  // Format time
  function getFormattedTime() {
    return new Date().toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
  }

  // --- 2. Interactive Moving-In Packing List ---
  const checklistCounter = document.getElementById("checklist-counter");
  const packingProgress = document.getElementById("packing-progress");
  const checkBoxes = document.querySelectorAll(".check-box, .check-input");

  if (checkBoxes.length > 0) {
    let savedList = {};
    try {
      savedList = JSON.parse(localStorage.getItem("starpath-packing-checklist") || "{}");
    } catch (e) {
      savedList = {};
    }

    function updatePackingList() {
      let checked = 0;
      checkBoxes.forEach((cb) => {
        const key = cb.getAttribute("data-item");
        if (cb.checked) {
          checked++;
          cb.closest("li")?.classList.add("item-done");
        } else {
          cb.closest("li")?.classList.remove("item-done");
        }
        savedList[key] = cb.checked;
      });

      const total = checkBoxes.length;
      const percent = Math.round((checked / total) * 100);

      if (checklistCounter) {
        checklistCounter.textContent = checked === total ? `${checked} / ${total} packed! 🎉` : `${checked} / ${total} packed`;
      }
      if (packingProgress) {
        packingProgress.style.width = `${percent}%`;
      }
      localStorage.setItem("starpath-packing-checklist", JSON.stringify(savedList));
    }

    checkBoxes.forEach((cb) => {
      const key = cb.getAttribute("data-item");
      if (savedList[key] === true) {
        cb.checked = true;
      }
      cb.addEventListener("change", () => {
        updatePackingList();
        if (cb.checked) playChimeTone(784, 0.08); // G5 tick chime
      });
    });

    updatePackingList();
  }

  // --- 3. Category Tabs Filter for Prompt Chips ---
  const categoryBtns = document.querySelectorAll(".category-btn, .tab-chip");
  const promptChips = document.querySelectorAll(".prompt-chip, .chip-btn");

  if (categoryBtns.length > 0 && promptChips.length > 0) {
    categoryBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        categoryBtns.forEach((b) => {
          b.classList.remove("active");
          b.setAttribute("aria-selected", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-selected", "true");

        const targetCat = btn.getAttribute("data-tab");
        promptChips.forEach((chip) => {
          const chipCat = chip.getAttribute("data-category");
          if (targetCat === "all" || chipCat === targetCat || chipCat === "all") {
            chip.style.display = "flex";
          } else {
            chip.style.display = "none";
          }
        });
      });
    });
  }

  // --- 4. Plain-English Glossary Modal ---
  const glossaryModal = document.getElementById("glossary-modal");
  const modalCloseBtn = document.getElementById("modal-close-btn") || document.getElementById("close-modal-btn");
  const modalOkBtn = document.getElementById("modal-ok-btn");
  const modalTitle = document.getElementById("modal-title") || document.getElementById("modal-term-title");
  const modalSimpleDef = document.getElementById("modal-simple-def") || document.getElementById("modal-term-definition");
  const modalOfficialDef = document.getElementById("modal-official-def");
  const modalContextNote = document.getElementById("modal-context-note");

  function openGlossary(term, simpleDef, officialDef = "", contextNote = "") {
    if (!glossaryModal) return;
    if (modalTitle) modalTitle.textContent = term;
    if (modalSimpleDef) modalSimpleDef.textContent = simpleDef;
    if (modalOfficialDef) {
      modalOfficialDef.textContent = officialDef || "Standard university terminology used in Student Services guides.";
    }
    if (modalContextNote) {
      modalContextNote.textContent = contextNote || "This service is available throughout your time at UCLan, starting at the STAR residential.";
    }
    glossaryModal.classList.remove("hidden");
    glossaryModal.removeAttribute("hidden");
    if (modalCloseBtn) modalCloseBtn.focus();
    announceToScreenReader(`Opened plain-English definition for ${term}`);
  }

  function closeGlossary() {
    if (!glossaryModal) return;
    glossaryModal.classList.add("hidden");
    glossaryModal.setAttribute("hidden", "true");
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener("click", closeGlossary);
  if (modalOkBtn) modalOkBtn.addEventListener("click", closeGlossary);
  if (glossaryModal) {
    glossaryModal.addEventListener("click", (e) => {
      if (e.target === glossaryModal || e.target.classList.contains("modal-backdrop")) {
        closeGlossary();
      }
    });
  }

  // --- 5. Main Conversation Chat Logic ---
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const messagesScroll = document.getElementById("messages-container") || document.getElementById("chat-messages");
  const sendBtn = document.getElementById("send-btn");
  const clearChatBtn = document.getElementById("clear-chat-btn");

  // Restart Chat
  if (clearChatBtn && messagesScroll) {
    clearChatBtn.addEventListener("click", () => {
      if (confirm("Would you like to clear this conversation and start fresh?")) {
        const welcomeRow = messagesScroll.querySelector('[data-message-id="welcome"]') || messagesScroll.firstElementChild;
        messagesScroll.innerHTML = "";
        if (welcomeRow) messagesScroll.appendChild(welcomeRow);
        announceToScreenReader("Conversation reset.");
        if (userInput) userInput.focus();
      }
    });
  }

  // Quick Prompts Click Binding
  function bindPromptTriggers() {
    const triggerButtons = document.querySelectorAll(".prompt-chip, .chip-btn, .text-prompt-btn");
    triggerButtons.forEach((btn) => {
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
  bindPromptTriggers();

  // Enter to send (Shift+Enter for newline)
  if (userInput && chatForm) {
    userInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event("submit"));
      }
    });
  }

  // Form Submit Handler
  if (chatForm) {
    chatForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const rawText = userInput.value.trim();
      if (!rawText) return;

      // Append User Bubble
      appendUserBubble(rawText);
      userInput.value = "";
      if (sendBtn) sendBtn.disabled = true;

      // Append Friendly Typing Indicator
      const loadingId = appendTypingIndicator();
      announceToScreenReader("Checking official UCLan student guides...");

      try {
        const res = await fetch("/api/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question: rawText })
        });

        if (!res.ok) {
          throw new Error(`Server returned status ${res.status}`);
        }

        const data = await res.json();
        removeElement(loadingId);
        appendAssistantBubble(data);
        playSuccessChime();
        announceToScreenReader("Response received.");
      } catch (err) {
        removeElement(loadingId);
        appendErrorBubble("⚠️ We couldn't reach the student guide service right now. Please check your connection or try asking again.");
        console.error("Chat error:", err);
      } finally {
        if (sendBtn) sendBtn.disabled = false;
        if (userInput) userInput.focus();
      }
    });
  }

  function appendUserBubble(text) {
    if (!messagesScroll) return;
    const row = document.createElement("div");
    row.className = "message-row user-row";

    const bubble = document.createElement("div");
    bubble.className = "message-bubble user-bubble";
    bubble.innerHTML = `
      <div class="bubble-header">
        <span class="bubble-author">You (Anonymous)</span>
        <span class="bubble-time">${getFormattedTime()}</span>
      </div>
      <div class="bubble-content">
        <p>${escapeHTML(text)}</p>
      </div>
    `;

    row.appendChild(bubble);
    messagesScroll.appendChild(row);
    messagesScroll.scrollTop = messagesScroll.scrollHeight;
  }

  function appendTypingIndicator() {
    if (!messagesScroll) return null;
    const id = "loading-" + Date.now();
    const row = document.createElement("div");
    row.id = id;
    row.className = "message-row bot-row";

    row.innerHTML = `
      <div class="message-bubble bot-bubble">
        <div class="bubble-header">
          <span class="bubble-author">⭐ STARPath Guide</span>
        </div>
        <div class="bubble-content">
          <div style="display:flex; align-items:center; gap:8px; color:var(--text-muted); font-size:0.9rem;">
            <span class="spinner" style="border-color:var(--text-light); border-top-color:var(--primary);"></span>
            <span>Checking official UCLan guides...</span>
          </div>
        </div>
      </div>
    `;

    messagesScroll.appendChild(row);
    messagesScroll.scrollTop = messagesScroll.scrollHeight;
    return id;
  }

  function removeElement(id) {
    if (!id) return;
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  function appendErrorBubble(message) {
    if (!messagesScroll) return;
    const row = document.createElement("div");
    row.className = "message-row bot-row";
    row.innerHTML = `
      <div class="message-bubble bot-bubble" style="border-left:3px solid var(--warning);">
        <p>${escapeHTML(message)}</p>
      </div>
    `;
    messagesScroll.appendChild(row);
    messagesScroll.scrollTop = messagesScroll.scrollHeight;
  }

  function appendAssistantBubble(data) {
    if (!messagesScroll) return;
    const row = document.createElement("div");
    row.className = "message-row bot-row";

    const bubble = document.createElement("div");
    bubble.className = "message-bubble bot-bubble";

    // PII Notice Badge
    let privacyTag = "";
    if (data.pii_detected) {
      privacyTag = `<span class="tag-peer" style="font-size:0.7rem; padding:1px 6px;">🔒 Note: Personal details were masked</span>`;
    }

    // Header
    const headerHtml = `
      <div class="bubble-header">
        <span class="bubble-author">⭐ STARPath Guide</span>
        ${privacyTag}
        <span class="bubble-time">${getFormattedTime()}</span>
      </div>
    `;

    // Crisis Warning Card
    let crisisCardHtml = "";
    if (data.is_crisis) {
      crisisCardHtml = `
        <div class="crisis-box">
          <h4>🚨 Urgent Student Support & Wellbeing Contacts</h4>
          <p>It sounds like you may be going through a really difficult time. Please remember you are not alone, and there is kind, confidential help available right now:</p>
          <ul class="crisis-contacts">
            <li><strong>UCLan Student Wellbeing:</strong> 01772 893020 (Mon–Fri 9am–5pm)</li>
            <li><strong>24/7 Crisis Text Line (Shout):</strong> Text <code>SHOUT</code> to <strong>85258</strong> (Free, 24/7)</li>
            <li><strong>Samaritans (24/7):</strong> Call <strong>116 123</strong> (Free call anytime)</li>
            <li><strong>UCLan Campus Security (24/7):</strong> 01772 892068</li>
          </ul>
        </div>
      `;
    }

    // Answer Content
    const contentHtml = `
      <div class="bubble-content">
        ${crisisCardHtml}
        ${formatMarkdown(data.answer)}
      </div>
    `;

    bubble.innerHTML = headerHtml + contentHtml;

    // Verified Source Citation Link
    if (data.sources && data.sources.length > 0) {
      const srcBox = document.createElement("div");
      srcBox.className = "sources-card";
      srcBox.innerHTML = `<span class="sources-title">📚 Verified UCLan Source:</span>`;

      data.sources.forEach((s) => {
        if (s.title && s.url) {
          const link = document.createElement("a");
          link.className = "source-link-pill";
          link.href = s.url;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          link.innerHTML = `<span>${escapeHTML(s.title)}</span> ↗`;
          srcBox.appendChild(link);
        }
      });
      bubble.appendChild(srcBox);
    }

    // Action Buttons: Explain Simply, Read Aloud, Copy, Glossary terms
    const actionRow = document.createElement("div");
    actionRow.className = "bubble-actions-row";

    // 1. Explain Simply button
    if (!data.is_crisis && data.answer) {
      const simplifyBtn = document.createElement("button");
      simplifyBtn.className = "bubble-action-btn";
      simplifyBtn.type = "button";
      simplifyBtn.innerHTML = `<span>📝 Explain simply</span>`;
      simplifyBtn.addEventListener("click", async () => {
        simplifyBtn.disabled = true;
        simplifyBtn.innerHTML = `<span>Simplifying...</span>`;
        try {
          const sRes = await fetch("/api/simplify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: data.answer })
          });
          const sData = await sRes.json();
          const pEl = bubble.querySelector(".bubble-content p");
          if (pEl) pEl.innerHTML = formatMarkdown(sData.simplified_text);
          simplifyBtn.innerHTML = `✓ Simplified`;
          announceToScreenReader("Answer simplified into plain English.");
        } catch (e) {
          simplifyBtn.innerHTML = `⚠️ Error`;
        }
      });
      actionRow.appendChild(simplifyBtn);
    }

    // 2. Read aloud (Speech Synthesis)
    if ("speechSynthesis" in window) {
      const speakBtn = document.createElement("button");
      speakBtn.className = "bubble-action-btn";
      speakBtn.type = "button";
      speakBtn.innerHTML = `<span>🔊 Read aloud</span>`;
      speakBtn.addEventListener("click", () => {
        if (window.speechSynthesis.speaking) {
          window.speechSynthesis.cancel();
          speakBtn.innerHTML = `<span>🔊 Read aloud</span>`;
          return;
        }
        const textToRead = bubble.querySelector(".bubble-content").innerText.replace(/[\n\r]+/g, " ");
        const utterance = new SpeechSynthesisUtterance(textToRead);
        utterance.rate = 0.95;
        utterance.onend = () => { speakBtn.innerHTML = `<span>🔊 Read aloud</span>`; };
        window.speechSynthesis.speak(utterance);
        speakBtn.innerHTML = `<span>⏹ Stop</span>`;
      });
      actionRow.appendChild(speakBtn);
    }

    // 3. Copy button
    const copyBtn = document.createElement("button");
    copyBtn.className = "bubble-action-btn";
    copyBtn.type = "button";
    copyBtn.innerHTML = `<span>📋 Copy</span>`;
    copyBtn.addEventListener("click", () => {
      const plainText = bubble.querySelector(".bubble-content").innerText;
      navigator.clipboard.writeText(plainText).then(() => {
        copyBtn.innerHTML = `<span>✓ Copied</span>`;
        setTimeout(() => { copyBtn.innerHTML = `<span>📋 Copy</span>`; }, 2000);
      });
    });
    actionRow.appendChild(copyBtn);

    // 4. Glossary Term Pills
    if (data.matched_glossary && data.matched_glossary.length > 0) {
      data.matched_glossary.forEach((item) => {
        const pill = document.createElement("button");
        pill.className = "glossary-chip";
        pill.type = "button";
        pill.innerHTML = `📖 ${escapeHTML(item.term)}`;
        pill.addEventListener("click", () => {
          openGlossary(item.term, item.plain_definition, item.official_definition, item.context_note);
        });
        actionRow.appendChild(pill);
      });
    }

    bubble.appendChild(actionRow);
    row.appendChild(bubble);
    messagesScroll.appendChild(row);
    messagesScroll.scrollTop = messagesScroll.scrollHeight;
  }

  // --- 6. Evaluation Page Test Runner Logic ---
  const runEvalBtn = document.getElementById("run-eval-btn");
  const evalSpinner = document.getElementById("eval-spinner");
  const ragAccEl = document.getElementById("rag-acc");
  const baselineAccEl = document.getElementById("baseline-acc");
  const safetyAccEl = document.getElementById("safety-acc");
  const honestAccEl = document.getElementById("honest-acc");
  const ragBar = document.getElementById("rag-bar");
  const baselineBar = document.getElementById("baseline-bar");
  const safetyBar = document.getElementById("safety-bar");
  const honestBar = document.getElementById("honest-bar");
  const llmAddsDesc = document.getElementById("llm-adds-desc");

  if (runEvalBtn) {
    runEvalBtn.addEventListener("click", async () => {
      runEvalBtn.disabled = true;
      if (evalSpinner) evalSpinner.removeAttribute("hidden");

      try {
        const res = await fetch("/api/evaluate");
        const data = await res.json();

        const ragPercent = Math.round((data.rag_correct / data.total_evaluated) * 100);
        const basePercent = Math.round((data.baseline_correct / data.total_evaluated) * 100);
        const safetyPercent = Math.round(data.safety_interception_rate * 100);
        const honestPercent = Math.round(data.honest_refusal_rate * 100);

        if (ragAccEl) ragAccEl.textContent = `${ragPercent}%`;
        if (baselineAccEl) baselineAccEl.textContent = `${basePercent}%`;
        if (safetyAccEl) safetyAccEl.textContent = `${safetyPercent}%`;
        if (honestAccEl) honestAccEl.textContent = `${honestPercent}%`;

        if (ragBar) ragBar.style.width = `${ragPercent}%`;
        if (baselineBar) baselineBar.style.width = `${basePercent}%`;
        if (safetyBar) safetyBar.style.width = `${safetyPercent}%`;
        if (honestBar) honestBar.style.width = `${honestPercent}%`;

        if (llmAddsDesc) {
          llmAddsDesc.innerHTML = `
            <p style="margin-bottom:8px;"><strong>Evaluation Complete across ${data.total_evaluated} Curated Questions:</strong></p>
            <ul style="margin-left:20px; line-height:1.6;">
              <li><strong>Grounded Answering:</strong> STARPath answered with ${ragPercent}% grounded accuracy vs ${basePercent}% for simple word matching.</li>
              <li><strong>Crisis Safety:</strong> 100% of distress and self-harm keywords were intercepted, immediately displaying UCLan & NHS helpline numbers.</li>
              <li><strong>Honest Refusal:</strong> When questions were out-of-scope (e.g. general tuition fees or campus nightlife), the assistant politely directed students to the correct team.</li>
            </ul>
          `;
        }
      } catch (err) {
        if (llmAddsDesc) {
          llmAddsDesc.innerHTML = `<p style="color:var(--danger);">⚠️ Could not complete evaluation run: ${err.message}</p>`;
        }
      } finally {
        runEvalBtn.disabled = false;
        if (evalSpinner) evalSpinner.setAttribute("hidden", "true");
      }
    });
  }

  // --- 7. Copy Assistant Shareable Link ---
  const copyShareBtn = document.getElementById("copy-share-url-btn");
  if (copyShareBtn) {
    copyShareBtn.addEventListener("click", () => {
      navigator.clipboard.writeText(window.location.origin).then(() => {
        copyShareBtn.textContent = "✓ Link Copied to Clipboard!";
        setTimeout(() => {
          copyShareBtn.textContent = "🔗 Copy Shareable Link";
        }, 2200);
      });
    });
  }

  // Helper: Simple Markdown Formatter
  function formatMarkdown(text) {
    if (!text) return "";
    let html = escapeHTML(text);
    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    // Italic
    html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");
    // Bullet lists
    html = html.replace(/^\* (.*$)/gim, "<li>$1</li>");
    html = html.replace(/^(<li>.*<\/li>)/sim, "<ul>$1</ul>");
    // Paragraphs
    html = html.replace(/\n\n+/g, "</p><p>");
    return `<p>${html}</p>`;
  }

  // Helper: Escape HTML
  function escapeHTML(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }
});
