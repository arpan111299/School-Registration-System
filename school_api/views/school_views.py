from rest_framework.views import APIView
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Teacher Views
class SchoolAPI(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    def get(self,request,pk):
        return self.retrieve(request)

    def patch(self,request,pk):
        return self.update(request, partial=True)
    
    def delete(self,request,pk):
        return self.destroy(request)

class SchoolListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def post(self,request):
        return self.create(request)
    
    def get(self, request):
        return self.list(request)


    # def get(self,request,id=None,format=None):
    #     id = id
    #     if id is not None:
    #         school = School.objects.get(id = id)
    #         serializer = SchoolSerializer(school)
    #         return Response(serializer.data)

    #     school = School.objects.all()
    #     serializer = SchoolSerializer(school,many = True)
    #     return Response(serializer.data)


    # def post(self,request,format=None):
    #     serializer = SchoolSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def patch(self, request, id, fromat=None):
    #     id = id
    #     school = School.objects.get(id=id)
    #     serializer= TeacherSerializer(school,data = request.data, partial= True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, id, format=None):
    #     id = id
    #     school = School.objects.get(id= id)
    #     school.delete()
    #     return Response({'msg':'Data Deleted Successfully'})