/* ============================================================
   INOVASS – main.js
   ============================================================ */

// ── Loading Screen ────────────────────────────────────────────
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');
  const body   = document.body;

  // Simulate a minimum visible load time so the animation plays nicely
  setTimeout(() => {
    loader.classList.add('hide');
    body.classList.add('loaded');
  }, 2400);
});

// ── Navbar Scroll Shadow ─────────────────────────────────────
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ── Mobile Nav ────────────────────────────────────────────────
const hamburger  = document.getElementById('hamburger');
let   mobileNav  = null;

function buildMobileNav() {
  if (mobileNav) return mobileNav;

  mobileNav = document.createElement('div');
  mobileNav.className = 'mobile-nav';
  mobileNav.innerHTML = `
    <button class="mobile-nav-close" id="mobileNavClose">✕</button>
    <a href="#home"    class="mobile-link">Business</a>
    <a href="#pricing" class="mobile-link">Pricing</a>
    <a href="#features" class="mobile-link">Features</a>
    <a href="#about"   class="mobile-link">About</a>
    <a href="#" class="btn btn-primary">Login →</a>
  `;
  document.body.appendChild(mobileNav);

  document.getElementById('mobileNavClose').addEventListener('click', closeMobileNav);
  mobileNav.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', closeMobileNav);
  });

  return mobileNav;
}

function openMobileNav() {
  buildMobileNav();
  mobileNav.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeMobileNav() {
  if (mobileNav) mobileNav.classList.remove('open');
  document.body.style.overflow = '';
}

hamburger.addEventListener('click', openMobileNav);

// ── Scroll Reveal ─────────────────────────────────────────────
const revealEls = document.querySelectorAll(
  '.stats-inner, .stat-card, .pricing-card, .services-inner, .brands-inner, .cta-inner'
);

revealEls.forEach(el => el.classList.add('reveal'));

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger siblings
      const siblings = [...entry.target.parentElement.querySelectorAll('.reveal')];
      const idx = siblings.indexOf(entry.target);
      entry.target.style.transitionDelay = `${idx * 0.1}s`;
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

revealEls.forEach(el => revealObserver.observe(el));

// ── Counter Animation ─────────────────────────────────────────
function animateCounter(el) {
  const raw    = el.textContent.trim();
  const suffix = raw.replace(/[\d.]/g, '');  // e.g. 'k+', '%', '+'
  const num    = parseFloat(raw);
  if (isNaN(num)) return;

  let start     = 0;
  const duration = 1600;
  const step      = 16;
  const increment = num / (duration / step);

  const timer = setInterval(() => {
    start += increment;
    if (start >= num) {
      el.textContent = num + suffix;
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(start) + suffix;
    }
  }, step);
}

const statNumbers = document.querySelectorAll('.stat-number');
const counterObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

statNumbers.forEach(el => counterObserver.observe(el));

// ── Accordion ─────────────────────────────────────────────────
document.querySelectorAll('.accordion-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.accordion-item');
    const body = item.querySelector('.accordion-body');
    const isOpen = item.classList.contains('open');

    // Close all
    document.querySelectorAll('.accordion-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.accordion-body').classList.remove('show');
      i.querySelector('.accordion-btn').classList.remove('active');
    });

    // Open clicked if it was closed
    if (!isOpen) {
      item.classList.add('open');
      body.classList.add('show');
      btn.classList.add('active');
    }
  });
});

// ── Smooth active nav link highlight on scroll ────────────────
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) current = section.getAttribute('id');
  });

  navAnchors.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
}, { passive: true });

// ── Pricing card entrance animation ──────────────────────────
const pricingCards = document.querySelectorAll('.pricing-card');

const pricingObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const cards = [...entry.target.parentElement.querySelectorAll('.pricing-card')];
      const idx   = cards.indexOf(entry.target);
      entry.target.style.transitionDelay = `${idx * 0.15}s`;
      entry.target.style.opacity = '1';
      entry.target.style.transform = entry.target.classList.contains('featured')
        ? 'scale(1.04) translateY(0)'
        : 'translateY(0)';
      pricingObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

pricingCards.forEach(card => {
  card.style.opacity = '0';
  card.style.transform = card.classList.contains('featured')
    ? 'scale(1.04) translateY(20px)'
    : 'translateY(20px)';
  card.style.transition = 'opacity .6s ease, transform .6s ease';
  pricingObserver.observe(card);
});
