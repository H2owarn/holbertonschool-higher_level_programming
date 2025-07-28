document.addEventListener('DOMContentLoaded', () => {
  const toggleHeaderTrigger = document.getElementById('toggle_header');
  const header = document.querySelector('header');

  if (toggleHeaderTrigger && header) {
    toggleHeaderTrigger.addEventListener('click', () => {
      if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
      } else {
        header.classList.replace('green', 'red');
      }
    });
  }
});