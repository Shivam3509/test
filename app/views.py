from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Employe
from .serializers import EmployeSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListView(ListAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    pagination_class = CustomPageNumberPagination

class CreateView(CreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class RetrieveView(RetrieveAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class UpdateView(UpdateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    lookup_field = 'pk'

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Updated successfully"})

    #     else:
    #         return Response({"message": "failed", "details": serializer.errors})

class DestroyView(DestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class DestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "GET":

            return {}
        return super().get_permissions()