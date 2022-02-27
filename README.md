# Fourth Milestone Project



Bonjour and welcome! :v:

This is a website created as my fourth and final Milestone Project for the Full Stack Developer Course of [Code Institute](https://codeinstitute.net/), after completing the 4 modules : User Centric Front End Development, Interactive Frontend Development, Backend Development & Full Stack Frameworks With Django. 

You can find the deployed site [here](https://thepastrybox.herokuapp.com/).

> **NOTE:** The links included in this README will not automatically open in a new tab. Press CTRL or Cmd + click on the link to open the target in a new tab.



## Table of Content

1. [UX](https://github.com/LuciusVH/the_pastry_box#ux)
   1. [Structure & Design](https://github.com/LuciusVH/the_pastry_box#structure--design)
   2. [User Stories](https://github.com/LuciusVH/the_pastry_box#user-stories)
2. [Features](https://github.com/LuciusVH/the_pastry_box#features)
   1. [Existing Features](https://github.com/LuciusVH/the_pastry_box#existing-features)
   2. [Features Left to Implement](https://github.com/LuciusVH/the_pastry_box#features-left-to-implement)
3. [Technologies Used](https://github.com/LuciusVH/the_pastry_box#technologies-used)
   1. [Web Technologies](https://github.com/LuciusVH/the_pastry_box#web-technologies)
   2. [Developer tools](https://github.com/LuciusVH/the_pastry_box#web-technologies)
4. [Testing](https://github.com/LuciusVH/the_pastry_box#testing)
5. [Deployment](https://github.com/LuciusVH/the_pastry_box#deployment)
6. [Credits](https://github.com/LuciusVH/the_pastry_box#credits)
   1. [Content](https://github.com/LuciusVH/the_pastry_box#content)
   2. [Media](https://github.com/LuciusVH/the_pastry_box#media)
   3. [Acknowledgements](https://github.com/LuciusVH/the_pastry_box#acknowledgements)




------
------

## UX

Seeing all these "box" concepts and subscription plans popping out everywhere like champagne out of a shaken bottle :champagne: (gotta be Frenchie :fr:!), yes I'm talking about streaming pay-and-view-it-all plans and other box you receive at home containing ingredients and recipes for the week or beauty product for the month... I had the idea to surf on the wave but add it one of my hobby: pastry & baking :cake:

The basic concept is then pretty simple and not so original: for a monthly or annual fee :moneybag:, you'd receive at your chosen address one box every month :package: containing a detailed pastry recipe, the tools and potentially some ingredients to make the recipe. Depending on the month, the recipe and box could be themed, e.g. Valentine's day :heart:, Pink October :ribbon:, Christmas :christmas_tree:... You get the idea. 

Added to this base concept would be a regular online store dedicated to pastry, bakery and chocolate work where you can find and buy most of the things you may need: plenty moulds, kitchen utensils, pastry rings, baking mats, maybe also a few dry ingredients :chocolate_bar: and why not even appliances, like stand-mixers?

Finally, a blog where some amazing recipes would be uploaded for everyone to enjoy the pleasure of making great cakes and other fine treats, without having to spend half your saving account in some fancy pastry stores :money_with_wings: (although some really deserve it, it's just so freaking good! :drooling_face:) 

### 	Structure & Design

The website is structured as a multi-pages site. 

The e-commerce part allows the user to subscribe to the box but also to purchase individual items, while the blog simply lists the sent newsletter, which are primarly recipes.

The primary color is a beautiful and deep yellow (#FFD75E) :yellow_heart: which I chose because I wanted a bright color, related to pastry but still natural. If you think pastry, of course you can find cakes and icing of any possible colors thanks to food colorants but... Unless you are 6yo, food-wise you tend to be more attracted to natural colors like red, yellow or green for example. There is a reason why you don't see much blue or purple on food packaging. Green does not really scream pastry tho, more vegetables! Red is everywhere and a bit overused if you ask me, while on the other hand yellow... Yellow is a joyful color, evoking sunshine and energy, optimism and intellect. These speak to me and I link them to the emotions I feel when I bake and then share the product of my efforts with loved ones. Yellow catches the eye and bring attention, it also goes well with darker colors such as brown(ies!) or black (hello :bee:). I decided to use it with parcimony tho, making the whole website as bright as the sun would probably discourage more than one... So it is used where I need to get the user's attention: the logo, buttons, links and titles. The background of the website is a very pale version of this #FFD75E, dare I say it remembered me of an old recipes book's pages... :book: 

Typography-wise, I chose [Style Script](https://fonts.google.com/specimen/Style+Script?query=style+script) to emphasize my titles and the rest of the content is written with [Merriweather](https://fonts.google.com/specimen/Merriweather?query=merriweather).

On all pages you can find the sticky navbar and the footer. The navbar contains the brand logo, leading back to the home page as it is customary, a search bar allowing users to quickly get where and what they want (searching through the products), a login/register link and the shopping cart. This one indicates the total amount or simply states "Cart" if it is empty. On a second line the actual navigation links: Home, Subscribe, Products, Recipes & Contact Us. 

The footer is divided in three parts: the left part explains who's behind The Pastry Box (TPB) and the values of the company; the 2nd part lists some useful links while the 3rd and last part is itself divided in 3 sections: a newsletter subscription field, the links to TPB's socials accounts and finally a mention of credit cards accepted and payment security 💳🔐

The initial wireframes can be found [here](https://github.com/LuciusVH/the_pastry_box/tree/main/docs/wireframes/). 

### User stories

As a user, I want to...

- be able to register an account 
- log in and out easily
- be able to modify my data
- be able to change my password if I can't remember it
- subscribe to the newsletter
- access recipes
- be able to follow the brand on social medias
- be able to contact the brand

As a shopper, I want to...

- see all products available
- view an item in details
- quickly purchase one item, without having to click 25 times
- see the amount in my shopping cart easily
- find details about the box subscription offer
- be reassured about the security when paying
- access my order history
- be able to select the quantity and potential size of the items I want to buy
- search and find products easily
- get a full final look on my shopping cart before to checkout
- be able to modify my shopping cart easily
- get a confirmation of my order after checkout
- manage my subscription easily

As a store owner, I want to...

- manage products
- send newsletter

View the tested user stories [here](https://github.com/LuciusVH/the_pastry_box#tested-user-stories).




## Features

### Existing Features

- Create a user profile:
  - Register for an account with your email address and a password.
  - To avoid any typo, the email and the password are asked twice, and the email is verified through a link sent to the registered email address. You cannot access the Profile page until you have verified your email.
  - The Profile page stores the user's details and order history.

- Products catalogue
  - Allows to visualize all the products available, search through them, sorting them in different orders.
  - Adds a product to your cart using the "Add to Cart" button and keep shopping or use the "Buy Now!" button to go straight to the Checkout page.
  - A Back to the top button is available on the product catalogue, since the page could get long with plenty products displayed.

- Shopping Cart
  - Stores your product(s) before payment
  - Allows you to adjust the quantity or delete a product before purchasing
  - Displays the subtotal, the delivery fee and the grand total.

- Checkout
  - Allows the user to buy the content of its shopping cart.
  - Redirects the user to the checkout and inform them is something went wrong.
  - If the payment is successful, the user is redirected to the confirmation page, where their order is summarized. A toast notification doubles the confirmation. They also receive an email with the order recap. Finally, this order is added to the user's profile, if they have one.

- Toast notifications
  - Inform the user whenever an action has been successful or not.
  - Display the content of the shopping cart everytime an item is added.

- Subscription
  - Stripe Checkout allows recurring payment, via two different plans: monthly for 35.99€ or annually for 395.00€ (you get one month for free). You need a profile to subscribe, since it grants you management of your subscription afterwards. If you try to Subscribe without being logged in, you will land on the Sign in page.
  - You can then manage your subscription from your Profile page, through Stripe Customer Portal.

- Newsletter
  - The store owner can write and send newsletter to all the mailing list. From the Admin panel, the newsletter can be formatted nicely with HTML with the help of a WYSIWYG editor, from [CKEditor](https://ckeditor.com/). This function is not available from the front end website, as the editor is quite large and was messing up the page when viewed from a tablet or a mobile.
  - Each post is sent via email, using SMTP and Gmail (thepastrybox.ms4@gmail.com) to the whole mailing list. It is also stored and displayed in the Recipe app.
  - The subscription to the mailing list is available to anyone, on any page, from the footer of the website.

- Recipes
  - Since the weekly newsletters are mostly recipes, each post is stored and displayed under the Recipe app.

- Contact
  - A contact page allows anyone to send a message to TPB's team, it will be sent to thepastrybox.ms4@gmail.com. The social links in the footer also allows user and visitors to subscribe to TPB's socials and stay in touch.



### Features Left to Implement

- Pagination on the Product catalogue if it gets too long.
- Login via socials.
- A reward system, like 4 different levels based on the amount spent throught the year, with a gift at each level.
- A review system for at least the Subscription plan, to incitate more engagement. Potentially for each product?
- A video section, accessible from the Profile page if you have subscribed to a plan. Video of recipe step-by-step.



## Technologies Used

### Web technologies

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

### Developer tools

- [Github](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [AWS](https://aws.amazon.com/) 
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Typora](https://typora.io/)
  - **Typora** was used to write this README file & its annexes.
- [Adobe XD](https://www.adobe.com/products/xd.html)
  - **Adobe XD** was used to create the wireframes. 
- [TinyPNG](https://tinypng.com/)
  - **TinyPNG** was used to compress all pictures, in order to reduce the loading time and improve UX. 
- [Favicon.io](https://favicon.io/)
  - **FavIcon** was used to create and implement the favicon. 
- [Caniuse.com](caniuse.com)



## Testing

### HTML Validator ([W3C](https://validator.w3.org/))

The W3C HTML validator being [unavailable](https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/w3c-validator-503.png) at the moment, I'm using [this one](https://www.freeformatter.com/html-validator.html) instead.

- When testing my [products page](https://thepastrybox.herokuapp.com/products/), some of the errors were as below. I honestly have no idea what that means and Google did not provide me much more info. Given the fact that the validator did not provide me any code extract, I chose to leave these errors as they are.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/html-validator-errors.png" alt="error img"/>
    </p>

- When testing product detail page & shopping cart, these errors appear. This snippet has been taken from this [JSFiddle](https://jsfiddle.net/puJ6G/2457/) and the [JS file](https://github.com/LuciusVH/the_pastry_box/blob/main/static/js/input_quantity.js) working with depends on these `field` attributes.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/field_attribute.png" alt="error img"/>
    </p>

- On the checkout page, the spinner inside the submit button is a code snippet taken from Stripe.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/div-inside-button.png" alt="error img"/>
    </p>

- Still the checkout page, there are two duplicate IDs, from email fields: one from the customer detail form, one from the newsletter subscription form in the footer. These IDs are set by crispy form.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/duplicate-id.png" alt="error img"/>
    </p>

### CSS Validator ([W3C](https://jigsaw.w3.org/css-validator/validator.html))

The W3C CSS validator being unavailable at the moment, I'm using [this one](https://cssportal.com/css-validator/) instead.

- `!important` was used to override Bootstrap CSS.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/css-important.png" alt="error img"/>
    </p>

- Use of CSS variables with `:root`

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/css-var.png" alt="error img"/>
    </p>

- From Bootstrap CSS.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/adjoining-classes.png" alt="error img"/>
    </p>

- I don't understand this error. `:root` is not empty...

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/empty-rule.png" alt="error img"/>
    </p>

- From Bootstrap CSS.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/margin-table-cell.png" alt="error img"/>
    </p>

- This is part of the `:root` variable, the `}` comes later.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/rbrace.png" alt="error img"/>
    </p>

- Isn't it possible to add several selectors to a `:not` pseudo-classe? It seems to be working.

  <p align="center">
      <img src="https://github.com/LuciusVH/the_pastry_box/blob/main/docs/readme_files/unexpected-token-comma.png" alt="error img"/>
    </p>



#### Link testing:

- The logo links to the homepage.
- The search bar links to the Product page, with the user's query.
- The My account dropdown links lead to Sign In and Sign Up pages as guest user, to the Profile and Log Out pages as logged in user + Product Management & Newsletter writting pages if logged in as staff.
- The Cart button links to the Shopping Cart page.
- All links from the sub-part of the navbar work, linking respectively to the Homepage, the Subscription page, the Products dropdown exposes all different products categories, the Recipes page which lists the newsletter posts sent and finally the Contact page, allowing the user to send a message to the TPB's team.
- In the footer, the Terms & Conditions and Privacy Policy links are blank, and the Sign In leads to the login page. The three social links leads to their respective socials.
- On the Subscription page, the Subscribe button leads to a Stripe Checkout page and from this page, the return button leads back to the Subscription page. 
- On the Products page, each card product links to the Product detail page of its specific product. The product category links to all products from the same category. If logged in as staff, the Edit link opens the Edit product page, while the Delete link removes the product from the database directly.
- On the Product detail page, the Back link leads you to the previous page. The Full size picture links opens up the picture in a new tab (visible only from desktop view). The Add to Cart button adds the specified product's quantity to the Cart while the Buy Now! button does the same but leads the user straight to the Checkout page.
- On the Recipes page, each post card links to the Recipe detail page, displaying the whole related post.
- On the Profile page, the order pagination links are disabled if you haven't passed any order yet. They activate after 5 orders minimum. If you have passed an order minimum, it is displayed here. The trucated order number takes you to the order details, while each product line is a link to this specific product. If you don't have subscribed to the Box, you see a button leading to the Subscription page. If you do have a subscription, then a link to manage it shows, leading to a Stripe Customer Portal, as well as a Contact link. 



#### Spotted bugs & errors:

- 


#### Tested user stories:

As a user, I want to...

- be able to register an account 

  *Possible through [Sign up](https://thepastrybox.herokuapp.com/accounts/signup/) page.*

- log in and out easily

  *Possible through [Sign in](https://thepastrybox.herokuapp.com/accounts/login/) and [Sign out](https://thepastrybox.herokuapp.com/accounts/logout/) pages, both easily accessible via the My account dropdown in the navbar.*

- be able to modify my data

  *Possible through the [Profile](https://thepastrybox.herokuapp.com/profile/) page.*

- be able to change my password if I can't remember it

  *Possible through the [Forgotten my password](https://thepastrybox.herokuapp.com/accounts/password/reset/) page*, accessible on the Sign in page. 

- subscribe to the newsletter

  *Possible through any page, from the footer.*

- access recipes

  *The recipes are available on the [Recipes](https://thepastrybox.herokuapp.com/newsletter/recipes/) page, each added once the owner sends them via newsletter.*

- be able to follow the brand on social medias

  *The social links are in the footer.*

- be able to contact the brand

  *Possible through the [Contact](https://thepastrybox.herokuapp.com/contact/contact/) page.*

As a shopper, I want to...

- see all products available

  *Possible through the [Products](https://thepastrybox.herokuapp.com/products/) page.*

- view an item in details

  *Possible through the [Product details](https://thepastrybox.herokuapp.com/products/2/) page.*

- quickly purchase one item, without having to click 25 times

  *Possible via the Buy Now! button on each product page.*

- see the amount in my shopping cart easily

  *The Cart button displays the total amount at anytime, if there's anything in the shopping cart.*

- find details about the box subscription offer

  *Details are provided on the [Subscription](https://thepastrybox.herokuapp.com/subscription/) page.*

- be reassured about the security when paying

  *Stripe, known as a secure payment partner, is mentioned in the footer. When subscribing to the Box offer, the payment is done through the Stripe Checkout directly.*

- access my order history

  *Possible on the [Profile](https://thepastrybox.herokuapp.com/profile/) page.*

- be able to select the quantity and potential size of the items I want to buy

  *There are no size to our products, but the quantity is easily adjustable on each [Product detail](https://thepastrybox.herokuapp.com/products/2/) page, as well as in the [Shopping Cart](https://thepastrybox.herokuapp.com/shopping_cart/) page.*

- search and find products easily

  *Possible through the Search function, at the top of the page.*

- get a full final look on my shopping cart before to checkout

  *The [Shopping Cart](https://thepastrybox.herokuapp.com/shopping_cart/) page displays the content of the cart, in detail.*

- be able to modify my shopping cart easily

  *Possible on the [Shopping Cart](https://thepastrybox.herokuapp.com/shopping_cart/) page. Items are easily adjustable in quantity or removed.*

- get a confirmation of my order after checkout

  *After checkout, you land on a confirmation page and you also receive an email with your order's details. Finally, your order is listed on your [Profile](https://thepastrybox.herokuapp.com/profile/) page.*

- manage my subscription easily

  *Your subscription to the Box is easily manageable via a link on your Profile page. It takes you to the Stripe Customer Portal where you can cancel, change your payment or invoicing details, and also view an historic of your payments related to the plan subscription.*

As a store owner, I want to...

- manage products

  *The products can be managed from different part of the website. If you are logged in at staff, you have access to Update / Delete links on each product card and product detail page. You can add a product from the Product Management link in the My account dropdown. All this can also be done from the [admin](https://thepastrybox.herokuapp.com/admin/) panel.*

- send newsletter

  *Newsletter can be sent fron the Newsletter link under My account dropdown, if logged in as staff. However, it might be better to send them from the Admin panel, since a HTML editor will allow you to format them much nicely.* 


## Deployment & cloning

You can find the deployed site [here](https://thepastrybox.herokuapp.com/).

All steps for deployment, cloning, setting up can be found [here](https://github.com/LuciusVH/the_pastry_box/blob/main/docs/deployment_cloning.md).


## Credits

### Content

- Products description have usually be taken from other websites selling the items, sometimes translated when not in English originally. 
- The rest of the content was written by myself.

### Media

- The hero images are both from Unsplash, [landscape](https://unsplash.com/photos/uxCtCB_yL-M) & [portrait](https://unsplash.com/photos/Gx_vsiMRgzk).
- Products images are from diverses websites, themselves selling these products, or sometimes from the brands' website.

### Acknowledgements

- 