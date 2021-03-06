from django.urls import path
from .views import index, detail, add_post, edit_post, delete_post, search_post, category, registerUser, loginUser, logoutUser

urlpatterns = [
    path('', index, name="index"),
    path('post/<int:post_id>/', detail, name="detail"),
    path('addpost/', add_post, name="addpost"),
    path('editpost/<int:post_id>/', edit_post, name="editpost"),
    path('deletepost/<int:post_id>/', delete_post, name="deletepost"),
    path('search/', search_post, name="search"),
    path('category/<str:slug>/', category, name="category"),
    path('register/', registerUser, name="register"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
]
