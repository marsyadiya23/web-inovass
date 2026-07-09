/**
 * INOVASS — Main JavaScript
 * Vanilla JS only · No external dependencies
 */
'use strict';

/* =====================================================
   LOADING SCREEN
   ===================================================== */
(function initLoading() {
  const screen  = document.getElementById('loading-screen');
  const bar     = document.getElementById('loading-bar');
  const percent = document.getElementById('loading-percent');
  const brand   = document.getElementById('loading-brand-text');
  const letters = 'INOVASS'.split('');
  let letterIdx = 0;

  document.body.classList.add('loading');

  function typeLetter() {
    if (letterIdx < letters.length) {
      brand.textContent += letters[letterIdx++];
      setTimeout(typeLetter, 110);
    }
  }
  setTimeout(typeLetter, 400);

  const totalDuration = 2600;
  const startTime = performance.now();

  function animateProgress(now) {
    const elapsed  = now - startTime;
    const progress = Math.min(elapsed / totalDuration, 1);
    const pct = Math.round(progress * 100);
    bar.style.width = pct + '%';
    percent.textContent = pct + '%';
    if (progress < 1) {
      requestAnimationFrame(animateProgress);
    } else {
      setTimeout(() => {
        screen.classList.add('slide-away');
        document.body.classList.remove('loading');
        screen.addEventListener('transitionend', () => {
          screen.style.display = 'none';
        }, { once: true });
      }, 200);
    }
  }
  requestAnimationFrame(animateProgress);
})();

/* =====================================================
   NAVBAR
   ===================================================== */
(function initNavbar() {
  const navbar    = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const nav       = document.getElementById('navbar-nav');
  const navLinks  = document.querySelectorAll('.nav-link');
  const dropItems = document.querySelectorAll('.nav-item-dropdown');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
    updateActiveLink();
  }, { passive: true });

  hamburger.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    hamburger.classList.toggle('open', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen);
  });

  // Mobile dropdown toggle
  dropItems.forEach(item => {
    const link = item.querySelector('.nav-link-drop');
    if (link) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          item.classList.toggle('mobile-open');
        }
      });
    }
  });

  // Close nav on link click
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', false);
    });
  });

  // Active link on scroll
  const sections = document.querySelectorAll('section[id]');
  function updateActiveLink() {
    const scrollY = window.scrollY + 120;
    sections.forEach(sec => {
      const top  = sec.offsetTop;
      const h    = sec.offsetHeight;
      const id   = sec.getAttribute('id');
      const link = document.querySelector(`.nav-link[href="#${id}"]`);
      if (link) link.classList.toggle('active', scrollY >= top && scrollY < top + h);
    });
  }
})();
