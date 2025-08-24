// Club Secret Menu JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling and interaction effects
    console.log('Club Secret Menu Loaded');

    // Add click effect to drink items
    const drinkItems = document.querySelectorAll('.drink-item');
    
    drinkItems.forEach(item => {
        item.addEventListener('click', function() {
            // Add a temporary flash effect
            this.style.transform = 'scale(1.02)';
            this.style.transition = 'transform 0.1s ease';
            
            setTimeout(() => {
                this.style.transform = '';
                this.style.transition = 'all 0.3s ease';
            }, 100);
        });
    });

    // Add floating animation to header
    const clubName = document.querySelector('.club-name');
    if (clubName) {
        let floatDirection = 1;
        setInterval(() => {
            clubName.style.transform = `translateY(${Math.sin(Date.now() * 0.001) * 3}px)`;
        }, 16);
    }

    // Add sparkle effect to gold elements
    function createSparkle(element) {
        const sparkle = document.createElement('div');
        sparkle.innerHTML = '✨';
        sparkle.style.position = 'absolute';
        sparkle.style.fontSize = '12px';
        sparkle.style.pointerEvents = 'none';
        sparkle.style.animation = 'sparkle 1s ease-out forwards';
        sparkle.style.left = Math.random() * element.offsetWidth + 'px';
        sparkle.style.top = Math.random() * element.offsetHeight + 'px';
        
        element.style.position = 'relative';
        element.appendChild(sparkle);
        
        setTimeout(() => {
            if (sparkle.parentNode) {
                sparkle.parentNode.removeChild(sparkle);
            }
        }, 1000);
    }

    // Add sparkle animation CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes sparkle {
            0% { opacity: 0; transform: scale(0) rotate(0deg); }
            50% { opacity: 1; transform: scale(1) rotate(180deg); }
            100% { opacity: 0; transform: scale(0) rotate(360deg); }
        }
    `;
    document.head.appendChild(style);

    // Add sparkles to section titles periodically
    const sectionTitles = document.querySelectorAll('.section-title');
    setInterval(() => {
        const randomTitle = sectionTitles[Math.floor(Math.random() * sectionTitles.length)];
        createSparkle(randomTitle);
    }, 3000);

    // Add current time display (optional)
    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString('es-CO', { 
            hour: '2-digit', 
            minute: '2-digit',
            hour12: true 
        });
        
        // You can add a time element if needed
        // document.querySelector('.current-time').textContent = timeString;
    }
    
    updateTime();
    setInterval(updateTime, 60000); // Update every minute
});
