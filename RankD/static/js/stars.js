function generateStarRating(container, rating) {
    const star_size = container.getAttribute('star_size');
    container.innerHTML = ''; // Clear any existing stars

    const maxRating = 5;
    const fullStars = Math.floor(rating / 2);
    const halfStar = rating % 2 !== 0;

    // Create full stars
    for (let i = 0; i < fullStars; i++) {
        const starIcon = document.createElement('span');
        starIcon.classList.add('star', 'full', star_size);
        container.appendChild(starIcon);
    }

    // Create half star if needed
    if (halfStar) {
        const halfStarIcon = document.createElement('span');
        halfStarIcon.classList.add('star', 'half', star_size);
        container.appendChild(halfStarIcon);
    }

    // Create empty stars to complete the 5-star rating
    const remainingStars = maxRating - fullStars - (halfStar ? 1 : 0);
    for (let i = 0; i < remainingStars; i++) {
        const starIcon = document.createElement('span');
        starIcon.classList.add('star', 'empty', star_size);
        container.appendChild(starIcon);
    }
}

const all_containers = document.getElementsByClassName('star_rating');

for (let container of all_containers) {
    const rating = container.getAttribute('rating');
    if (rating) {
        generateStarRating(container, rating);
    }
}

