from django.urls import path
from .views import MedListView, AddToCartView, CartView, CartUpdateView, CartDeleteView, OrderView, CreateOrder

app_name = 'medicine'

urlpatterns = [
    path('', MedListView.as_view(), name='medicine_list'),
    path('add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    
    
    path('<int:pk>/edit/', CartUpdateView.as_view(), name='update_cart'),
    path('<int:pk>/delete/', CartDeleteView.as_view(), name='delete_cart'),
    # path('<int:pk>/', CartDetailView.as_view(), name='cart_detail'),
    path('create/', CreateOrder.as_view(), name='checkout'),
    
    path('order/', OrderView.as_view(), name='order'),
]