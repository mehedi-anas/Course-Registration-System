from registration.models import Course, CourseCoordinator, Instructor, Student, Enrollment
from rest_framework import serializers
from registration.validators import validate_semester


class CourseCoordinatorSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(
        source="course.name",
        read_only=True
    )
    class Meta:
        model = CourseCoordinator
        fields = "__all__"

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor  
        fields="__all__"

class EnrollmentSerializer(serializers.ModelSerializer):
    semester = serializers.CharField(validators=[validate_semester])
    enrolled_on = serializers.DateField(read_only=True)

    class Meta:
        model = Enrollment
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    students=StudentSerializer(
        many=True,
        read_only=True
    )
    instructors=InstructorSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model=Course 
        fields="__all__"

    def validate_name(self,value):
        if Course.objects.filter(
            name__iexact=value
        ).exists():
            raise serializers.ValidationError(
                "Course name already exists"
            )