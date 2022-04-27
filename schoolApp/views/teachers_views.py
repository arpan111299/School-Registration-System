from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from schoolApp.models import *

# Create your views here.
class IndexView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponse("Please Logout First")
        else:
            return render(request,'index.html')
    # def get(self, request):
    #     if request.user.is_authenticated:
    #         school = School.objects.all()
    #         context = {
    #             "schools":school,
    #         }
    #         return render(request, 'teacher_mainbody.html', context)
    #     else:
    #         return redirect("TeacherLogIn")



class TeacherSignUpView(View):

    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            if request.user.is_student:
                return HttpResponse("You are not the correct user to access this page.")
            elif request.user.has_school:
                return redirect(f'/teacher_school_detail/{request.user.id}')   
            else:
                return redirect('TeacherMainBody')   
        else:
            return render(request,"teacher_signup.html") 
        # return render(request, 'teacher_signup.html')


            # return render(request, 'index.html')
    # return redirect('login')

    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        phone = request.POST['phone']
        email = request.POST['email']
        password2 = request.POST['password2']
        if len(firstname) != 0 and len(lastname) != 0 and len(username) != 0 and len(password1) != 0 and len(
                email) != 0 and len(password2) != 0 and len(phone) != 0:
            if not Teacher.objects.filter(username=username).exists():
                if password1 == password2:
                    teacher = Teacher.objects.create(first_name=firstname, last_name=lastname, username=username,
                                                email=email, phone=phone)
                    teacher.set_password(password1)
                    teacher.save()
                    return redirect('/teacherlogin/')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')


class TeacherLogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_student:
                print(request.user.is_student)
                return HttpResponse("You are not the correct user to access this page.")    
            else:
                return render(request, 'teacher_mainbody.html')
        else:
            return render(request,"teacherlogin.html")
        
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        teacher = Teacher.objects.get(username=username)
        print(teacher.password)
        password_check = check_password(password, teacher.password)
        print(password_check)
        if password_check:
            auth.login(request, teacher)
        if request.user.has_school:
            print("Hello>>>>>>>>>>>>>")
            return redirect(f'/teacher_school_detail/{request.user.id}')
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return redirect('TeacherMainBody')
        # return render(request, 'teacher_mainbody.html')



class TeacherMainBodyView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_student:
                return HttpResponse("You are not the correct user to access this page.")
            else:
                school = School.objects.all()
                context = {
                    "schools":school,
                }
                print(request.user.username)
                return render(request, 'teacher_mainbody.html', context)
        else:
            return redirect("TeacherLogIn")


class TeacherSchoolDetailedView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            if request.user.is_student:
                return HttpResponse("You are not the correct user to access this page.")
            else:
                # teacher = request.user.teacher_info.first()
                school = School.objects.get(id=id)
                class_name = Classs.objects.filter(id = id)
                print(school)
                print(class_name)
                context = {
                    # "teacher":teacher,
                    "school":school,
                    "class":class_name,
                }
                return render(request, 'teacher_school_detail.html',context)
        else:
            return redirect("TeacherLogIn")


# class TeacherSchoolCreateView(CreateView):
#     model = School
#     template_name ="schoolform.html"
#     success_url = "/teacher_mainbody"
#     fields = '__all__'



class TeacherLogout(View):
    def get(self, request):
        auth.logout(request)
        return render(request,'teacherlogin.html')


class AdminRemoveTeacherView(View):
    def get(self,request,username):
        teacher = Teacher.objects.get(username=username)
        teacher.has_school= False
        teacher.delete()
        teacher.save()
        print(username + "11111111111111111111111111111111111111111111111111111111111")
        school = School.objects.all()
        context= {
            "teacher":teacher,
            "school": school
        }
        
        return redirect("/teacher_mainbody",context)


class TeacherAddToExistingSchoolView(View):
    def get(self,request,id):
        school = School.objects.get(id=id)
        class_detail = Classs.objects.all()
        teacher = Teacher.objects.get(id=request.user.id)
        teacher.has_school= True
        school.teacher_id.add(teacher)

        school.save()
        teacher.save()
        print(request.user.id)
        print(teacher)
        print(class_detail)
        print(school)

        context= {
            "school":school,
            "teacher":teacher,
            "class_detail":class_detail,
        }

        return redirect(f"/teacher_school_detail/{id}",context)


class TeacherAddToExistingClassView(View):
    def get(self,request,access_code):
        # school = School.objects.get(id=id)
        class_detail = Classs.objects.get(access_code=access_code)
        teacher = Teacher.objects.get(id=request.user.id)
        class_detail.teacher_name.add(teacher)


        # teacher.save()
        print(request.user.id)
        print(teacher)
        print(class_detail)
        class_detail.save()

        context= {
            "teacher":teacher,
            # "school":school,
            "class_detail":class_detail,
        }

        return redirect("/teacher_mainbody",context)