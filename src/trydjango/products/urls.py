from django.urls import path
from .views import (
    product_create_view,
    product_delete_view,
    product_detail_view,
    product_list_view,
    dynamic_lookup_view,
)

urlpatterns = [
    path('create/', product_create_view),
    path('', product_detail_view),
    path('<int:my_id>', dynamic_lookup_view, name='product-review'),
    path('<int:hellid>/delete', product_delete_view, name='product-delete'),
    path('list', product_list_view, name='product-list'),
]