from django.views.generic import ListView, DetailView


from nefosta.models.event import Event


class EventListView(ListView):
    model = Event
    template_name = "nefosta/event_list.html"
    page_size = 10


class EventDetailView(DetailView):
    model = Event
    template_name = "nefosta/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_events"] = Event.objects.exclude(id=self.get_object().id).order_by(
            '-posted_on').only('title')[:4]
        return context
