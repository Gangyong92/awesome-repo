from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomSerializer


class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer