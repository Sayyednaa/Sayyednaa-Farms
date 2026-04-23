from django.urls import path
from .views import (
    HomeView, GalleryView, AboutView, DashboardView, StaffLoginView, StaffLogoutView,
    RegisterView, ProfileView, UserOrdersView, AddressCreateView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', StaffLoginView.as_view(), name='login'),
    path('logout/', StaffLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/orders/', UserOrdersView.as_view(), name='user_orders'),
    path('profile/address/add/', AddressCreateView.as_view(), name='address_add'),
]
