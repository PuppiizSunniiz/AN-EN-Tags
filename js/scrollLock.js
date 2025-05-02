(function () {
    let scrollY = 0;

    function lockScroll() {
        scrollY = window.scrollY;
        const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
        Object.assign(document.body.style, {
            position: 'fixed',
            top: `-${scrollY}px`,
            left: '0',
            right: '0',
            width: '100%',
            overflow: 'hidden',
            paddingRight: `${scrollbarWidth}px`,
            touchAction: 'none',
        });
    }

    function unlockScroll() {
        Object.assign(document.body.style, {
            position: '',
            top: '',
            left: '',
            right: '',
            width: '',
            overflow: '',
            paddingRight: '',
            touchAction: '',
        });
        window.scrollTo(0, scrollY);
    }

    // MutationObserver to watch for modal-open class on <body>
    const observer = new MutationObserver(function (mutations) {
        mutations.forEach(mutation => {
            if (mutation.attributeName === 'class') {
                const bodyHasModalOpen = document.body.classList.contains('modal-open');
                if (bodyHasModalOpen) {
                    lockScroll();
                } else {
                    unlockScroll();
                }
            }
        });
    });

    // Start observing class changes on <body>
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['class'],
    });

})();
