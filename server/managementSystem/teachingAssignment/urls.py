from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teachingAssignment import views


# Create a router and register our viewsets with it
router = DefaultRouter()

router.register(r'users', views.UserViewSet,
                basename="users")

router.register(r'careers', views.CareerViewSet,
                basename="careers")

router.register(r'departments', views.DepartmentViewSet,
                basename="departments")

router.register(r'class-types', views.ClassTypeViewSet,
                basename="class-types")

router.register(r'year-periods', views.YearPeriodViewSet,
                basename="year-periods")

router.register(r'teaching-categories', views.TeachingCategoryViewSet,
                basename="teaching-categories")

router.register(r'scientific-degrees', views.ScientificDegreeViewSet,
                basename="scientific-degrees")

router.register(r'study-plans', views.StudyPlanViewSet,
                basename="study-plans")

router.register(r'school-years', views.SchoolYearViewSet,
                basename="school-years")

router.register(r'professors', views.ProfessorViewSet,
                basename="professors")

router.register(r'snippets', views.SnippetViewSet,
                basename="snippets")

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
