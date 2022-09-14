from django.urls import path, include
from rest_framework.routers import DefaultRouter
from thesisAssignment import views

# Create a router and register our viewsets with it
router = DefaultRouter()

router.register(r'students', views.StudentViewSet,
                basename="students")

router.register(r'thesis', views.ThesisViewSet,
                basename="thesis")

router.register(r'thesis-committee', views.ThesisCommitteeViewSet,
                basename="thesis-committe")


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('thesis/', include(router.urls)),
]
