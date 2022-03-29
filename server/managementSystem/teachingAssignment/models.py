import uuid
from django.db import models


# NOMENCLADORES
class Career(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class StudyPlan(models.Model):
    name = models.CharField(max_length=200)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)
    numberOfSemesters = models.SmallIntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class SchoolYear(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    studyPlan = models.ForeignKey(StudyPlan, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.name + ' ' + self.studyPlan.name)


class Department(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class ScientificDegree(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class TeachingCategory(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class ClassType(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class YearPeriod(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


# Entidades
class Professor(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # Relationships
    scientificDegree = models.ForeignKey(
        ScientificDegree, on_delete=models.PROTECT, null=True, blank=True)
    teachingCategory = models.ForeignKey(
        TeachingCategory, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name + self.lastName)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    numberOfHours = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # Relationships
    career = models.ForeignKey(
        Career, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)
    StudyPlan = models.ForeignKey(
        StudyPlan, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class TeachingPlanning(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    numberOfHours = models.PositiveIntegerField()
    numberOfGroups = models.PositiveIntegerField()

    # Relationships
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classType = models.ForeignKey(ClassType, on_delete=models.PROTECT)
    yearPeriod = models.ForeignKey(YearPeriod, on_delete=models.PROTECT)


class TeachingAssigment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    percent = models.IntegerField(default=1)
    group = models.IntegerField()

    # Relationships
    teachingPlanning = models.ForeignKey(
        TeachingPlanning, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
