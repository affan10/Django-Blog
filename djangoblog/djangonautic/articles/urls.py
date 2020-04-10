from django.urls import path, re_path
from . import views

# Has the app_name before every URL in urlpatterns
app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article-list'),
    path('create/', views.article_create, name='article-create'),
    path('<slug:slug>/', views.article_detail, name='article-detail'),
    path('update/<int:userid>/', views.article_list_of_author, name='article-list-of-author'),
    path('delete/<int:articleid>', views.article_delete, name='article-delete'),
    path('update/<int:userid>/<int:articleid>/', views.article_update, name='article-update'),
]