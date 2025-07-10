from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/invoice/sell/list/", views.SellInvoiceListView.as_view(), name="sell-invoice-list-view"),
    path("dashboard/invoice/purchase/list/", views.PurchaseInvoiceListView.as_view(), name="purchase-invoice-list-view"),
    path("dashboard/credit/list/", views.CreditListView.as_view(), name="credit-list-view"),
    path("dashboard/invoice/detail/<int:invoice_id>/", views.InvoiceDetailView.as_view(), name="invoice-detail-view"),
]