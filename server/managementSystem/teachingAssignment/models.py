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
    owner = models.ForeignKey(
        'auth.User', related_name='careers', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)


class StudyPlan(models.Model):
    name = models.CharField(max_length=50)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)
    numberOfSemesters = models.SmallIntegerField()

    def __str__(self) -> str:
        return str(self.name)


class SchoolYear(models.Model):
    name = models.CharField(max_length=50)

    # Relationship
    studyPlan = models.ForeignKey(StudyPlan, on_delete=models.PROTECT)

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


class YearPeriod(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class Professor(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Relationships
    scientificDegree = models.ForeignKey(
        ScientificDegree, on_delete=models.PROTECT, null=True, blank=True)
    teachingCategory = models.ForeignKey(
        TeachingCategory, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' ' + str(self.lastName)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    numberOfHours = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField()

    # Relationships
    career = models.ForeignKey(
        Career, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)
    studyPlan = models.ForeignKey(
        StudyPlan, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' ' + '[' + str(self.studyPlan) + ']'


class TeachingPlanning(models.Model):
    numberOfHours = models.PositiveIntegerField()
    numberOfGroups = models.PositiveIntegerField()

    # Relationships
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classType = models.ForeignKey(ClassType, on_delete=models.PROTECT)
    yearPeriod = models.ForeignKey(YearPeriod, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '[' + str(self.subject) + '] ' + '[' + str(self.classType) + '] ' + '[' + str(self.yearPeriod) + ']'


class TeachingAssignment(models.Model):
    percent = models.IntegerField(default=1)
    group = models.IntegerField()

    # Relationships
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    teachingPlanning = models.ForeignKey(
        TeachingPlanning, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '[' + str(self.professor) + '] ' + '[' + str(self.teachingPlanning) + ']'


class CarmenTable(models.Model):
    schoolYear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    yearPeriod = models.ForeignKey(YearPeriod, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '[' + str(self.schoolYear) + '] ' + '[' + str(self.yearPeriod) + ']' + '[' + str(self.semester) + ']'
