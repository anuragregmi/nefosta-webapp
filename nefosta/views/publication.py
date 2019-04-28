from django.views.generic import ListView, DetailView


from nefosta.models.publication import Publication


class PublicationListView(ListView):
    model = Publication
    template_name = "nefosta/publication_list.html"
    page_size = 10


class PublicationDetailView(DetailView):
    model = Publication
    template_name = "nefosta/publication_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_publications"] = Publication.objects.exclude(
            id=self.get_object().id).order_by('-posted_on').only('id', 'title')[:4]
        return context
