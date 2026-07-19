"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registration.views import CourseListCreateApiView,CourseUpdateDeleteApiView,StudentApiViewSet,InstructorApiViewSet,EnrollmentApiViewSet,CourseCoordinatorApiViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course/', CourseListCreateApiView.as_view()),
    path('api/course/<int:pk>/', CourseUpdateDeleteApiView.as_view()),
    path('api/student/',StudentApiViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('api/student/<int:pk>/',StudentApiViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        'patch':'partial_update'
    })),
     path('api/Instructor/',InstructorApiViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('api/Instructor/<int:pk>/',InstructorApiViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        'patch':'partial_update'
    })),
     path('api/CourseCoordinator/',CourseCoordinatorApiViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('api/CourseCoordinator/<int:pk>/',CourseCoordinatorApiViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        'patch':'partial_update'
    })),
     path('api/Enrollment/',EnrollmentApiViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
  
]
