from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('notes/', views.get_notes, name="notes"),
    path('notes/create/', views.create_note, name='create-note'),
    path('notes/<str:pk>/update/', views.update_note, name="update-note"),
    path('notes/<str:pk>/delete/', views.delete_note, name="delete-note"),
    path('notes/<str:pk>/', views.get_note, name="note"),

    path('snippets/', views.snippet_list, name="snippets"),
    path('snippets/<int:pk>', views.snippet_detail, name="snippet"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
