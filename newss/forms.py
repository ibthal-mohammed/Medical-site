from django.forms import ModelForm
from .models import News



class UpdateForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'body', 'thumb')