from django.urls import path

from djapp.views import ThemeDetailView, ThemesListView, index

urlpatterns = [
    # path("", index),

    path("", ThemesListView.as_view(), name="themes_list"),
    path("detail/<int:theme_id>/", ThemeDetailView.as_view(), name="theme-detail"),
]