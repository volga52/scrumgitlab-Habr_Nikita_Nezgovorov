from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('create/', mainapp.ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', mainapp.ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', mainapp.ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/', mainapp.ArticleDetailView.as_view(), name='detail', ),
    path('category/<int:pk>/', mainapp.ArticleCategoryView.as_view(), name='category')
]
