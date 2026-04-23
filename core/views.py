from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, Address, ContactMessage
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages_list'] = ContactMessage.objects.all()
        context['orders_list'] = Order.objects.all().order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:home')
            
        action = request.POST.get('action')
        message_id = request.POST.get('message_id')
        
        if action == 'mark_read':
            ContactMessage.objects.filter(id=message_id).update(is_read=True)
            messages.success(request, "Message marked as read.")
        elif action == 'delete':
            ContactMessage.objects.filter(id=message_id).delete()
            messages.success(request, "Message deleted successfully.")
        elif action == 'update_status':
            order_id = request.POST.get('order_id')
            new_status = request.POST.get('status')
            Order.objects.filter(id=order_id).update(status=new_status)
            messages.success(request, f"Order #{order_id} status updated to {new_status}.")
            
        return redirect('core:dashboard')

class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully! We will get back to you soon.")
        else:
            messages.error(request, "There was an error in your submission. Please try again.")
            
        return redirect('core:contact')

class PrivacyView(TemplateView):
    template_name = 'core/privacy.html'

class TermsView(TemplateView):
    template_name = 'core/terms.html'

class ShippingView(TemplateView):
    template_name = 'core/shipping.html'

from django.contrib.auth import login

class StaffLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)

class StaffLogoutView(LogoutView):
    next_page = reverse_lazy('core:home')

# Customer Views
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Create profile
        UserProfile.objects.create(user=self.object)
        # Auto-login after registration
        login(self.request, self.object)
        messages.success(self.request, f"Welcome to Sayyednaa Farms, {self.object.username}! Your account has been created successfully.")
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field.capitalize()}: {error}")
        return super().form_invalid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'
    login_url = 'core:login'

class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'core/user_orders.html'
    context_object_name = 'orders'
    login_url = 'core:login'

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

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)
