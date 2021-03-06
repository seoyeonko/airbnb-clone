from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"  # room_list.html에서 사용


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room