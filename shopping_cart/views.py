from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_shopping_cart(request):
    """ View the shopping cart content """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_shopping_cart(request, product_id):
    """ Add product x quantity to the shopping cart """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity != 0:
        if product_id in list(shopping_cart.keys()):
            shopping_cart[product_id] += quantity
            messages.success(request, f'Added {product.name} to your bag')
        else:
            shopping_cart[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)


def adjust_shopping_cart(request, product_id):
    """ Adjust item quantity in the shopping cart """

    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[product_id] = quantity
    else:
        shopping_cart.pop(product_id)

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse(view_shopping_cart))


def remove_from_shopping_cart(request, product_id):
    """ Remove the item from the shopping cart """

    try:
        shopping_cart = request.session.get('shopping_cart', {})
        print(shopping_cart)

        shopping_cart.pop(product_id)

        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
