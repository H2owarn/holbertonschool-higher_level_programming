document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Fetch error:', error);
      helloElement.textContent = 'Erreur de chargement';
    });
});