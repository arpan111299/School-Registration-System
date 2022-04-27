from rest_framework.views import APIView
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework.response import Response

# Teacher Views
class SchoolAPI(APIView):
    def get(self,request,id=None,format=None):
        id = id
        if id is not None:
            school = School.objects.get(id = id)
            serializer = SchoolSerializer(school)
            return Response(serializer.data)

        school = School.objects.all()
        serializer = SchoolSerializer(school,many = True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id, fromat=None):
        id = id
        school = School.objects.get(id=id)
        serializer= TeacherSerializer(school,data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        id = id
        school = School.objects.get(id= id)
        school.delete()
        return Response({'msg':'Data Deleted Successfully'})