from django.urls import path
from auth.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
