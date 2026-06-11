/* =============================================
   LABORATOIRE INTERNATIONAL - Main JavaScript
   Modern Healthcare SaaS - 2026
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

    // --- Reduced Motion Preference ---
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- Navbar Scroll Effect (Debounced) ---
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                const scrollY = window.scrollY;

                if (scrollY > 60) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }

                if (backToTop) {
                    if (scrollY > 400) {
                        backToTop.classList.add('visible');
                    } else {
                        backToTop.classList.remove('visible');
                    }
                }
                ticking = false;
            });
            ticking = true;
        }
    });

    // --- Back to Top ---
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- Mobile Nav Toggle ---
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navOverlay = document.getElementById('navOverlay');

    function openNav() {
        navToggle.classList.add('active');
        navMenu.classList.add('active');
        if (navOverlay) navOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeNav() {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        if (navOverlay) navOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            if (navMenu.classList.contains('active')) {
                closeNav();
            } else {
                openNav();
            }
        });

        if (navOverlay) {
            navOverlay.addEventListener('click', closeNav);
        }

        document.querySelectorAll('.nav-menu .nav-link').forEach(link => {
            link.addEventListener('click', closeNav);
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                closeNav();
            }
        });
    }

    // --- Scroll Animations ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (prefersReducedMotion) {
                    entry.target.style.transition = 'none';
                }
                entry.target.classList.add('visible');

                if (entry.target.classList.contains('stat-bar-fill')) {
                    entry.target.classList.add('animate');
                }
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right, .stat-bar-fill').forEach(el => {
        if (prefersReducedMotion) {
            el.classList.add('visible');
        } else {
            observer.observe(el);
        }
    });

    // --- Counter Animation ---
    const counterElements = document.querySelectorAll('.stat-number[data-target]');

    const animateCounter = (el) => {
        const target = el.getAttribute('data-target');
        const numericValue = parseFloat(target.replace(/[^0-9.]/g, ''));
        const suffix = target.replace(/[0-9.]/g, '');

        // Skip animation if reduced motion preferred
        if (prefersReducedMotion) {
            el.textContent = target;
            return;
        }

        const duration = 2000;
        const start = performance.now();

        const update = (currentTime) => {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(numericValue * easeOut * 10) / 10;

            el.textContent = (Number.isInteger(numericValue) ? Math.floor(current) : current.toFixed(1)) + suffix;

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                el.textContent = target;
            }
        };

        requestAnimationFrame(update);
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counterElements.forEach(el => {
        if (prefersReducedMotion) {
            el.textContent = el.getAttribute('data-target');
        } else {
            counterObserver.observe(el);
        }
    });

    // --- Services Accordion (with ARIA) ---
    document.querySelectorAll('.category-header').forEach(header => {
        header.addEventListener('click', () => {
            const body = header.nextElementSibling;
            const isActive = header.classList.contains('active');

            // Close all
            document.querySelectorAll('.category-header').forEach(h => {
                h.classList.remove('active');
                h.setAttribute('aria-expanded', 'false');
            });
            document.querySelectorAll('.category-body').forEach(b => b.classList.remove('active'));

            // Toggle current
            if (!isActive) {
                header.classList.add('active');
                header.setAttribute('aria-expanded', 'true');
                body.classList.add('active');
            }
        });

        // Keyboard support
        header.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                header.click();
            }
        });
    });

    // Open first category by default
    const firstCategory = document.querySelector('.category-header');
    if (firstCategory) {
        firstCategory.classList.add('active');
        firstCategory.setAttribute('aria-expanded', 'true');
        firstCategory.nextElementSibling.classList.add('active');
    }

    // --- Password Visibility Toggle ---
    const passwordToggle = document.getElementById('passwordToggle');
    const passwordInput = document.getElementById('patientCode');
    if (passwordToggle && passwordInput) {
        passwordToggle.addEventListener('click', () => {
            const type = passwordInput.type === 'password' ? 'text' : 'password';
            passwordInput.type = type;
            const icon = passwordToggle.querySelector('i');
            icon.classList.toggle('fa-eye');
            icon.classList.toggle('fa-eye-slash');
            passwordToggle.setAttribute('aria-label',
                type === 'password' ? 'Afficher le mot de passe' : 'Masquer le mot de passe'
            );
        });
    }

    // --- Results Portal Integration ---
    const resultsForm = document.getElementById('resultsForm');
    if (resultsForm) {
        resultsForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const patientIdEl = document.getElementById('patientId');
            const patientCodeEl = document.getElementById('patientCode');
            
            const patientIdRaw = patientIdEl.value.trim();
            const patientCodeRaw = patientCodeEl.value.trim();
            
            if (!patientIdRaw || !patientCodeRaw) {
                resultsForm.reportValidity();
                return;
            }

            const btn = resultsForm.querySelector('button[type="submit"]');
            const originalHTML = btn.innerHTML;

            // Loading state
            btn.disabled = true;
            btn.classList.add('btn-loading');
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Connexion...';

            // Open new tab synchronously to prevent browser popup blockers
            const newWin = window.open('about:blank', '_blank');

            // 1. Create hidden iframe for authentication cookie setting
            let iframe = document.getElementById('authIframe');
            if (!iframe) {
                iframe = document.createElement('iframe');
                iframe.id = 'authIframe';
                iframe.name = 'authIFrameTarget';
                iframe.style.display = 'none';
                document.body.appendChild(iframe);
            }
            
            // 2. Create and submit hidden form to set session cookies
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = 'http://liamt.ddns.net:12543/visionlis/authenticatepatient';
            form.target = 'authIFrameTarget';
            
            const usernameInput = document.createElement('input');
            usernameInput.type = 'hidden';
            usernameInput.name = 'username';
            usernameInput.value = patientIdRaw;
            
            const passwordInput = document.createElement('input');
            passwordInput.type = 'hidden';
            passwordInput.name = 'password';
            passwordInput.value = patientCodeRaw;
            
            form.appendChild(usernameInput);
            form.appendChild(passwordInput);
            document.body.appendChild(form);
            form.submit();
            
            // Clean up the form
            setTimeout(() => {
                if (form.parentNode) {
                    form.parentNode.removeChild(form);
                }
            }, 500);

            const patientId = encodeURIComponent(patientIdRaw);
            const patientCode = encodeURIComponent(patientCodeRaw);
            
            // VisionLIS Patient portal link
            const targetUrl = `http://liamt.ddns.net:12543/visionlis/#/loginpatient?username=${patientId}&password=${patientCode}&user=${patientId}&pass=${patientCode}&login=${patientId}&code=${patientCode}&id=${patientId}`;

            // Redirect new window to VisionLIS
            setTimeout(() => {
                if (newWin) {
                    newWin.location.href = targetUrl;
                    
                    // Same-origin prefill fallback (in case pages run under same port/domain)
                    setTimeout(() => {
                        try {
                            const doc = newWin.document;
                            const uInput = doc.querySelector('input[ng-model="$parent.username"]');
                            const pInput = doc.querySelector('input[ng-model="$parent.password"]');
                            if (uInput && pInput) {
                                uInput.value = patientIdRaw;
                                pInput.value = patientCodeRaw;
                                uInput.dispatchEvent(new Event('input', { bubbles: true }));
                                pInput.dispatchEvent(new Event('input', { bubbles: true }));
                                const submitBtn = doc.querySelector('button[ng-click="login()"]');
                                if (submitBtn) submitBtn.click();
                            }
                        } catch (err) {
                            console.log("Cross-origin access restricted. Utilizing session cookies/URL params.");
                        }
                    }, 1200);
                }
                
                btn.disabled = false;
                btn.classList.remove('btn-loading');
                btn.innerHTML = originalHTML;
            }, 1000);
        });
    }

    // --- Contact Form ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const msgDiv = document.getElementById('formMessage');
            const originalHTML = submitBtn.innerHTML;

            submitBtn.disabled = true;
            submitBtn.classList.add('btn-loading');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Envoi en cours...';

            const formData = {
                name: contactForm.querySelector('#name').value,
                email: contactForm.querySelector('#email').value,
                phone: contactForm.querySelector('#phone').value,
                subject: contactForm.querySelector('#subject').value,
                message: contactForm.querySelector('#message').value,
            };

            try {
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                const response = await fetch('/contact/submit/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                    body: JSON.stringify(formData),
                });

                const result = await response.json();

                msgDiv.className = 'form-message ' + (result.success ? 'success' : 'error');
                msgDiv.innerHTML = `<i class="fas fa-${result.success ? 'check-circle' : 'exclamation-circle'}"></i> ${result.message}`;

                if (result.success) {
                    contactForm.reset();
                }
            } catch (err) {
                msgDiv.className = 'form-message error';
                msgDiv.innerHTML = '<i class="fas fa-exclamation-circle"></i> Une erreur est survenue. Veuillez réessayer ou nous appeler directement.';
            }

            submitBtn.disabled = false;
            submitBtn.classList.remove('btn-loading');
            submitBtn.innerHTML = originalHTML;
        });
    }

    // --- Responsive Table Detection ---
    function updateResponsiveTables() {
        const tables = document.querySelectorAll('.demo-results');
        const isMobile = window.innerWidth <= 768;
        tables.forEach(table => {
            if (isMobile) {
                table.classList.add('responsive');
            } else {
                table.classList.remove('responsive');
            }
        });
    }

    updateResponsiveTables();
    window.addEventListener('resize', updateResponsiveTables);

    // --- Smooth Scroll for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;
            const targetEl = document.querySelector(targetId);
            if (targetEl) {
                e.preventDefault();
                targetEl.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // --- Hero Particles ---
    const particlesContainer = document.querySelector('.hero-particles');
    if (particlesContainer && !prefersReducedMotion) {
        for (let i = 0; i < 25; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.width = (Math.random() * 5 + 2) + 'px';
            particle.style.height = particle.style.width;
            particle.style.animationDuration = (Math.random() * 15 + 10) + 's';
            particle.style.animationDelay = (Math.random() * 10) + 's';
            particlesContainer.appendChild(particle);
        }
    }
});
