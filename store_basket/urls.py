from django.urls import path
from . import views

app_name = 'store_basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('basket_add/', views.basket_add, name='basket_add'),
    path('basket_delete', views.basket_delete, name='basket_delete'),
    path('basket_update', views.basket_update, name='basket_update')

]