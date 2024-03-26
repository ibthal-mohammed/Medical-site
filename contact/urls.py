from django.urls import path
from .views import ContactView, SuccessView, FailedView
app_name = 'contact'


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
    path('failed/', FailedView.as_view(), name='failed'),
]