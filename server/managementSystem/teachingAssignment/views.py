from rest_framework import permissions, viewsets, authentication
from rest_framework import filters
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from .models import Career, CarmenTable, Faculty, Student, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, Thesis, ThesisCommittee, TimePeriod, TeachingCategory, ScientificDegree, Professor, Subject, Semester, TeachingPlanning
from .serializers import CarmenTableSerializer, FacultySerializer, StudentSerializer, SubjectDescriptionSerializer, TeachingAssignmentSerializer, ThesisCommitteeSerializer, ThesisSerializer, UserSerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ClassTypeSerializer, TimePeriodSerializer, TeachingCategorySerializer, ScientificDegreeSerializer, ProfessorSerializer, SubjectSerializer, SemesterSerializer, TeachingPlanningSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SnippetViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions for snippets.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


class CareerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for careers.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class StudyPlanViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for study plans.
    """
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SemesterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for semesters.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingGroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching groups.
    """
    queryset = TeachingGroup.objects.all()
    serializer_class = TeachingGroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FacultyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for faculty.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'career__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for school years.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'career__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClassTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for class types.
    """
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimePeriodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for time periods.
    """
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScientificDegreeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for scientific degrees.
    """
    queryset = ScientificDegree.objects.all()
    serializer_class = ScientificDegreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching categories.
    """
    queryset = TeachingCategory.objects.all()
    serializer_class = TeachingCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for professors.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'last_name', 'department__name',
                     'scientific_degree__name', 'teaching_category__name']
    filter_backends = [filters.SearchFilter]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']
    # search_fields = ['name', 'department__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectDescriptionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects descriptions.
    """
    queryset = SubjectDescription.objects.all()
    serializer_class = SubjectDescriptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject__department', 'subject__study_plan']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingAssignmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching assignments.
    """
    queryset = TeachingAssignment.objects.all()
    serializer_class = TeachingAssignmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject_description__subject__department__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingPlanningViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching planning.
    """
    queryset = TeachingPlanning.objects.all()
    serializer_class = TeachingPlanningSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['professor__name', 'subjectDescription__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarmenTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for carmen table.
    """
    queryset = CarmenTable.objects.all()
    serializer_class = CarmenTableSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['teachingGroup__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for students table.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThesisViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for thesis table.
    """
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tutor__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThesisCommitteeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for thesis committee table.
    """
    queryset = ThesisCommittee.objects.all()
    serializer_class = ThesisCommitteeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
