from django.views.generic import ListView, DetailView, View, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem
from django.contrib import messages

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_active=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart = request.session.get('cart', {})
        
        product_id = str(pk)
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1
            
        request.session['cart'] = cart
        messages.success(request, f"{product.name} added to cart.")
        return redirect('shop:cart')

class UpdateCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        product_id = str(pk)
        action = request.POST.get('action')
        
        if product_id in cart:
            if action == 'increment':
                cart[product_id] += 1
            elif action == 'decrement' and cart[product_id] > 1:
                cart[product_id] -= 1
        
        request.session['cart'] = cart
        return redirect('shop:cart')

class RemoveFromCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        product_id = str(pk)
        
        if product_id in cart:
            del cart[product_id]
            messages.info(request, "Item removed from cart.")
            
        request.session['cart'] = cart
        return redirect('shop:cart')

class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        cart_items = []
        total = 0
        
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            item_total = product.price * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
            
        context['cart_items'] = cart_items
        context['total'] = total
        return context

class CheckoutView(View):
    def get(self, request):
        return render(request, 'shop/checkout.html')

    def post(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect('shop:product_list')
            
        # Simplistic order creation for this demo
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            customer_name=name,
            customer_email=email,
            customer_phone=phone,
            total_amount=0 # Will update below
        )
        
        total = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            item_total = product.price * quantity
            total += item_total
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_purchase=product.price
            )
            # Update stock
            product.stock -= quantity
            product.save()
            
        order.total_amount = total
        order.save()
        
        # Clear cart
        request.session['cart'] = {}
        
        return render(request, 'shop/order_complete.html', {'order': order})

# Staff CRUD for Shop
class ShopDashboardView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'shop/staff_dashboard.html'
    context_object_name = 'products'
    login_url = 'core:login'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'name', 'description', 'price', 'stock', 'image', 'is_active']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('shop:staff_dashboard')
    login_url = 'core:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add New Product"
        return context

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['category', 'name', 'description', 'price', 'stock', 'image', 'is_active']
    template_name = 'staff/form.html'
    success_url = reverse_lazy('shop:staff_dashboard')
    login_url = 'core:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit Product"
        return context

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'staff/confirm_delete.html'
    success_url = reverse_lazy('shop:staff_dashboard')
    login_url = 'core:login'
