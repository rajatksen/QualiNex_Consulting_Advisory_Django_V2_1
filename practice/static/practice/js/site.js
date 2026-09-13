(function(){
  // Always start the application at the Home page and at scroll position 0.
  // This prevents browser scroll restoration from reopening a long page halfway down.
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (window.location.pathname === '/' || window.location.pathname === '') {
    window.addEventListener('load', function(){ window.scrollTo(0,0); }, {once:true});
  }

  const toggle=document.querySelector('.menu-toggle'), nav=document.querySelector('.mobile-nav');
  if(toggle&&nav){
    toggle.addEventListener('click',()=>{
      const open=toggle.getAttribute('aria-expanded')==='true';
      toggle.setAttribute('aria-expanded',String(!open));
      nav.hidden=open;
    });
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      toggle.setAttribute('aria-expanded','false');
      nav.hidden=true;
    }));
  }

  const section=document.body.dataset.section;
  document.querySelectorAll('.desktop-nav a[data-page]').forEach(a=>{
    if(a.dataset.page===section)a.classList.add('active');
  });
})();
