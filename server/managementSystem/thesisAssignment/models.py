from django.db import models

from teachingAssignment.models import Professor

# Create your models here.


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
