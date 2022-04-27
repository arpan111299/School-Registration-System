from rest_framework.views import APIView
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework.response import Response

# Teacher Views
class TeacherAPI(APIView):
    def get(self,request,id=None,format=None):
        id = id
        if id is not None:
            teacher = Teacher.objects.get(id = id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)

        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many = True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id, fromat=None):
        id = id
        teacher = Teacher.objects.get(id=id)
        serializer= TeacherSerializer(teacher,data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        id = id
        teacher = Teacher.objects.get(id= id)
        teacher.delete()
        return Response({'msg':'Data Deleted Successfully'})