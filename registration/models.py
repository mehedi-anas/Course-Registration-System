from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Course(TimeStampedModel):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=20, unique=True)
    credit_hours = models.DecimalField(max_digits=3, decimal_places=1, default=3.0)
    offered_since = models.DateField()

    def __str__(self):
        return self.name


class Instructor(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name="instructors")

    def __str__(self):
        return self.name

class Student(TimeStampedModel):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name
    
class Enrollment(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    semester = models.CharField(max_length=20, blank=True)
    grade = models.DecimalField(
    max_digits=3,
    decimal_places=2,
    null=True,
    blank=True,
    validators=[
        MinValueValidator(0, message="Grade must be 0 or greater"),
        MaxValueValidator(4.0, message="Grade cannot exceed 4.0")
    ]
    )
    enrolled_on = models.DateField(auto_now_add=True)
    class Meta:
        unique_together=("student","grade")

    def __str__(self):
        return f"{self.student.name}_{self.semester}"
    
class CourseCoordinator(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    appointed_on = models.DateField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="coordinator")

    def __str__(self):
        return self.name


