from django.views.generic import TemplateView, ListView, DetailView

from nefosta.models.article import Article


class IndexView(TemplateView):
    template_name = "nefosta/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'articles': Article.objects.all().order_by('-posted_on')[:3]
        })

        return ctx


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
