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

router.register(r'time-periods', views.TimePeriodViewSet,
                basename="time-periods")

router.register(r'teaching-categories', views.TeachingCategoryViewSet,
                basename="teaching-categories")

router.register(r'scientific-degrees', views.ScientificDegreeViewSet,
                basename="scientific-degrees")

router.register(r'study-plans', views.StudyPlanViewSet,
                basename="study-plans")

router.register(r'teaching-groups', views.TeachingGroupViewSet,
                basename="teaching-groups")

router.register(r'professors', views.ProfessorViewSet,
                basename="professors")

router.register(r'subjects', views.SubjectViewSet,
                basename="subjects")

router.register(r'subject-descriptions', views.SubjectDescriptionViewSet,
                basename="subject-descriptions")

router.register(r'teaching-assignments', views.TeachingAssignmentViewSet,
                basename="teaching-assignments")

router.register(r'carmen-table', views.CarmenTableViewSet,
                basename="carmen-table")

router.register(r'semesters', views.SemesterViewSet,
                basename="semesters")

router.register(r'students', views.StudentViewSet,
                basename="students")

router.register(r'thesis', views.ThesisViewSet,
                basename="thesis")


router.register(r'thesis-committee', views.ThesisCommitteeViewSet,
                basename="thesis-committe")

# router.register(r'snippets', views.SnippetViewSet,
#                 basename="snippets")

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
