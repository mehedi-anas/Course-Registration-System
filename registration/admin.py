from django.contrib import admin
from registration.models import Course, Instructor, Student, Enrollment, CourseCoordinator

# Register your models here.
class StudentInline(admin.TabularInline):
    model=Student
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "name",
        "credit_hours",
        "offered_since"
    ]
    search_fields=["name"]
    ordering=["name"]
    inlines = [StudentInline]

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "designation",
        
    ]
    search_fields=["name","email"]
    ordering=["name"]
    filter_horizontal=["courses"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "student_id",
        "course"
        
    ]
    search_fields=["name","student_id"]
    list_filter=["course"]
    ordering=["name"]
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "semester",
        "grade"   
        
    ]
    search_fields=["student__name"]
    list_filter=["semester"]
    ordering=["grade"]