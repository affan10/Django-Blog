from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleAPIView.as_view(), name='articles-list-and-post-apiurl'),
    path('<int:id>/', views.ArticleAPIView.as_view(), name='get-apiurl'),
    path('<int:id>/update/', views.ArticleAPIView.as_view(), name='update-apiurl'),
    path('<int:id>/delete/', views.ArticleAPIView.as_view(), name='delete-apiurl'),
    path('list/', views.ArticlesPaginationView.as_view(), name='pagination-url'),
]