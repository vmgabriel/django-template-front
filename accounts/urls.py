"""Accounts Session of User"""

# Libraries
from django.urls import path

# Views
from . import views


app_name = "accounts"
urlpatterns = [
    path(
        "users/",
        views.ListProfileView.as_view(),
        name="users"
    ),

    path(
        "users/new",
        views.SignUpView.as_view(),
        name="profile-new"
    ),

    path(
        "users/<str:username>/",
        views.ShowProfileView.as_view(),
        name="profile-username"
    ),

    path(
        "users/<str:username>/block/",
        views.block_user,
        name="profile-username-block"
    ),
    path(
        "users/<str:username>/unblock/",
        views.unlock_user,
        name="profile-username-unblock"
    ),
    path(
        "users/<str:username>/delete/",
        views.delete_user,
        name="profile-username-delete"
    ),

    path(
        "me/edit",
        views.UpdateProfileView.as_view(),
        name="profile-user-edit"
    ),

    path(
        "me/",
        views.show_profile,
        name="profile-user",
    ),
]
