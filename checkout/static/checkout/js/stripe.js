var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: '#000',
    fontFamily: 'Merriweather, Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};
var card = elements.create('card', {
  style: style
});
card.mount('#payment-element');


// Handle realtime validation errors on the card element
var errorDiv = document.getElementById('card-errors');

card.addEventListener('change', function (event) {
  if (event.error) {
    var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>`;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  setLoading(true);
  card.update({
    'disabled': true
  });
  $('#submit-btn').attr('disabled', true);

  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  // From using {% csrf_token %} in the form
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.city.value),
            country: $.trim(form.country.value),
            state: $.trim(form.county.value),
          }
        }
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.city.value),
          country: $.trim(form.country.value),
          postal_code: $.trim(form.postcode.value),
          state: $.trim(form.county.value),
        }
      },
    }).then(function (result) {
      if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
                  <span class="icon" role="alert">
                  <i class="fas fa-times"></i>
                  </span>
                  <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        setLoading(false);
        card.update({
          'disabled': false
        });
        $('#submit-btn').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function () {
    location.reload();
  })
});


// ------- Stripe UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageText.textContent = "";
  }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit-btn").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit-btn").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}