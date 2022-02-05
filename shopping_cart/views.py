from django.shortcuts import render, redirect

# Create your views here.


def view_shopping_cart(request):
    """ View the shopping cart content """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_shopping_cart(request, product_sku):
    """ Add product x quantity to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if product_sku in list(shopping_cart.keys()):
        shopping_cart[product_sku] += quantity
    else:
        shopping_cart[product_sku] = quantity

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)
