from django.urls import path

from warehouse.views import ProductListView

urlpatterns = [
    path('dashboard/product/list/', ProductListView.as_view(), name='product-list-view'),
]