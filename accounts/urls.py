from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),

    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage,  name='login'),
    path('logout/',views.logoutUser,  name='logout'),

    path('user/',views.userPage,  name='user-page'),
    path('account/',views.accountSettings,  name='account'),

    path('products/',views.products,name='products'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    
    path('create_order/<str:pk>/' ,views.createOrder, name='create_order'),
    path('update_order/<str:pk>/' ,views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/' ,views.deleteOrder, name='delete_order'),
]