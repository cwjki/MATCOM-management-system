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

router.register(r'thesis-defense', views.ThesisDefenseViewSet,
                basename="thesis-defense")

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('thesis-committee-csv-download/',
         views.ThesisCommitteeCSVDownloadView.as_view()),
    path('thesis-defense-csv-download/',
         views.ThesisDefenseCSVDownloadView.as_view()),
    path('', include(router.urls)),
]
