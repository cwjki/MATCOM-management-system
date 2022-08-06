from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    # Relationship
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)


class Career(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    # Relationship
    # owner = models.ForeignKey(
    #     'auth.User', related_name='careers', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)


class StudyPlan(models.Model):
    name = models.CharField(max_length=50)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)
    number_of_semesters = models.SmallIntegerField()

    def __str__(self) -> str:
        return str(self.name)


class TeachingGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Department(models.Model):
    name = models.CharField(max_length=100)

    # Relationship
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    

    def __str__(self) -> str:
        return str(self.name)


class ScientificDegree(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class TeachingCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class ClassType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class Semester(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class TimePeriod(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class Professor(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Relationships
    scientific_degree = models.ForeignKey(
        ScientificDegree, on_delete=models.PROTECT, null=True, blank=True)
    teaching_category = models.ForeignKey(
        TeachingCategory, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' ' + str(self.last_name)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    number_of_hours = models.PositiveIntegerField()
    # semester = models.PositiveSmallIntegerField()

    # Relationships
    career = models.ForeignKey(
        Career, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)
    study_plan = models.ForeignKey(
        StudyPlan, on_delete=models.PROTECT, null=True, blank=True)
    semester = models.ForeignKey(
        Semester, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' ' + '[' + str(self.career) + ']' + ' ' + '[' + str(self.study_plan) + ']'


class CarmenTable(models.Model):
    teaching_group = models.ForeignKey(TeachingGroup, on_delete=models.CASCADE)
    time_period = models.ForeignKey(TimePeriod, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '[' + str(self.teaching_group) + '] ' + '[' + str(self.study_plan) + '] ' + '[' + str(self.time_period) + ']' + '[' + str(self.semester) + ']'


class SubjectDescription(models.Model):
    number_of_hours = models.PositiveIntegerField()
    number_of_groups = models.PositiveIntegerField()

    # Relationships
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_type = models.ForeignKey(ClassType, on_delete=models.PROTECT)
    time_period = models.ForeignKey(TimePeriod, on_delete=models.PROTECT)
    scholar_year = models.ForeignKey(CarmenTable, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '[' + str(self.subject) + '] ' + '[' + str(self.class_type) + '] ' + '[' + str(self.time_period) + ']'


class TeachingAssignment(models.Model):
    percent = models.IntegerField(default=1)
    group = models.IntegerField()

    # Relationships
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject_description = models.ForeignKey(
        SubjectDescription, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '[' + str(self.professor) + '] ' + '[' + str(self.subject_description) + ']' + '[Grupo ' + str(self.group) + ']'


# ---------- Thesis Committee ----------


class Student(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name) + ' ' + str(self.last_name)


class Thesis(models.Model):
    title = models.CharField(max_length=200)

    # Relationships
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(
        Professor, related_name='tutor', on_delete=models.CASCADE)
    cotutor = models.ForeignKey(
        Professor, related_name='cotutor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title + ' ' + str(self.student))


class ThesisCommittee(models.Model):
    date = models.DateField(null=True, blank=True)

    # Relationships
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    opponent = models.ForeignKey(
        Professor, related_name='opponent', on_delete=models.CASCADE)
    secretary = models.ForeignKey(
        Professor, related_name='secretary', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.thesis) + ' ' + str(self.opponent) + ' ' + str(self.secretary)
