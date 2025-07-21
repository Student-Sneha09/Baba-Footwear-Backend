// Theme Toggle
  const themeToggle = document.getElementById('theme-toggle');
  themeToggle?.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
  });

  // Search Functionality
  // Search Filter
document.addEventListener("DOMContentLoaded", function () {
  const searchBtn = document.getElementById("search-btn");
  const searchInput = document.getElementById("search-input");

  searchBtn.addEventListener("click", function () {
    const searchTerm = searchInput.value.toLowerCase();
    const products = document.querySelectorAll(".product-card");

    products.forEach((product) => {
      const title = product.querySelector(".product-title").textContent.toLowerCase();
      if (title.includes(searchTerm)) {
        product.style.display = "block";
      } else {
        product.style.display = "none";
      }
    });
  });
});
