$('.signinToSignup').click(() => {
  $('.form-signin').css('left', '-100vw');
  $('.form-signup').css('left', '0');
  $('.signin-up-container').css('height', '27.3rem');
})

$('.signupToSignin').click(() => {
  $('.form-signin').css('left', '0');
  $('.form-signup').css('left', '100vw');
  $('.signin-up-container').css('height', '22rem');
})