from django import forms

QUANTITY_RANGE = [(i,str(i)) for i in range(1,250)]

class AddToCart(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_RANGE, coerce=int)


from .models import Order

class CreateOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('address', 'phone', 'cart')
        # fields('cart').widget = forms.HiddenInput()
        
        # widgets = {'cart': forms.HiddenInput()}
        