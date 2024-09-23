document.addEventListener("DOMContentLoaded", function() {
    console.log("Page is loaded and ready!");
    
    const header = document.querySelector('header');
    
    header.addEventListener('click', function() {
        alert("Header clicked!");
    });
});
