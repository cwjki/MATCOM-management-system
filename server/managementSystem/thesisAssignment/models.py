from django.db import models
from teachingAssignment.models import Professor


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Thesis(models.Model):
    title = models.CharField(max_length=200)
    student = models.CharField(max_length=200)

    # Relationships
    tutor = models.ForeignKey(
        Professor, related_name='cotutor', on_delete=models.CASCADE)
    cotutors = models.ManyToManyField(
        Professor, blank=True, related_name='tutors')
    keywords = models.ManyToManyField(Keyword, related_name='keywords')

    def __str__(self) -> str:
        return str(self.title + ' ' + str(self.student))


class ThesisCommittee(models.Model):
    # Relationships
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    opponent = models.ForeignKey(
        Professor, null=True, blank=True, related_name='opponent', on_delete=models.CASCADE)
    president = models.ForeignKey(
        Professor, null=True, blank=True, related_name='president', on_delete=models.CASCADE)
    secretary = models.ForeignKey(
        Professor, null=True, blank=True, related_name='secretary', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.thesis) + ' ' + str(self.opponent) + ' ' + str(self.secretary)


class ThesisDefense(models.Model):
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    thesis_committee = models.ForeignKey(
        ThesisCommittee, on_delete=models.CASCADE)
    place = models.ForeignKey(
        Place, null=True, blank=True, on_delete=models.CASCADE)

    # Relationships
