from django.views.generic import ListView, DetailView


from nefosta.models.article import Article


class ArticleListView(ListView):
    model = Article
    template_name = "nefosta/article_list.html"
    page_size = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = "nefosta/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_articles"] = Article.objects.exclude(id=self.get_object().id).order_by(
            '-posted_on').only('title')[:4]
        return context
