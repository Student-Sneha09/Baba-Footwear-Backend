const toggleBtn = document.getElementById('theme-toggle');
const body = document.body;

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');

  // Also toggle class on footer (add if not present)
  const footer = document.querySelector('footer');
  if (footer) {
    footer.classList.toggle('dark-mode');
  }

  // Optional: Store user preference in localStorage
  const mode = body.classList.contains('dark-mode') ? 'dark' : 'light';
  localStorage.setItem('theme', mode);
});

// Load saved theme on reload
window.addEventListener('DOMContentLoaded', () => {
  const savedMode = localStorage.getItem('theme');
  if (savedMode === 'dark') {
    body.classList.add('dark-mode');

    const footer = document.querySelector('footer');
    if (footer) {
      footer.classList.add('dark-mode');
    }
  }
});

