from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('profile',views.profile,name="profile"),
    path('cart/', views.cart_view, name='cart'),
    path('products/', views.product_list, name='product_list'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('order/<int:order_id>/update/', views.update_order_status, name='update_order_status'),
]

