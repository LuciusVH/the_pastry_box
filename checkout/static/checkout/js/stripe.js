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
  setLoading(true)
  card.update({
    'disabled': true
  });
  $('#submit-btn').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function (result) {
    if (result.error) {
      var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
      $(errorDiv).html(html);
      card.update({
        'disabled': false
      });
      setLoading(false);
      $('#submit-btn').attr('disabled', false);
    } else {
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
        setLoading(false);
      }
    }
  });
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