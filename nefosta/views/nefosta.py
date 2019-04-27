from django.views.generic import TemplateView, ListView

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
    template_name = "nefosta/article_list"
