from django.shortcuts import render,redirect
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from schoolApp.models import *
from schoolApp.forms import UpdateStudentForm,TeacherUpdateStudentForm




class StudentSignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(f'/student_mainbody/{request.user.pk}')
        else:
            return render(request,'student_signup.html')

    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        password2 = request.POST['password2']
        if len(firstname) != 0 and len(lastname) != 0 and len(username) != 0 and len(password1) != 0 and len(
                email) != 0 and len(password2) != 0 and len(phone) != 0:
            if not Student.objects.filter(username=username).exists():
                if password1 == password2:
                    student = Student.objects.create(first_name=firstname, last_name=lastname, username=username,
                                                email=email, phone=phone, age=age,is_student=True)
                    student.set_password(password1)
                    student.save()
                    return redirect('/student_login/')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')



class StudentLogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(f'/student_mainbody/{request.user.pk}')
        else:
            return render(request,'student_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(auth.login(request,student))
        print(username)
        student = Student.objects.get(username=username)
        print(student)
        password_check = check_password(password, student.password)  
        print(password_check)      
        if password_check:
            auth.login(request, student)
            print(auth.login(request, student))
            return redirect(f'/student_mainbody/{student.pk}')
    

class StudentLogout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('StudentLogIn')


class StudentMainBodyView(View):
    def get(self, request,id):
        if request.user.is_authenticated:
            student = Student.objects.get(is_student= True ,id=id)
            print(student,"************")
            if not student.access_token:
                
                print(student)
                context ={
                    "student":student,
                    }
                return render(request,'student_mainbody.html',context)
            else:
                return redirect('StudentAccessCodeSearch')
        else:
            return render(request,'student_login.html')



class StudentAccessCodeSearchView(View):
        def get(self, request):
            student=Student.objects.get(pk=request.user.pk)
            if not student.access_token: 
                searched = request.GET.get('searched')
                student.access_token=searched
                student.save()
                
                class_object = Classs.objects.get(access_code=searched)
                class_object.student_name.add(student)
            else:
                # print(student.access_token)
                class_object = Classs.objects.filter(access_code=student.access_token).values_list('standard',flat=True)
                class_object_one = Classs.objects.filter(access_code=student.access_token).values_list('division',flat=True)
                print(class_object)
                # print(student_name)
                teacher_list=Classs.objects.filter(access_code=student.access_token).values_list('teacher_name__username',flat=True)
                student_list=Classs.objects.filter(access_code=student.access_token).values_list('student_name__username',flat=True)
            context={
                "class_student_list_json":student_list,
                "teacher_list_json":teacher_list,
                "class_object_json":class_object_one,
                "class_list_json":class_object,
            }
            # return JsonResponse(context,safe=False)
            return render(request,'student_details_page.html',context)


class StudentUpdateView(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            form = UpdateStudentForm
            return render(request, 'update_student.html',{'form':form}) 
        else:
            return render(request,'student_login.html')

    def post(self,request,id):
        print(request.POST)
        student = Student.objects.get(pk=id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        student.first_name =first_name
        student.last_name =last_name
        student.email =email
        student.save()
        return redirect(f'/student_mainbody/{id}')


class TeacherUpdateStudentView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            form = TeacherUpdateStudentForm
            return render(request, 'update_student.html',{'form':form}) 
        else:
            return render(request,'teacherlogin.html')

    def post(self,request,pk):
        student=Student.objects.get(pk=pk)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        access_token=request.POST['access_token']
        student.first_name =first_name
        student.last_name =last_name
        student.email =email
        
        
        
        if student.access_token: 
            print("**************************************************************************")
            c = Classs.objects.get(access_code = student.access_token)
            c.student_name.remove(student)

            student.access_token=access_token
            student.save()   
            cls = Classs.objects.get(access_code=access_token)
            cls.student_name.add(student)
            cls.save()
        return redirect('TeacherMainBody')