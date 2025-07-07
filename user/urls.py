from django.urls import path
from . import views
urlpatterns = [
    path('storekeeper/login/', views.StorekeeperLoginView.as_view(), name='storekeeper-login-view'),
]