document.addEventListener('DOMContentLoaded', () => {
  const movieList = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      data.results.forEach(film => {
        const listItem = document.createElement('li');
        listItem.textContent = film.title;
        movieList.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Fetch error:', error);
      const errorItem = document.createElement('li');
      errorItem.textContent = 'Failed to load movie titles';
      movieList.appendChild(errorItem);
    });
});