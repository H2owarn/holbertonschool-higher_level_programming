document.addEventListener('DOMContentLoaded', () => {
  const updateHeaderTrigger = document.getElementById('update_header');
  const header = document.querySelector('header');

  if (updateHeaderTrigger && header) {
    updateHeaderTrigger.addEventListener('click', () => {
      header.textContent = 'New Header!!!';
    });
  }
});