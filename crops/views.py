from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Plantation, CropType, Variety

class CropsIndexView(LoginRequiredMixin, ListView):
    model = Plantation
    template_name = 'crops/index.html'
    context_object_name = 'plantations'
    login_url = 'core:login'

class CropCreateView(LoginRequiredMixin, CreateView):
    model = Plantation
    fields = ['variety', 'location', 'planting_date', 'number_of_plants', 'expected_harvest_date', 'status']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('crops:index')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add New Plantation"
        return context

class CropUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantation
    fields = ['variety', 'location', 'planting_date', 'number_of_plants', 'expected_harvest_date', 'status']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('crops:index')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Edit Plantation: {self.object.location}"
        return context

class CropDeleteView(LoginRequiredMixin, DeleteView):
    model = Plantation
    template_name = 'staff/confirm_delete.html'
    success_url = reverse_lazy('crops:index')
    login_url = 'core:login'
