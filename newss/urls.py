from django.urls import path
from .views import NewsListView, NewsDetailView, NewsUpdateView, NewsDeleteView, NewsCreateView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]