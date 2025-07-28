document.addEventListener('DOMContentLoaded', () => {
  const redHeaderTrigger = document.getElementById('red_header');
  const header = document.querySelector('header');
  if (redHeaderTrigger && header) {
    redHeaderTrigger.addEventListener('click', () => {
        header.style.color = '#FF0000';
    });
  }
});

