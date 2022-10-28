from django.urls import path, include
from auth.views import MyTokenObtainPairView, RegisterView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


# The API URLs are now determined automatically by the router
router = DefaultRouter()

router.register(r'users', UserViewSet,
                basename="users")

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', include(router.urls))
]
