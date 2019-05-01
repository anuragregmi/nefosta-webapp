from django.urls import path
from nefosta.views.download import (DownloadCategoryListView,
                                    DownloadResouceListView)
from nefosta.views.gallery import AlbumDetailView, AlbumListView
from nefosta.views.link import LinkCategoryDetailView
from nefosta.views.users import UserDetailView

from .views.article import ArticleDetailView, ArticleListView
from .views.career import CareerDetailView, CareerListView
from .views.events import EventDetailView, EventListView
from .views.nefosta import AboutView, ContactView, IndexView
from .views.publication import PublicationDetailView, PublicationListView

app_name = "nefosta"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),

    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(),
         name="article_detail"),


    path("events/", EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", EventDetailView.as_view(),
         name="event_detail"),

    path("publications/", PublicationListView.as_view(), name="publication_list"),
    path("publications/<int:pk>/", PublicationDetailView.as_view(),
         name="publication_detail"),

    path("links/<int:cat_id>/", LinkCategoryDetailView.as_view(),
         name="link_category_detail"),

    path("careers/", CareerListView.as_view(), name="career_list"),
    path("careers/<int:pk>/", CareerDetailView.as_view(),
         name="career_detail"),

    path("downloads/", DownloadCategoryListView.as_view(),
         name="download_category_list"),
    path("downloads/<int:cat_id>/", DownloadResouceListView.as_view(),
         name="download_resource_list"),

    path("gallery/", AlbumListView.as_view(),
         name="album_list"),
    path("gallery/<int:album_id>/", AlbumDetailView.as_view(),
         name="album_detail"),


    path("accounts/<int:pk>/", UserDetailView.as_view(), name="user_detail")
]
