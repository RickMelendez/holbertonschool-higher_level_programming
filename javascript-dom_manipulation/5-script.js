document.addEventListener('DOMContentLoaded', () => {
    const updateHeader = document.getElementById('update_header');
    updateHeader.addEventListener('click', () => {
      const header = document.querySelector('header');
      header.textContent = 'New Header!!!';
    });
  });
  