from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("feed/", views.feed, name="feed"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="create_post"),
    path("signup/", views.signup, name="signup"),
    path("search/", views.search, name="search"),
    path("profile/", views.my_profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("users/", views.user_list, name="users"),
    path("users/<str:username>/", views.user_profile, name="user_profile"),
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),

]
