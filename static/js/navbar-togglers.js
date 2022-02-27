$('.navbar-toggler').click(function () {
  let dropdown_id = this.getAttribute('data-bs-target');
  $('#mobile-navbar').find('.collapse').not(dropdown_id).removeClass('show');
});