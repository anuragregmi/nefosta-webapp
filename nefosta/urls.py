from django.urls import path

from nefosta.views.nefosta import AboutView

from .views.article import ArticleDetailView, ArticleListView
from .views.nefosta import IndexView

app_name = "nefosta"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),

    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("about/", AboutView.as_view(), name="about"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(),
         name="article_detail"),
]
