from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)
from django.views.generic import ListView, DetailView, FormView, UpdateView,  DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import AddToCart, CreateOrderForm
from .models import Medicine, Cart, Order
from django import forms

class MedListView(ListView):
    model = Medicine
    context_object_name = 'med_list'
    template_name = 'medicine/medicine_list.html'

class CartView(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = 'cart_list'
    template_name = 'medicine/cart.html'


class AddToCartView(LoginRequiredMixin, DetailView, FormView):
    model = Medicine
    template_name = 'medicine/addcart.html'
    form_class = AddToCart
    success_url = reverse_lazy('medicine:cart')
    
    def form_valid(self, form):
        # Calls the custom send method
        cl = form.cleaned_data
        ob = self.get_object()
        med = Medicine.objects.get(id=ob.id)
        med_ex = Cart.objects.filter(medicine=ob.id, username=self.request.user.id).exists()
        user_ex = Cart.objects.filter(username=self.request.user.id).exists()
        med_data = Cart.objects.filter(medicine=ob.id).values('medicine_id')
        user_data = Cart.objects.filter(username=self.request.user.id).values('medicine_id')
       #med_id_user = user_data[0]['medicine_id']
        #med_id_med = med_data[0]['medicine_id']
        q = cl['quantity']
        p = 0
       
        if med_ex and user_ex:
            k = list(Cart.objects.filter(username=self.request.user.id, medicine=ob.id).values('c_quantity','total_price'))
            q +=  k[0]['c_quantity']
            p = q * med.price
            Cart.objects.filter(username=self.request.user.id, medicine=ob.id).update(c_quantity = q,total_price=p)
        else:
            Cart.objects.create(medicine=med, 
            c_quantity=cl['quantity'], total_price=cl['quantity']*med.price, username=self.request.user)
        

        return redirect("medicine:cart")



class CartUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cart
    template_name = 'medicine/cart_update.html'
    success_url = reverse_lazy('medicine:cart')
    fields = ('c_quantity',)
    def form_valid(self, form):
        cl = form.cleaned_data
        ob = self.get_object()
        # med = Medicine.objects.get(id=ob.id)
        # cart_ids = Cart.objects.filter(medicine=ob.id).values_list('medicine', flat=True)
        p = int(cl['c_quantity']) * int(ob.medicine.price)
        Cart.objects.filter(id=ob.id).update(
                    c_quantity = cl['c_quantity'],
                    total_price=p
                )
        return redirect("medicine:cart")
    def test_func(self):  
        obj = self.get_object()
        return obj.username == self.request.user


class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cart
    template_name = 'medicine/cart_delete.html'
    success_url = reverse_lazy('medicine:cart')
    def test_func(self):  
        obj = self.get_object()
        return obj.username == self.request.user

# class CartDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Cart
#     template_name = 'medicine/cart_detail.html'
#     def test_func(self):  
#         obj = self.get_object()
#         return obj.username == self.request.user


class OrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'medicine/display_orders.html'
    

class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'medicine/checkout.html'
    success_url = reverse_lazy("medicine:cart")
    form_class = CreateOrderForm
    def form_valid(self, form):  
        # cl = form.cleaned_data
        # cart = Cart.objects.filter(username=self.request.user.id).values('id')
        form.instance.username = self.request.user
        # cc = Cart.objects.filter(username=self.request.user).get(id=cart)
        
        # form.instance.cart = cart[0]['id']
        return super().form_valid(form)

