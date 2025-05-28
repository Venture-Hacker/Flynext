// Use the 'DOMContentLoaded' event to ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Delay for 1 second before starting the fade-out
    setTimeout(function() {
        const preloader = document.querySelector('.preloader');
        if (preloader) {
            preloader.classList.add('fade-out'); // Add fade-out class
            
            // Wait for the transition to finish before hiding it
            preloader.addEventListener('transitionend', function() {
                preloader.style.display = 'none'; // Hide the preloader after fade-out
            });
        }
    }, 1000); // 1 second delay
});
