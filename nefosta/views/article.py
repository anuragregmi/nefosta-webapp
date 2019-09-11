from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from nefosta.models.article import Article


class ArticleListView(ListView):
    model = Article
    template_name = "nefosta/article_list.html"
    paginate_by = 9


class ArticleDetailView(DetailView):
    model = Article
    template_name = "nefosta/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_articles"] = Article.objects.exclude(id=self.get_object().id).order_by(
            '-posted_on').only('id', 'title')[:4]
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'photo']
    template_name = "utils/basic_form.html"
    success_url = reverse_lazy('nefosta:article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["col_size"] = "col-md-6 col-sm-12"
        context["submit_text"] = "Submit Article"
        return context
