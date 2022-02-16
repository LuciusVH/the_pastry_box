let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
  $('#id_default_country').css('color', 'hsla(210, 18%, 72%, 1)');
};
$('#id_default_country').change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css('color', 'hsla(210, 18%, 72%, 1)');
  } else {
    $(this).css('color', '#000');
  }
});