from django.shortcuts import render

# Create your views here.
from registration.models import Course, Student, Instructor,Enrollment,CourseCoordinator
from registration.serializers import CourseSerializer, StudentSerializer, InstructorSerializer,EnrollmentSerializer,CourseCoordinatorSerializer
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class CourseListCreateApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=["code","name"]
    search_fields=["name"]
    ordering_fields=["name"]

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class CourseUpdateDeleteApiView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class StudentApiViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class InstructorApiViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class EnrollmentApiViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    ordering_fields=["grade"]

class CourseCoordinatorApiViewSet(viewsets.ModelViewSet):
    queryset = CourseCoordinator.objects.all()
    serializer_class = CourseCoordinatorSerializer
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    ordering_fields=["course"]
    search_fields=["course"]


    