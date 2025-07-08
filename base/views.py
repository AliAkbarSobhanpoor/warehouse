from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class StoreKeeperViLoginRequiredMixin(LoginRequiredMixin):
    login_url = "storekeeper-login-view"