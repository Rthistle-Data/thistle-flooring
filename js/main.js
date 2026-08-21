(function () {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    });
    nav.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        nav.classList.remove("is-open");
        toggle.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ── gallery filter + lightbox ── */
  const items = Array.from(document.querySelectorAll(".g-item"));
  const filters = document.querySelectorAll(".filter-btn");
  filters.forEach((btn) => {
    btn.addEventListener("click", () => {
      filters.forEach((b) => b.classList.remove("is-on"));
      btn.classList.add("is-on");
      const cat = btn.dataset.filter;
      items.forEach((el) => {
        const show = cat === "all" || el.dataset.cat === cat;
        el.style.display = show ? "" : "none";
      });
    });
  });

  const lb = document.querySelector(".lightbox");
  if (lb && items.length) {
    const lbImg = lb.querySelector("img");
    const lbCap = lb.querySelector(".lightbox-cap");
    let index = 0;
    const visible = () => items.filter((el) => el.style.display !== "none");

    const openAt = (i) => {
      const vis = visible();
      if (!vis.length) return;
      index = (i + vis.length) % vis.length;
      const fig = vis[index];
      const img = fig.querySelector("img");
      lbImg.src = img.src;
      lbImg.alt = img.alt || "";
      lbCap.textContent = fig.querySelector("figcaption")?.textContent || "";
      lb.classList.add("is-open");
      document.body.style.overflow = "hidden";
    };
    const close = () => {
      lb.classList.remove("is-open");
      document.body.style.overflow = "";
    };

    items.forEach((fig) => {
      fig.addEventListener("click", () => {
        const vis = visible();
        openAt(vis.indexOf(fig));
      });
    });
    lb.querySelector(".lb-close")?.addEventListener("click", close);
    lb.querySelector(".lb-prev")?.addEventListener("click", () => openAt(index - 1));
    lb.querySelector(".lb-next")?.addEventListener("click", () => openAt(index + 1));
    lb.addEventListener("click", (e) => {
      if (e.target === lb) close();
    });
    document.addEventListener("keydown", (e) => {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") openAt(index - 1);
      if (e.key === "ArrowRight") openAt(index + 1);
    });
  }

  /* ── quote form → server email ── */
  const form = document.getElementById("quote-form");
  if (form) {
    const ok = form.querySelector(".form-success");
    const errEl = form.querySelector(".form-error");
    const btn = form.querySelector('button[type="submit"]');
    const idleLabel = btn ? btn.textContent : "Send quote request";

    const show = (el, on) => {
      if (!el) return;
      el.classList.toggle("is-on", Boolean(on));
    };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const payload = {
        name: (data.get("name") || "").toString().trim(),
        email: (data.get("email") || "").toString().trim(),
        phone: (data.get("phone") || "").toString().trim(),
        project: (data.get("project") || "").toString().trim(),
        sqft: (data.get("sqft") || "").toString().trim(),
        message: (data.get("message") || "").toString().trim(),
        website: (data.get("website") || "").toString().trim(),
      };

      if (!payload.name || !payload.email) {
        form.reportValidity();
        return;
      }

      show(ok, false);
      show(errEl, false);
      if (btn) {
        btn.disabled = true;
        btn.textContent = "Sending…";
      }

      try {
        const res = await fetch("/api/quote", {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(payload),
        });
        const result = await res.json().catch(() => ({}));
        if (!res.ok || !result.ok) {
          throw new Error(result.error || "Couldn’t send the quote just now.");
        }
        form.reset();
        show(ok, true);
      } catch (err) {
        if (errEl) {
          errEl.textContent =
            err.message || "Couldn’t send the quote. Please text (587) 594-8169.";
        }
        show(errEl, true);
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.textContent = idleLabel;
        }
      }
    });
  }

  const copyBtn = document.getElementById("copy-email");
  if (copyBtn) {
    copyBtn.addEventListener("click", async () => {
      const email = copyBtn.dataset.email || "thistleflooringinstalls@gmail.com";
      try {
        await navigator.clipboard.writeText(email);
        copyBtn.textContent = "Email copied";
        setTimeout(() => {
          copyBtn.textContent = "Copy email address";
        }, 2000);
      } catch {
        window.prompt("Copy email address", email);
      }
    });
  }
})();
