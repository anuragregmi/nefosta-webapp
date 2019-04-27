from django.views.generic import TemplateView

from nefosta.models.article import Article
from nefosta.models.event import Event


class IndexView(TemplateView):
    template_name = "nefosta/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'articles': Article.objects.all().order_by('-posted_on')[:3],
            'events': Event.objects.all().order_by('-posted_on')[:3]
        })

        return ctx


class AboutView(TemplateView):
    template_name = "nefosta/about_us.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'events': Event.objects.all().order_by('-posted_on')[:5]
        })

        return ctx
