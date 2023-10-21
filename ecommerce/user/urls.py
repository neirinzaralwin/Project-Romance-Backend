from django.urls import path
from .views import UserCreate, UserLogin, UserInfoFromToken, UserListView

app_name = "users"

urlpatterns = [
    path("register/", UserCreate.as_view(), name="create_user"),
    path("login/", UserLogin.as_view(), name="login"),
    path("info/", UserInfoFromToken.as_view(), name="user_info"),
    path("list/", UserListView.as_view(), name="user_list"),
]