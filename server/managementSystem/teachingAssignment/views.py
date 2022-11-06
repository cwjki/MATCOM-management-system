import os
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import permissions, viewsets, authentication, generics, mixins
from rest_framework import filters, status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Career, CarmenTable, Faculty, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, TimePeriod, TeachingCategory, ScientificDegree, Professor, Subject, Semester, TeachingPlanning
from .serializers import CarmenTableSerializer, FacultySerializer, SubjectDescriptionSerializer, TeachingAssignmentSerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ClassTypeSerializer, TimePeriodSerializer, TeachingCategorySerializer, ScientificDegreeSerializer, ProfessorSerializer, SubjectSerializer, SemesterSerializer, TeachingPlanningSerializer
from .serializers_csv import CareerSerializerCSV
from .permissions import IsOwnerOrReadOnly
from .optimization.optimization import OptimizationModel
from .excels.get_csv import TA_CSV_GENERATOR


class CSVDownloadView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    This view handles the teaching assignments csv file download
    """

    def get(self, request):
        current_path = os.path.dirname(__file__)
        file_dir = os.path.join(
            current_path, 'excels/download/teaching_assignments.csv')

        csv_generator = TA_CSV_GENERATOR(
            department_name='Matemática Aplicada', file_dir=file_dir)
        csv_generator.generate_csv()

        try:
            with open(file_dir, 'r') as f:
                file_data = f.read()

            response = HttpResponse(
                file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Docencia.csv"'

        except IOError:
            response = HttpResponseNotFound('<h1>File not found</h1>')

        return response


class GenerateSolutionTAView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = []

    def get(self, request):
        subject_qs = SubjectDescription.objects.all()
        professor_qs = Professor.objects.all()

        model = OptimizationModel(subject_qs, professor_qs)
        results = model.solve()

        response = Response(data=results)
        return response


class CareerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for careers.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    search_fields = ['name', 'faculty__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CareerCSVViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for careers.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializerCSV
    search_fields = ['name']


class StudyPlanViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for study plans.
    """
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SemesterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for semesters.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingGroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching groups.
    """
    queryset = TeachingGroup.objects.all()
    serializer_class = TeachingGroupSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FacultyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for faculty.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for school years.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    search_fields = ['name', 'faculty__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClassTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for class types.
    """
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimePeriodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for time periods.
    """
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScientificDegreeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for scientific degrees.
    """
    queryset = ScientificDegree.objects.all()
    serializer_class = ScientificDegreeSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching categories.
    """
    queryset = TeachingCategory.objects.all()
    serializer_class = TeachingCategorySerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for professors.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    search_fields = ['name', 'last_name', 'department__name',
                     'scientific_degree__name', 'teaching_category__name']
    filterset_fields = ['department', 'scientific_degree', 'teaching_category']
    ordering_fields = ['name']
    ordering = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    search_fields = ['name']
    filterset_fields = ['department', 'career', 'study_plan', 'semester']
    ordering_fields = ['name']
    ordering = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubjectDescriptionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for subjects descriptions.
    """
    queryset = SubjectDescription.objects.all()
    serializer_class = SubjectDescriptionSerializer
    search_fields = ['subject__name',
                     'class_type__name', 'teaching_group__name', 'time_period__name']
    filterset_fields = ['teaching_group', 'class_type', 'time_period']
    ordering_fields = ['subject__name']
    ordering = ['subject__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def get_groups(self, request, pk=None):
        """
        Return a list with the groups of the subject description.
        """
        try:
            subject_description = SubjectDescription.objects.get(pk=pk)
            groups = subject_description.number_of_groups
            data = [i for i in range(1, groups + 1)]
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        except:
            print('C')
            return Response(status=status.HTTP_404_NOT_FOUND)


class TeachingAssignmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching assignments.
    """
    queryset = TeachingAssignment.objects.all()
    serializer_class = TeachingAssignmentSerializer
    search_fields = ['subject_description__subject__name',
                     'professor__name', 'professor__last_name',
                     'subject_description__class_type__name',
                     'subject_description__teaching_group__name']
    filterset_fields = ['professor']
    # ordering_fields = ['subject_description__subject__name']
    # ordering = ['subject_description__subject__name']

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeachingPlanningViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for teaching planning.
    """
    queryset = TeachingPlanning.objects.all()
    serializer_class = TeachingPlanningSerializer
    # search_fields = ['professor__name', 'subjectDescription__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarmenTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for carmen table.
    """
    queryset = CarmenTable.objects.all()
    serializer_class = CarmenTableSerializer
    search_fields = ['teaching_group__name', 'study_plan__name']
    filterset_fields = ['teaching_group', 'study_plan', 'semester']

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
