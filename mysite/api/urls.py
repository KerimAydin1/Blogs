from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blog/create", views.BlogCreate.as_view(), name="create",),
    path("blog/update/<int:pk>", views.BlogUpdate.as_view(), name="update",),
    path("blog/delete/<int:pk>", views.BlogDestroy.as_view(), name="delete",),
    path("user/", views.UserView.as_view(), name="UserView"),
    path("user/create", views.UserCreate.as_view(), name="CreateUser"),
    path("user/delete/<int:pk>", views.UserDelete.as_view(), name="DeleteUser"),
    path("user/update/<int:pk>", views.UserUpdate.as_view(), name="UpdateUser"),
]   