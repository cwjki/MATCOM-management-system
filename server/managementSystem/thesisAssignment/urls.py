from django.urls import path, include
from rest_framework.routers import DefaultRouter
from thesisAssignment import views

# Create a router and register our viewsets with it
router = DefaultRouter()

router.register(r'places', views.PlaceViewSet,
                basename="places")

router.register(r'keywords', views.KeywordViewSet,
                basename="keywords")

router.register(r'thesis', views.ThesisViewSet,
                basename="thesis")

router.register(r'thesis-committees', views.ThesisCommitteeViewSet,
                basename="thesis-committes")


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('csv-download/', views.CSVDownloadView.as_view()),
    path('', include(router.urls)),
]
