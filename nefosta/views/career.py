from django.views.generic import ListView, DetailView

from nefosta.models.career import Career


class CareerListView(ListView):
    model = Career
    template_name = "nefosta/career_list.html"
    page_size = 10


class CareerDetailView(DetailView):
    model = Career
    template_name = "nefosta/career_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_careers"] = Career.objects.exclude(id=self.get_object().id).order_by(
            '-posted_on').only('id', 'heading')[:4]
        return context
