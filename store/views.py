from itertools import product
from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import JsonResponse,HttpResponse
import json
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']
        
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)

# def wishlist(request):
#     if request.user.is_authenticated:
#         customer=request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer,complete=False)
#         items=order.orderitem_set.all()
#         cartItems=order.get_cart_items
#         wishItems=order.get_wishlist_items
#     else:
#         items=[]
#         order={'get_cart_total':0,'get_cart_items':0}
#         cartItems=order['get_cart_items']
        
#     product=Product.objects.get(id=order.id)
#     print(product)
#     context={'product':product,'wishItems':wishItems,'cartItems':cartItems}
#     return render(request, 'store/wishlist.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']
        
    context={'items':items,'order': order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']
        
    context={'items':items,'order': order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action:',action)
    print('product:',productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created = Order.objects.update_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.update_or_create(order=order,product=product)
    
    if action=='add':
        orderItem.quantity=(orderItem.quantity +1)
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added",safe=False)
