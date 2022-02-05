// Manage the quantity field, with + & - buttons
// Code snippet taken from https://jsfiddle.net/puJ6G/2457/ & slightly customized

jQuery(document).ready(function () {
  // This button will increment the value
  $('.qtyplus').click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    // Get the field name
    fieldName = $(this).attr('field');
    // Get its current value
    var currentVal = parseInt($(this).siblings('input[name=' + fieldName + ']').val());
    // If is not undefined and it's smaller than 99
    if (!isNaN(currentVal) && currentVal < 99) {
      // Increment
      $(this).siblings('input[name=' + fieldName + ']').val(currentVal + 1);
    } else {
      // Otherwise put a 1 there
      $(this).siblings('input[name=' + fieldName + ']').val(1);
    }
  });
  // This button will decrement the value till 1
  $(".qtyminus").click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    // Get the field name
    fieldName = $(this).attr('field');
    // Get its current value
    var currentVal = parseInt($(this).siblings('input[name=' + fieldName + ']').val());
    // If it isn't undefined and it's greater than 1
    if (!isNaN(currentVal) && currentVal > 1) {
      // Decrement one
      $(this).siblings('input[name=' + fieldName + ']').val(currentVal - 1);
    } else {
      // Otherwise put a 1 there
      $(this).siblings('input[name=' + fieldName + ']').val(1);
    }
  });
});