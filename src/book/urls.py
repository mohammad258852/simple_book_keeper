from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('order/<int:order_id>', views.order, name='order'),
    path('new_order', views.new_order, name='new_order'),
    path('order/<int:order_id>/add/<str:book_id>', views.add_book, name='add_book'),
    path('order/<int:order_id>/remove/<str:book_id>', views.remove_book, name='remove_book'),
    path('order/<int:order_id>/finalize', views.finalize, name='remove_book'),
]