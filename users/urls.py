from rest_framework.routers import DefaultRouter
from users import views

app_name = "users"
router = DefaultRouter()
router.register("", views.UsersViewSet)


urlpatterns = router.urls
