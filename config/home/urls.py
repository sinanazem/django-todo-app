from django.urls import path
from home.views import introduction, todo, detail, delete, create, update




urlpatterns = [
    path("", introduction, name="introduction"),
    path("todo/", todo, name="todo"),
    path("todo/details/<int:todo_id>/", detail, name="details"),
    path("delete/<int:todo_id>", delete, name="delete"),
    path("update/<int:todo_id>", update, name="update"),
    path("create/", create, name="create"),
]