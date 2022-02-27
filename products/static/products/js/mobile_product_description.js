// PRODUCT DESCRIPTION ACCORDION ON MOBILE
$(document).ready(() => {
  // Target the mobiles & tablets
  if (window.innerWidth < 1200) {
    $('#product-description-accordion').hide();
    $('#product-description-accordion-toggler').click((e) => {
      let toggler = e.target;
      let target = toggler.getAttribute('data-target');

      if ($(target).is(':hidden')) {
        $(toggler).addClass('open');
        $(target).slideDown('fast');
        // Switch the + icon to a - when the related content is displayed
        if ($(toggler).hasClass('open')) {
          $(toggler).children('.fa-caret-down').fadeOut(150, () => {
            $(toggler).children('.fa-caret-up').fadeIn(150);
          });
        }
      } else {
        $(target).slideUp('fast');
        $(toggler).removeClass('open');
        // Switch the - icon to a + when the related content is hidden
        $(toggler).children('.fa-caret-up').fadeOut(150, () => {
          $(toggler).children('.fa-caret-down').fadeIn(150);
        });
      }
    });
  } else {
    $('.footer-block-item-content').show();
  }
});