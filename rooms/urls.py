from django.urls import path
from rooms import views

app_name = "rooms"

urlpatterns = [
    path("list/", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
]
