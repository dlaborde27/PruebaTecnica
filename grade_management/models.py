from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    guardian = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    TRIMESTERS = [
        (1, 'First Trimester'),
        (2, 'Second Trimester'),
        (3, 'Third Trimester')
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    trimester = models.IntegerField(choices=TRIMESTERS)
    grade = models.FloatField()

    class Meta:
        unique_together = ['student', 'subject', 'trimester']

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.trimester}"
