from django.urls import path
from .views import (
    ProductListView, ProductDetailView, AddToCartView, 
    CartView, CheckoutView, ShopDashboardView, 
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = 'shop'

urlpatterns = [
    # Public
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    
    # Internal Staff CRUD
    path('staff/', ShopDashboardView.as_view(), name='staff_dashboard'),
    path('staff/product/add/', ProductCreateView.as_view(), name='product_add'),
    path('staff/product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('staff/product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    
    path('index/', ProductListView.as_view(), name='index'), 
]
