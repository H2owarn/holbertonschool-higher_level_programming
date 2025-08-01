document.addEventListener('DOMContentLoaded', () => {
  const characterElement = document.getElementById('character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Fetch error:', error);
      characterElement.textContent = 'Failed to load character';
    });
});