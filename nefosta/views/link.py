from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views.generic import ListView

from nefosta.models.link import Link, LinkCategory, FoodTechnologyCollege


class LinkCategoryDetailView(ListView):
    model = Link
    template_name = "nefosta/link_detail.html"
    page_size = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            queryset = queryset.filter(category__id=self.category.id)
        except (TypeError, ValueError, ValidationError, ObjectDoesNotExist):
            queryset = queryset.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_categories"] = LinkCategory.objects.exclude(
            id=self.category.id).order_by('-posted_on').only('id', 'title')[:4]
        context["category"] = self.category
        return context

    @cached_property
    def category(self):
        return get_object_or_404(LinkCategory, id=self.kwargs.get('cat_id'))


class FoodTechnologyCollegeView(ListView):
    model = FoodTechnologyCollege
    template_name = "nefosta/college_list.html"
    paze_size = 10
