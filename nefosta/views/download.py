from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views.generic import ListView

from nefosta.models.download import DownloadCategory, DownloadResource


class DownloadCategoryListView(ListView):
    model = DownloadCategory
    template_name = "nefosta/download_category_list.html"


class DownloadResouceListView(ListView):
    model = DownloadResource
    template_name = "nefosta/download_resource_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            queryset = queryset.filter(category__id=self.category.id)
        except (TypeError, ValueError, ValidationError, ObjectDoesNotExist):
            queryset = queryset.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_categories"] = DownloadCategory.objects.exclude(
            id=self.category.id).order_by('-posted_on').only('id', 'title')[:4]
        context["category"] = self.category
        return context

    @cached_property
    def category(self):
        return get_object_or_404(DownloadCategory, id=self.kwargs.get('cat_id'))
