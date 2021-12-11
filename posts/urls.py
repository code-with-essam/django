from django.urls import path
from . import views

app_name="posts"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("create/", views.create_article, name="create"),
    path("update/<int:id>/", views.update_view,name="update"),
    path("delete/<int:id>/", views.delete_view, name="delete"),
    path("search/", views.search_view, name="search"),
    path("detail/<int:id>/", views.detail_view, name="detail")
]
