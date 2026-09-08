document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-links');
    const dropdowns = document.querySelectorAll('.nav-dropdown');

    const updateNavbar = () => navbar?.classList.toggle('scrolled', window.scrollY > 20);
    updateNavbar();
    window.addEventListener('scroll', updateNavbar, { passive: true });

    const closeMenu = () => {
        menu?.classList.remove('open');
        dropdowns.forEach((dropdown) => dropdown.removeAttribute('open'));
        document.body.classList.remove('menu-open');
        toggle?.setAttribute('aria-expanded', 'false');
        if (toggle) toggle.textContent = 'Menu';
    };

    toggle?.addEventListener('click', () => {
        const willOpen = !menu?.classList.contains('open');
        menu?.classList.toggle('open', willOpen);
        document.body.classList.toggle('menu-open', willOpen);
        toggle.setAttribute('aria-expanded', String(willOpen));
        toggle.textContent = willOpen ? 'Close' : 'Menu';
    });

    menu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
    document.addEventListener('click', (event) => {
        if (!(event.target instanceof Element) || event.target.closest('.nav-dropdown')) return;
        dropdowns.forEach((dropdown) => dropdown.removeAttribute('open'));
    });
    window.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') closeMenu();
    });

    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
        const revealTargets = document.querySelectorAll('.section-heading, .app-directory-card, .studio-grid, .services-intro, .service-grid article, .product-section-heading, .product-feature-grid article, .rings-grid, .analysis-copy, .analysis-phone, .product-privacy-grid, .ateyet-pantry-grid, .ateyet-library-grid');
        revealTargets.forEach((element) => element.classList.add('reveal'));
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        revealTargets.forEach((element) => observer.observe(element));
    }
});
