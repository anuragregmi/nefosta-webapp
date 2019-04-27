from django.urls import path

from nefosta.views.nefosta import ArticleListView

from .views.nefosta import IndexView

app_name = "nefosta"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("articles/", ArticleListView.as_view(), name="article_list")
]
