document.addEventListener('DOMContentLoaded', () => {
  const addItemTrigger = document.getElementById('add_item');
  const list = document.querySelector('ul.my_list');

  if (addItemTrigger && list) {
    addItemTrigger.addEventListener('click', () => {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      list.appendChild(newItem);
    });
  }
});