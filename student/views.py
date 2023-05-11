from django.shortcuts import HttpResponse
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class PathView(ListCreateAPIView):
    serializer_class = PathSerializer
    queryset = Path.objects.all()

class PathDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PathSerializer
    queryset = Path.objects.all()

class StudentView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()