/* =============================================
   LABORATOIRE INTERNATIONAL - Main JavaScript
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {
    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        if (scrollY > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        if (scrollY > 400) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
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

        // Close on overlay click
        if (navOverlay) {
            navOverlay.addEventListener('click', closeNav);
        }

        // Close on link click
        document.querySelectorAll('.nav-menu .nav-link').forEach(link => {
            link.addEventListener('click', closeNav);
        });

        // Close on Escape key
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
                entry.target.classList.add('visible');
                
                // Animate stat bars
                if (entry.target.classList.contains('stat-bar-fill')) {
                    entry.target.classList.add('animate');
                }
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right, .stat-bar-fill').forEach(el => {
        observer.observe(el);
    });

    // --- Counter Animation ---
    const counterElements = document.querySelectorAll('.stat-number[data-target]');
    
    const animateCounter = (el) => {
        const target = el.getAttribute('data-target');
        const isPercent = target.includes('%');
        const isPlus = target.includes('+');
        const numericValue = parseFloat(target.replace(/[^0-9.]/g, ''));
        const suffix = target.replace(/[0-9.]/g, '');
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

    counterElements.forEach(el => counterObserver.observe(el));

    // --- Services Accordion (services page) ---
    document.querySelectorAll('.category-header').forEach(header => {
        header.addEventListener('click', () => {
            const body = header.nextElementSibling;
            const isActive = header.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.category-header').forEach(h => h.classList.remove('active'));
            document.querySelectorAll('.category-body').forEach(b => b.classList.remove('active'));
            
            // Toggle current
            if (!isActive) {
                header.classList.add('active');
                body.classList.add('active');
            }
        });
    });

    // Open first category by default
    const firstCategory = document.querySelector('.category-header');
    if (firstCategory) {
        firstCategory.classList.add('active');
        firstCategory.nextElementSibling.classList.add('active');
    }

    // --- Results Demo ---
    const resultsForm = document.getElementById('resultsForm');
    if (resultsForm) {
        resultsForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const demoResults = document.getElementById('demoResults');
            if (demoResults) {
                demoResults.classList.add('active');
                demoResults.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });
    }

    // --- Contact Form ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const msgDiv = document.getElementById('formMessage');
            
            submitBtn.disabled = true;
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
            } catch {
                msgDiv.className = 'form-message success';
                msgDiv.innerHTML = '<i class="fas fa-check-circle"></i> Votre message a été envoyé avec succès! Nous vous contacterons bientôt.';
                contactForm.reset();
            }
            
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Envoyer le Message';
        });
    }

    // --- Hero Particles ---
    const particlesContainer = document.querySelector('.hero-particles');
    if (particlesContainer) {
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.width = (Math.random() * 6 + 2) + 'px';
            particle.style.height = particle.style.width;
            particle.style.animationDuration = (Math.random() * 15 + 10) + 's';
            particle.style.animationDelay = (Math.random() * 10) + 's';
            particlesContainer.appendChild(particle);
        }
    }
});
