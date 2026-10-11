/* ========================
   NAVBAR — scroll state
======================== */
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

/* ========================
   SCROLL REVEAL
   Adds .visible to elements with .reveal / .reveal-left / .reveal-right / .reveal-scale
======================== */
const revealSelectors = '.reveal, .reveal-left, .reveal-right, .reveal-scale';
const revealEls = document.querySelectorAll(revealSelectors);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

revealEls.forEach((el) => revealObserver.observe(el));

/* ========================
   TESTIMONIALS SLIDER
   Auto-scroll with pause on hover/drag
======================== */
const track = document.querySelector('.testimonials-track');
if (track) {
  let raf;
  let speed = 0.8;
  let isPaused = false;
  let isDragging = false;
  let startX = 0;
  let startScroll = 0;

  function autoScroll() {
    if (!isPaused && !isDragging) {
      track.scrollLeft += speed;
      // reset seamlessly at end
      if (track.scrollLeft >= track.scrollWidth - track.clientWidth - 2) {
        track.scrollLeft = 0;
      }
    }
    raf = requestAnimationFrame(autoScroll);
  }

  raf = requestAnimationFrame(autoScroll);

  // pause on hover
  track.addEventListener('mouseenter', () => { isPaused = true; });
  track.addEventListener('mouseleave', () => { isPaused = false; });

  // drag to scroll
  track.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.pageX - track.offsetLeft;
    startScroll = track.scrollLeft;
    track.style.cursor = 'grabbing';
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const x = e.pageX - track.offsetLeft;
    track.scrollLeft = startScroll - (x - startX);
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
    track.style.cursor = 'grab';
  });

  // touch support
  track.addEventListener('touchstart', (e) => {
    startX = e.touches[0].pageX;
    startScroll = track.scrollLeft;
    isPaused = true;
  }, { passive: true });

  track.addEventListener('touchmove', (e) => {
    const x = e.touches[0].pageX;
    track.scrollLeft = startScroll - (x - startX);
  }, { passive: true });

  track.addEventListener('touchend', () => {
    setTimeout(() => { isPaused = false; }, 1200);
  });
}

/* ========================
   PARALLAX — ethos bg
======================== */
const ethosBg = document.querySelector('.ethos-bg');
if (ethosBg) {
  window.addEventListener('scroll', () => {
    const ethos = ethosBg.parentElement;
    const rect = ethos.getBoundingClientRect();
    if (rect.bottom > 0 && rect.top < window.innerHeight) {
      const pct = rect.top / window.innerHeight;
      ethosBg.style.transform = `scale(1.08) translateY(${pct * 30}px)`;
    }
  }, { passive: true });
}

/* ========================
   NEWSLETTER FORM
======================== */
const form = document.querySelector('.newsletter-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input');
    const btn = form.querySelector('button');
    if (!input.value.trim()) return;

    btn.textContent = 'Subscribed ✓';
    btn.style.background = 'var(--olive)';
    btn.style.color = 'var(--gold)';
    btn.style.borderColor = 'var(--olive)';
    btn.style.letterSpacing = '0.08em';
    input.value = '';

    setTimeout(() => {
      btn.textContent = 'Subscribe';
      btn.style.background = '';
      btn.style.color = '';
      btn.style.borderColor = '';
      btn.style.letterSpacing = '';
    }, 3200);
  });
}

/* ========================
   STAGGER — product & archive cards
======================== */
function staggerCards(selector, baseDelay = 0) {
  document.querySelectorAll(selector).forEach((el, i) => {
    el.style.transitionDelay = `${baseDelay + i * 0.1}s`;
  });
}

staggerCards('.product-card');
staggerCards('.archive-card');
staggerCards('.step', 0.05);

/* ========================
   MOBILE MENU (Hamburger)
======================== */
const hamburgerBtn = document.getElementById('hamburgerBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (hamburgerBtn && mobileMenu) {
  hamburgerBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    hamburgerBtn.classList.toggle('active');
    mobileMenu.classList.toggle('open');
  });

  // Close mobile menu on click outside or on a menu link
  document.addEventListener('click', (e) => {
    if (e.target.closest('.mobile-link, .mobile-cta') || (!mobileMenu.contains(e.target) && !hamburgerBtn.contains(e.target))) {
      hamburgerBtn.classList.remove('active');
      mobileMenu.classList.remove('open');
    }
  });
}

/* ========================
   SERVICE TABS — keep active tab visible
======================== */
const activeTab = document.querySelector('.nav-tabs-card .nav-tab-item.active');
if (activeTab) {
  const card = activeTab.parentElement;
  card.scrollLeft = activeTab.offsetLeft - (card.clientWidth - activeTab.offsetWidth) / 2;
}
