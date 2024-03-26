from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm



class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("contact:success")
    template_name = 'contact/contact.html'
    
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'contact/success.html'

class FailedView(TemplateView):
    template_name = 'contact/failed.html'

# class SubEmail(FormView):
#     form_class = SubForm
#     success_url = reverse_lazy("pages:home")
#     template_name = 'pages/home.html'
    
#     def form_valid(self, form):
#         # Calls the custom send method
#         form.send()
#         return super().form_valid(form)