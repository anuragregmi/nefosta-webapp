from django.views.generic import TemplateView
from nefosta.models.article import Article
from nefosta.models.event import Event
from nefosta.models.gallery import Photo


class ImageCarouselMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'carousel_images': Photo.objects.filter(show_in_carousel=True)}
        )

        return ctx


class IndexView(ImageCarouselMixin, TemplateView):
    template_name = "nefosta/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'articles': Article.objects.all().order_by('-posted_on')[:3],
            'events': Event.objects.all().order_by('-posted_on')[:3]
        })

        return ctx


class AboutView(ImageCarouselMixin, TemplateView):
    template_name = "nefosta/about_us.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'events': Event.objects.all().order_by('-posted_on')[:5]
        })

        return ctx


class ContactView(TemplateView):
    template_name = "nefosta/contact_us.html"
