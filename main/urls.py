from django.urls import path
from . import views

app_name='main'

urlpatterns =[
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('sign-up',views.sign_up, name='sign_up'),
    path('create-post',views.create_post, name='create_post'),
    path('product',views.product_list, name='product_list'),
    path('product/<slug:category_slug>/',views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>',views.product_detail, name='product_detail')

]