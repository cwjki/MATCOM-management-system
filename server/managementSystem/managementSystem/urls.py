from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('thesis-assignment/', include('thesisAssignment.urls')),
    path('teaching-assignment/', include('teachingAssignment.urls'))
]

# path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
