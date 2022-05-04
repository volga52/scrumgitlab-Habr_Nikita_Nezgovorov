from django.shortcuts import render
from django.urls import reverse_lazy
# from mainapp.forms import ArticleCreateForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
import random

from mainapp.models import Article, Article


def main(request):
    n = 3
    articles = []
    gen = get_random(n)
    for i in gen:
        articles.append(i)

    content = {
        'articles': articles,
        'categorys': Article.objects.all()[:4],
    }
    return render(request, 'mainapp/index.html', content)


def get_random(n):
    max_id = Article.objects.all().order_by('-pk')[0].pk
    while n >= 0:
        pk = random.randint(1, max_id)
        yield Article.objects.filter(pk=pk).first()
        n -= 1


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'mainapp/article_update.html'
    success_url = reverse_lazy('articles:index')
    fields = '__all__'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'mainapp/article_update.html'
    success_url = reverse_lazy('articles:index')
    fields = '__all__'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')


class ArticleDetailView(DetailView):
    model = Article


class ArticleCategoryView(DetailView):
    model = Article

# def article_create(request):
#     if request.method == 'POST':
#         create_form = ArticleCreateForm(request.POST, request.FILES)
#         if create_form.is_valid():
#             article = create_form.save()
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         create_form = ArticleCreateForm
