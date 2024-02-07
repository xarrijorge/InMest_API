from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("1", views.index1, name="index1"),
    path("fil/<int:id>/", views.filter_queries, name="filter_queries"),
    path("queries/", views.QueryView.as_view(),name="query_view")
    # path("filter_queries/", views.filter_queries, name="filter_queries")
]