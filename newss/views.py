from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import News
from .forms import UpdateForm

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    success_url = reverse_lazy('news:news_list')
    fields = ('title', 'body', 'thumb')
    template_name = 'news/news_create.html'
    def form_valid(self, form):  
        form.instance.username = self.request.user
        return super().form_valid(form)

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    form_class = UpdateForm
    template_name = 'news/news_update.html'
    success_url = reverse_lazy('news:news_list')
    def test_func(self):  # new
        obj = self.get_object()
        return obj.username == self.request.user


    

class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news:news_list')
    def test_func(self):  
        obj = self.get_object()
        return obj.username == self.request.user
