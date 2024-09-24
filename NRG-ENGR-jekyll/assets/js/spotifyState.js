let hoverTimeout;

const spotifyIcon = document.getElementById('spotify-icon');
const spotifyBubble = document.getElementById('spotify-bubble');

// Handle hover to show bubble
spotifyIcon.addEventListener('mouseenter', () => {
   spotifyBubble.classList.remove('hidden');
});

// Hide after 5 seconds of no hover
spotifyBubble.addEventListener('mouseleave', () => {
   hoverTimeout = setTimeout(() => {
      spotifyBubble.classList.add('hidden');
   }, 5000);
});

// Keep bubble open if hovered within 5 seconds
spotifyBubble.addEventListener('mouseenter', () => {
   clearTimeout(hoverTimeout);
});