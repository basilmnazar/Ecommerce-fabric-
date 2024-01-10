from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('blog',views.blog, name='blog'),
    path('products',views.products, name='products'),
    path('contact',views.contact, name='contact'),
    path('login',views.login, name='login'),
    path('register/',views.for_register, name='registerpage'),
    path('login',views.login, name='login'),
    
    ##view products url
    # path('',views.view_product, name='products')
    #cart url
    # path('cart/',views.cart,name='cart')
    path('view_cart/',views.view_cart,name='viewCart'),
    path('addtoCart/<int:product_id>',views.add_to_cart,name='addToCart'),
    path('increament/<int:id>',views.increament,name='increament')
]
