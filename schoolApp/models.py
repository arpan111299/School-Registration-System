from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.

class TeacherManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have a valid email address.")

        if not kwargs.get("username"):
            raise ValueError("Users must have a valid username.")

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get("username")
        )

        # account.set_username(username)
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account



class Teacher(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=40,default='')
    is_student = models.BooleanField(default=False)
    has_school = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    objects = TeacherManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    @property
    def is_authenticated(self):
        return True



class Student(Teacher):
    age = models.IntegerField(blank=True)
    access_token = models.CharField(max_length=10, null=True,blank=True)


class Classs(models.Model):
    standard = models.IntegerField(blank= True)
    division = models.CharField(max_length=10)
    access_code = models.CharField(max_length=10, unique=True, blank=True)
    student_name = models.ManyToManyField(Student,related_name="student_class")
    teacher_name = models.ManyToManyField(Teacher, related_name="teacher_class")

    def __str__(self):
        return self.access_code
    
    class Meta:
        verbose_name_plural= "Classes"


class School(models.Model):
    school_name = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=100)
    school_phone = models.CharField(max_length=15, blank=True)
    teacher_id = models.ManyToManyField(Teacher,related_name='teacher_info')
    admin_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="admin_info",unique=True)
    class_field = models.ManyToManyField(Classs)

    def __str__(self):
        return self.school_name




@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created= False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender= Student)
def create_auth_token_student(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)