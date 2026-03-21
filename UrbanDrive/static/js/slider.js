 let currentIndex = 0;
        const slides = document.querySelectorAll('.slider-wrapper .slider');
        const totalSlides = slides.length;

        function showSlides() {
            currentIndex = (currentIndex + 1) % totalSlides;
            slides.forEach((slide, index) => {
                slide.style.transform = `translateX(-${currentIndex * 100}%)`;
            });
        }

        setInterval(showSlides, 3000);