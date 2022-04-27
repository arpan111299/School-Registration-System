from rest_framework.views import APIView
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework.response import Response

# Student Views
class StudentAPI(APIView):
    def get(self,request,id=None,format=None):
        id = id
        if id is not None:
            student = Student.objects.get(id = id,is_student = True)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        student = Student.objects.filter(is_student=True)
        # print(student)
        serializer = StudentSerializer(student,many = True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id, fromat=None):
        id = id
        student = Student.objects.get(id=id)
        serializer= StudentSerializer(student,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        id = id
        student = Student.objects.get(id= id)
        student.delete()
        return Response({'msg':'Data Deleted Successfully'})