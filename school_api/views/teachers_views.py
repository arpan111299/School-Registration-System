from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import mixins,generics
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response

# Teacher Views
class TeacherAPI(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = Teacher.objects.filter(is_student=False)
    serializer_class = TeacherSerializer

    def get(self,request,pk):
        return self.retrieve(request)

    def patch(self,request,pk):
        return self.update(request,partial=True)
    
    def delete(self,request,pk):
        return self.destroy(request)

class TeacherListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = Teacher.objects.filter(is_student=False)
    serializer_class = TeacherSerializer
    
    def get(self, request):
        return self.list(request)
 
    def post(self,request):
        return self.create(request)

class AdminRemoveTeacherAPI(generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Teacher.objects.filter(is_student=False)
    serializer_class= SchoolSerializer

    def get(self,request,pk):
        print(pk)
        teacher = Teacher.objects.get(pk=pk)
        teacher.has_school= False
        teacher.delete()
        teacher.save()
        # print(pk + "11111111111111111111111111111111111111111111111111111111111")
        return JsonResponse("teacher removed successfully", safe=False)


    # def get_teacher(self, pk):
    #     try:
    #         teacher = Teacher.objects.get(pk=pk)
    #         return teacher
    #     except Teacher.DoesNotExist:
    #         return False

    # @csrf_exempt
    # def delete(self,request,pk):
    #     if self.get_teacher():
    #         teacher=Teacher.objects.get(pk=pk)
    #         return self.destroy(request)
    #     else:
    #         return JsonResponse("Teacher Not Found")
    


    # def get(self,request,id=None,format=None):
    #     id = id
    #     if id is not None:
    #         teacher = Teacher.objects.get(id = id)
    #         serializer = TeacherSerializer(teacher)
    #         return Response(serializer.data)

    #     teacher = Teacher.objects.filter(is_student = False)
    #     serializer = TeacherSerializer(teacher,many = True)
    #     return Response(serializer.data)

    # @csrf_exempt
    # def post(self,request,format=None):
    #     serializer = TeacherSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def patch(self, request, id, fromat=None):
    #     id = id
    #     teacher = Teacher.objects.get(id=id)
    #     serializer= TeacherSerializer(teacher,data = request.data, partial= True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, id, format=None):
    #     id = id
    #     teacher = Teacher.objects.get(id= id)
    #     teacher.delete()
    #     return Response({'msg':'Data Deleted Successfully'})


class UserLogout(APIView):
    permission_classes = (IsAuthenticated)
    def post(self, request, format=None):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
