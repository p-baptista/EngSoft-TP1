document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById("search_form");
    const searchButton = document.getElementById("search_button");
    const searchInput = document.getElementById("search_bar");
    const searchPopup = document.getElementById("search_popup");

    searchButton.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Get the search query from the input field
        const searchQuery = searchInput.value;

        // Update the URL with the search query
        const newUrl = window.location.origin + window.location.pathname + "?searched=" + encodeURIComponent(searchQuery);
        window.history.pushState({ path: newUrl }, '', newUrl);

        // Display the search suggestions popup
        searchPopup.style.display = "block";
    });

    // Hide the search suggestions popup when clicking outside of it
    document.addEventListener("click", function(event) {
        if (!searchForm.contains(event.target)) {
            searchPopup.style.display = "none";
        }
    });
});

