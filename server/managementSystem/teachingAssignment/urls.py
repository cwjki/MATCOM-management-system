from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# A PI endpoints
urlpatterns = [
    path('', views.api_root, name="home"),

    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name="snippet-datail"),

    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user-detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
