from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import UserProfile, Address
from shop.models import Order

class HomeView(TemplateView):
    template_name = 'core/home.html'

class GalleryView(TemplateView):
    template_name = 'core/gallery.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    login_url = 'core:login'

class StaffLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('core:dashboard')

class StaffLogoutView(LogoutView):
    next_page = reverse_lazy('core:home')

# Customer Views
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response

class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'core/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'core/user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['address_line1', 'address_line2', 'city', 'state', 'postal_code', 'is_default']
    template_name = 'core/address_form.html'
    success_url = reverse_lazy('core:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
