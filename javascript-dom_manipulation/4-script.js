document.addEventListener('DOMContentLoaded', () => {
    const addItem = document.getElementById('add_item');
    addItem.addEventListener('click', () => {
      const ul = document.querySelector('ul.my_list');
      const li = document.createElement('li');
      li.textContent = 'Item';
      ul.appendChild(li);
    });
  });
  