from django.views.generic import ListView
from nefosta.models.gallery import Album, Photo


class AlbumListView(ListView):
    model = Album
    template_name = 'nefosta/album_list.html'
    paginate_by = 10


class AlbumDetailView(ListView):
    model = Photo
    template_name = 'nefosta/album_detail.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(
            album_id=self.kwargs.get('album_id')
        )
