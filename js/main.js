/**
 * INOVASS — Main JavaScript
 * Vanilla JS · No external dependencies
 */
'use strict';

const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

/* ── NAVBAR ── */
(function initNavbar() {
  const navbar    = $('#navbar');
  const hamburger = $('#hamburger');
  const navMenu   = $('#nav-menu');
  const navLinks  = $$('.nav-link');
  let lastScrollY = 0;
  let ticking     = false;

  function updateNavbar() {
    const cur = window.scrollY;
    navbar.classList.toggle('scrolled', cur > 20);
    if (cur > 200) {
      if (cur > lastScrollY + 4) { navbar.classList.add('hidden'); closeMenu(); }
      else if (cur < lastScrollY - 4) { navbar.classList.remove('hidden'); }
    } else {
      navbar.classList.remove('hidden');
    }
    lastScrollY = cur;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(updateNavbar); ticking = true; }
  }, { passive: true });

  function closeMenu() {
    navMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  function openMenu() {
    navMenu.classList.add('open');
    hamburger.classList.add('open');
    hamburger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  hamburger.addEventListener('click', () => {
    navMenu.classList.contains('open') ? closeMenu() : openMenu();
  });

  navLinks.forEach(link => link.addEventListener('click', closeMenu));

  document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target) && navMenu.classList.contains('open')) closeMenu();
  });

  $$('.has-dropdown').forEach(item => {
    item.querySelector('.nav-link').addEventListener('click', (e) => {
      if (window.getComputedStyle(hamburger).display !== 'none') {
        e.preventDefault();
        item.classList.toggle('open-mobile');
      }
    });
  });

  const sections = $$('section[id], footer[id]');
  const sectionObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  sections.forEach(sec => sectionObs.observe(sec));
})();

/* ── SCROLL ANIMATIONS ── */
(function initScrollAnimations() {
  const els = $$('.fade-in, .fade-up, .fade-in-left, .fade-in-right');
  if (!els.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(el => el.classList.add('visible'));
    return;
  }
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); obs.unobserve(entry.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => obs.observe(el));
})();

/* ── ANIMATED COUNTERS ── */
(function initCounters() {
  const counters = $$('.stat-number[data-target]');
  if (!counters.length) return;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function animateCounter(el) {
    const target   = parseInt(el.dataset.target, 10);
    const duration = 1800;
    const startTime = performance.now();
    function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }
    function tick(now) {
      const progress = Math.min((now - startTime) / duration, 1);
      el.textContent = Math.round(easeOutQuart(progress) * target);
      if (progress < 1) requestAnimationFrame(tick);
    }
    reduced ? (el.textContent = target) : requestAnimationFrame(tick);
  }

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { animateCounter(entry.target); obs.unobserve(entry.target); }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => obs.observe(c));
})();

/* ── SCROLL TO TOP ── */
(function initScrollTop() {
  const btn = $('#scrollTop');
  if (!btn) return;
  window.addEventListener('scroll', () => btn.classList.toggle('visible', window.scrollY > 400), { passive: true });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
})();

/* ── SMOOTH SCROLL ── */
(function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const navbarH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--navbar-h'), 10) || 72;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navbarH, behavior: 'smooth' });
    });
  });
})();

/* ── DROPDOWN KEYBOARD A11Y ── */
(function initDropdownA11y() {
  $$('.has-dropdown').forEach(item => {
    const toggle = item.querySelector('.nav-link');
    toggle.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const isOpen = item.classList.contains('open-kb');
        $$('.has-dropdown').forEach(d => d.classList.remove('open-kb'));
        if (!isOpen) item.classList.add('open-kb');
      }
      if (e.key === 'Escape') { item.classList.remove('open-kb'); toggle.focus(); }
    });
    document.addEventListener('click', (e) => { if (!item.contains(e.target)) item.classList.remove('open-kb'); });
  });
})();

/* ── HERO PARALLAX ── */
(function initParallax() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const heroBg = $('.hero__bg');
  if (!heroBg) return;
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > window.innerHeight) return;
    heroBg.style.transform = `translateY(${scrollY * 0.25}px)`;
  }, { passive: true });
})();
