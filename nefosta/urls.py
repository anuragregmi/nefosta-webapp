from django.urls import path

from .views.nefosta import AboutView
from .views.events import EventListView, EventDetailView
from .views.article import ArticleDetailView, ArticleListView
from .views.publication import PublicationDetailView, PublicationListView
from .views.nefosta import IndexView

app_name = "nefosta"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),

    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(),
         name="article_detail"),


    path("events/", EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", EventDetailView.as_view(),
         name="event_detail"),

    path("publications/", PublicationListView.as_view(), name="publication_list"),
    path("publications/<int:pk>/", PublicationDetailView.as_view(),
         name="publication_detail"),
]
