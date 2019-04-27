from django.urls import path

from .views.nefosta import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="")
]
