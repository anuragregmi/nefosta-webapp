from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import Http404
from django.views.generic import DetailView, UpdateView
from nefosta.models.article import Article

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ("first_name", "last_name", "username", "email",
              "introduction", "profile_picture", "phone_number")
    template_name = "utils/basic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["col_size"] = "col-sm-6"
        return context

    def get_success_url(self):
        return reverse('nefosta:user_detail', args=[self.get_object().id])
