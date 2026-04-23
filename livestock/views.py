from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Livestock, Category, Breed

class LivestockIndexView(LoginRequiredMixin, ListView):
    model = Livestock
    template_name = 'livestock/index.html'
    context_object_name = 'animals'
    login_url = 'core:login'

class LivestockCreateView(LoginRequiredMixin, CreateView):
    model = Livestock
    fields = ['breed', 'identifier', 'date_of_birth', 'status', 'weight', 'notes', 'image']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('livestock:index')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add New Animal"
        return context

class LivestockUpdateView(LoginRequiredMixin, UpdateView):
    model = Livestock
    fields = ['breed', 'identifier', 'date_of_birth', 'status', 'weight', 'notes', 'image']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('livestock:index')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Edit Animal: {self.object.identifier}"
        return context

class LivestockDeleteView(LoginRequiredMixin, DeleteView):
    model = Livestock
    template_name = 'staff/confirm_delete.html'
    success_url = reverse_lazy('livestock:index')
    login_url = 'core:login'
