from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import *
from schoolApp.models import School
from schoolApp.forms import AddSchoolForm

class CreateSchoolView(View):
    def get(self,request):
        if request.user.is_authenticated:
            if not request.user.has_school:
                form = AddSchoolForm
                return render(request, 'schoolform.html',{'form':form})
            else :
                return HttpResponse("Admin Already has a School")
        else:
             return redirect("TeacherLogIn")

    def post(self, request):
        school_name = request.POST['school_name']
        address = request.POST['address']
        school_phone = request.POST['school_phone']
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        if not request.user.has_school:
            school = School.objects.create(school_name=school_name, address=address, school_phone=school_phone,
                                        admin_id=request.user
                                    )
            request.user.has_school = True
            request.user.save()
            school.save()
            
            school.teacher_id.add(request.user)
        return redirect('TeacherMainBody')