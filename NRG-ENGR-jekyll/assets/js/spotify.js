<script>
    async function fetchCurrentlyPlaying() {
        const authCode = 'YOUR_AUTHORIZATION_CODE';  // Replace with the actual auth code
        const response = await fetch(`/now-playing?auth_code=${authCode}`);
        
        if (response.ok) {
            const data = await response.json();
            if (data && data.item) {
                const songName = data.item.name;
                const artistName = data.item.artists[0].name;
                const progressMs = data.progress_ms;

                document.getElementById('spotify-song').innerHTML = `
                    <p><strong>Song:</strong> ${songName}</p>
                    <p><strong>Artist:</strong> ${artistName}</p>
                    <p><strong>Current Time:</strong> ${(progressMs / 1000).toFixed(2)} seconds</p>
                `;
            } else {
                document.getElementById('spotify-song').innerHTML = "No track is currently playing.";
            }
        } else {
            document.getElementById('spotify-song').innerHTML = "Error fetching currently playing track.";
        }
    }

    // Call the function on page load
    window.onload = fetchCurrentlyPlaying;
</script>