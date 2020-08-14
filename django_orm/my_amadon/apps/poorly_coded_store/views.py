from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    selected_product = Product.objects.get(id=request.POST['product_id'])
    price_from_form = selected_product.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/thank_you')

def render_checkout(request):
    last_order = Order.objects.last()
    orders_info = orders_total()
    context = {
        'last_total': last_order.total_price,
        'orders_total': orders_info[0],
        'num_orders': orders_info[1]
    }
    return render(request, "store/checkout.html", context)

def orders_total():
    orders = Order.objects.all()
    total = 0
    num_orders = 0
    for order in orders:
        total += order.total_price
        num_orders += 1
    return [total, num_orders]