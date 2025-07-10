from django.urls import path
from . import views


urlpatterns = [
    path('storekeeper/login/', views.StorekeeperLoginView.as_view(), name='storekeeper-login-view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard-view'),
    path('dashboard/user/list', views.UserListView.as_view(), name='user-list-view'),
    path('dashboard/customer/list', views.CustomerListView.as_view(), name='customer-list-view'),
]