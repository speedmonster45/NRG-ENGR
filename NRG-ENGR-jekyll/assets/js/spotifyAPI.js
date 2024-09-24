async function fetchCurrentSong() {
   const response = await fetch('https://api.spotify.com/v1/me/player/currently-playing', {
      headers: {
         'Authorization': 'Bearer ' + accessToken // You'll need to get an OAuth token from Spotify
      }
   });

   if (response.ok) {
      const data = await response.json();
      document.getElementById('song-title').textContent = data.item.name;
      document.getElementById('artist-name').textContent = data.item.artists[0].name;
      document.getElementById('song-thoughts').textContent = 'This song is awesome!';
   }
}

fetchCurrentSong();