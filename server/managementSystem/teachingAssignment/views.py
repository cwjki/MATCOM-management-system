from rest_framework import permissions, viewsets
from rest_framework import filters
from django.contrib.auth.models import User

from .models import Career, StudyPlan, TeachingGroup, Department, ClassType, TimePeriod, TeachingCategory, ScientificDegree, Professor, Subject, SubjectDescription, TeachingAssignment, Semester, CarmenTable
from .serializers import UserSerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ClassTypeSerializer, TimePeriodSerializer, TeachingCategorySerializer, ScientificDegreeSerializer, ProfessorSerializer, SubjectSerializer, SubjectDescriptionSerializer, TeachingAssignmentSerializer, SemesterSerializer, CarmenTableSerializer
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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudyPlanViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for study plans.
    """
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SemesterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for semesters.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingGroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching groups.
    """
    queryset = TeachingGroup.objects.all()
    serializer_class = TeachingGroupSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for school years.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClassTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for class types.
    """
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimePeriodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for time periods.
    """
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScientificDegreeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for scientific degrees.
    """
    queryset = ScientificDegree.objects.all()
    serializer_class = ScientificDegreeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching categories.
    """
    queryset = TeachingCategory.objects.all()
    serializer_class = TeachingCategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for professors.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'lastName']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectDescriptionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects descriptions.
    """
    queryset = SubjectDescription.objects.all()
    serializer_class = SubjectDescriptionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingAssignmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching assignments.
    """
    queryset = TeachingAssignment.objects.all()
    serializer_class = TeachingAssignmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarmenTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for carmen table.
    """
    queryset = CarmenTable.objects.all()
    serializer_class = CarmenTableSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
