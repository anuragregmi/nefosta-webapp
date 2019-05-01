from django.contrib.auth import get_user_model
from django.http import Http404
from django.views.generic import DetailView
from nefosta.models.article import Article

User = get_user_model()


class UserDetailView(DetailView):
    model = User
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.get_object():
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter(author=self.get_object())
        return context
