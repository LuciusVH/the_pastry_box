var dropdowns = document.querySelectorAll('.navbar-toggler');

$('.navbar-toggler').click(function () {
  let dropdown_id = this.getAttribute('data-bs-target');
  // console.log($('#mobile-navbar').find('.collapse').not(dropdown_id));
  $('#mobile-navbar').find('.collapse').not(dropdown_id).removeClass('show');
});