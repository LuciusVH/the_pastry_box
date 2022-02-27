// FOOTER ACCORDION ON MOBILE
$(document).ready(() => {
  // Target the mobiles
  if (window.innerWidth < 576) {
    $('.footer-block-item-content').hide();
    $('.footer-block-item-title').click((e) => {
      let toggler = e.target;
      let target = toggler.getAttribute('data-target');

      if ($(target).is(':hidden')) {
        $(toggler).addClass('open');
        $(target).slideDown('fast');
        // Switch the + icon to a - when the related content is displayed
        if ($(toggler).hasClass('open')) {
          $(toggler).children('.fa-plus').fadeOut(150, () => {
            $(toggler).children('.fa-minus').fadeIn(150);
          });
        }
      } else {
        $(target).slideUp('fast');
        $(toggler).removeClass('open');
        // Switch the - icon to a + when the related content is hidden
        $(toggler).children('.fa-minus').fadeOut(150, () => {
          $(toggler).children('.fa-plus').fadeIn(150);
        });
      }
    });
  } else {
    $('.footer-block-item-content').show();
  }
});