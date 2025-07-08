from django.urls import path

from warehouse import views

urlpatterns = [
    path('dashboard/product/list/', views.ProductListView.as_view(), name='product-list-view'),
    path("dashboard/product/create/", views.ProductCreateAndUpdateView.as_view(), name='product-create-view'),
    path("dashboard/product/<int:product_id>/update/", views.ProductCreateAndUpdateView.as_view(), name='product-update-view'),
]