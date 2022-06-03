from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
   
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',csrf_exempt(views.processOrder),name='process_order'),
    # path('update_wish/',views.updateWish,name='update_wish'),

]
