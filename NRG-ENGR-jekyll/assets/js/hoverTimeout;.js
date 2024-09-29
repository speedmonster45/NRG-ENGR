let hoverTimeout;

const spotifyIcon = document.getElementById('spotify-icon');
const spotifyBubble = document.getElementById('spotify-bubble');

// Show bubble on hover
spotifyIcon.addEventListener('mouseenter', () => {
    spotifyBubble.classList.remove('hidden');
    fetchCurrentSong(); // Fetch song data when user hovers
});

// Hide bubble after 5 seconds when hover ends
spotifyBubble.addEventListener('mouseleave', () => {
    hoverTimeout = setTimeout(() => {
        spotifyBubble.classList.add('hidden');
    }, 5000);
});

// Keep the bubble open if re-hovered within 5 seconds
spotifyBubble.addEventListener('mouseenter', () => {
    clearTimeout(hoverTimeout);
});

// Function to fetch the currently playing song from Spotify API
async function fetchCurrentSong() {
    const accessToken = 'YOUR_ACCESS_TOKEN';  // Replace with actual OAuth token from Spotify

    try {
        const response = await fetch('https://api.spotify.com/v1/me/player/currently-playing', {
            headers: {
                'Authorization': 'Bearer ' + accessToken
            }
        });

        if (response.ok) {
            const data = await response.json();
            if (data && data.item) {
                // Update song information in the widget
                document.getElementById('song-title').textContent = data.item.name;
                document.getElementById('artist-name').textContent = data.item.artists[0].name;
                document.getElementById('song-thoughts').textContent = 'This song is awesome!';
            } else {
                document.getElementById('song-title').textContent = "No track is currently playing.";
                document.getElementById('artist-name').textContent = "";
                document.getElementById('song-thoughts').textContent = "";
            }
        } else {
            throw new Error('Failed to fetch song data from Spotify.');
        }
    } catch (error) {
        console.error(error);
        document.getElementById('song-title').textContent = "Error fetching song.";
    }
}

// Fetch the currently playing song when the page loads
window.onload = fetchCurrentSong;