// Navbar scroll effect
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.style.background = 'rgba(17, 17, 16, 0.96)';
  } else {
    navbar.style.background = 'rgba(26, 26, 24, 0.85)';
  }
});

// Testimonials auto-scroll
const track = document.querySelector('.testimonials-track');
let scrollDir = 1;
let autoScroll;

function startAutoScroll() {
  autoScroll = setInterval(() => {
    track.scrollLeft += scrollDir * 1.2;
    if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 10) {
      scrollDir = -1;
    } else if (track.scrollLeft <= 0) {
      scrollDir = 1;
    }
  }, 16);
}

startAutoScroll();

track.addEventListener('mouseenter', () => clearInterval(autoScroll));
track.addEventListener('mouseleave', startAutoScroll);

// Intersection Observer - fade in on scroll
const fadeEls = document.querySelectorAll(
  '.product-card, .step, .archive-card, .testimonial-card, .ethos-content, .newsletter-content'
);

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 }
);

fadeEls.forEach((el) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});

// Newsletter form
const form = document.querySelector('.newsletter-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const input = form.querySelector('input');
  const btn = form.querySelector('button');
  if (input.value) {
    btn.textContent = 'Subscribed ✓';
    btn.style.background = '#3a3d2e';
    btn.style.color = '#c9b89a';
    input.value = '';
    setTimeout(() => {
      btn.textContent = 'Subscribe';
      btn.style.background = '';
      btn.style.color = '';
    }, 3000);
  }
});
