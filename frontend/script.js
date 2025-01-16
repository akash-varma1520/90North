window.onload = function () {
  const toggleMenu = document.getElementById('toggle-menu');
  const menuList = document.getElementById('menu-list');

  toggleMenu.addEventListener('click', () => {
    const isHidden = menuList.style.display === 'none';
    menuList.style.display = isHidden ? 'block' : 'none';
    toggleMenu.setAttribute('aria-expanded', isHidden);
  });

  function adjustScale() {
    const width = window.innerWidth;
    let scale = 1;

    if (width >= 992 && width <= 1600) scale = 0.9;
    else if (width >= 700 && width <= 767) scale = 0.8;
    else if (width >= 600 && width <= 700) scale = 0.75;
    else if (width <= 600) scale = 0.5;

    document.body.style.transform = `scale(${scale})`;
    document.body.style.transformOrigin = 'top left';
  }

  window.addEventListener('resize', adjustScale);
  adjustScale();
};
