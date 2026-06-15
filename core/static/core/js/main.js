/**
 * Laboratoire International — Main JavaScript
 * Handles: navbar scroll, mobile nav, language switcher, scroll animations,
 * back-to-top, cookie consent
 */

(function () {
  'use strict';

  // ============================================
  // Navbar Scroll Effect
  // ============================================
  const navbar = document.getElementById('navbar');

  function updateNavbar() {
    if (!navbar) return;
    const scrolled = window.scrollY > 50;
    navbar.classList.toggle('scrolled', scrolled);
  }

  window.addEventListener('scroll', updateNavbar, { passive: true });
  updateNavbar();

  // ============================================
  // Mobile Navigation
  // ============================================
  const navToggle = document.getElementById('navToggle');
  const navClose = document.getElementById('navClose');
  const mobileNav = document.getElementById('mobileNav');
  const navOverlay = document.getElementById('navOverlay');

  function openMobileNav() {
    if (!mobileNav) return;
    mobileNav.classList.add('active');
    navOverlay.classList.add('active');
    navToggle.classList.add('active');
    navToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (!mobileNav) return;
    mobileNav.classList.remove('active');
    navOverlay.classList.remove('active');
    navToggle.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (navToggle) navToggle.addEventListener('click', openMobileNav);
  if (navClose) navClose.addEventListener('click', closeMobileNav);
  if (navOverlay) navOverlay.addEventListener('click', closeMobileNav);

  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMobileNav();
  });

  // ============================================
  // Language Switcher
  // ============================================
  const langSwitcher = document.getElementById('langSwitcher');
  const langToggle = document.getElementById('langToggle');

  if (langToggle && langSwitcher) {
    langToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      const isOpen = langSwitcher.classList.toggle('open');
      langToggle.setAttribute('aria-expanded', isOpen);
    });

    document.addEventListener('click', function (e) {
      if (!langSwitcher.contains(e.target)) {
        langSwitcher.classList.remove('open');
        langToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ============================================
  // Scroll Animations (Intersection Observer)
  // ============================================
  const animatedElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');

  if ('IntersectionObserver' in window && animatedElements.length > 0) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
    );

    animatedElements.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // Fallback: show all elements
    animatedElements.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  // ============================================
  // Back to Top
  // ============================================
  const backToTop = document.getElementById('backToTop');

  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('is-visible', window.scrollY > 300);
    }, { passive: true });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ============================================
  // Cookie Consent
  // ============================================
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAccept = document.getElementById('cookieAccept');
  const cookieDecline = document.getElementById('cookieDecline');

  if (cookieBanner && !localStorage.getItem('cookie_consent')) {
    setTimeout(function () {
      cookieBanner.classList.add('is-visible');
    }, 1500);
  }

  function hideCookieBanner(value) {
    localStorage.setItem('cookie_consent', value);
    if (cookieBanner) cookieBanner.classList.remove('is-visible');
  }

  if (cookieAccept) cookieAccept.addEventListener('click', function () { hideCookieBanner('accepted'); });
  if (cookieDecline) cookieDecline.addEventListener('click', function () { hideCookieBanner('declined'); });

  // ============================================
  // Smooth scroll for anchor links
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      if (href === '#') return;
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
  // ============================================
  // Website Protection (Anti-Inspect & Anti-Copy)
  // ============================================
  // Disable Right Click
  document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
  });

  // Disable Copy/Cut/Drag
  document.addEventListener('copy', function (e) { e.preventDefault(); });
  document.addEventListener('cut', function (e) { e.preventDefault(); });
  document.addEventListener('dragstart', function (e) { e.preventDefault(); });

  // Disable Inspect element shortcuts & View Source
  document.addEventListener('keydown', function (e) {
    // Disable F12
    if (e.keyCode === 123) {
      e.preventDefault();
      return false;
    }
    // Disable Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C, Ctrl+Shift+K
    if (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67 || e.keyCode === 75)) {
      e.preventDefault();
      return false;
    }
    // Disable Ctrl+U (View Source)
    if (e.ctrlKey && e.keyCode === 85) {
      e.preventDefault();
      return false;
    }
    // Disable Ctrl+S (Save Page)
    if (e.ctrlKey && e.keyCode === 83) {
      e.preventDefault();
      return false;
    }
    // Disable Ctrl+A (Select All)
    if (e.ctrlKey && e.keyCode === 65) {
      e.preventDefault();
      return false;
    }
    // Disable Ctrl+C (Copy)
    if (e.ctrlKey && e.keyCode === 67) {
      e.preventDefault();
      return false;
    }
  });

})();
