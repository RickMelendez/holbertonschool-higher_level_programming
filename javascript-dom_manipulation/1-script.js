document.addEventListener('DOMContentLoaded', () => {
    const redHeader = document.getElementById('red_header');
    redHeader.addEventListener('click', () => {
      document.querySelector('header').style.color = '#FF0000';
    });
  });
  