from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import UserViewSet, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", UserViewSet.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
