// Switch the data-plan attr of the submit button depending on the selected plan
$('input[name="plan_subscription"').change(function () {
  let submitBtn = document.querySelector("#plans-submit-btn");
  switch ($(this).val()) {
    case 'price_1KTNtjKBwtRGPDpB0CyfyR7R':
      submitBtn.dataset.plan = 'price_1KTNtjKBwtRGPDpB0CyfyR7R';
      break;
    case 'price_1KTNuDKBwtRGPDpB6TBNWtG4':
      submitBtn.dataset.plan = 'price_1KTNuDKBwtRGPDpB6TBNWtG4';
      break;
    default:
      submitBtn.dataset.plan = 'price_1KTNtjKBwtRGPDpB0CyfyR7R';
  }
})


// Get Stripe publishable key
fetch('/subscription/config/')
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);


    // Event handler
    let submitBtn = document.querySelector("#plans-submit-btn");
    if (submitBtn !== null) {
      submitBtn.addEventListener("click", (e) => {
        e.preventDefault();
        let chosenPlan = submitBtn.dataset.plan;
        // Get Checkout Session ID depending on the selected plan
        fetch(`create-checkout-session/${chosenPlan}/`, {
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json'
            }
          })
          .then((result) => {
            return result.json();
          })
          .then((data) => {
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({
              sessionId: data.sessionId
            })
          })
          .catch(error => console.log(error))
      });
    }
  })
  .catch(error => console.log(error));