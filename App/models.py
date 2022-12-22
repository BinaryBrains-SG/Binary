from django.db import models

# Create your models here.
class Instructor(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    pswd=models.CharField(max_length=20 )
    is_live=models.BooleanField(default=False)
    img=models.ImageField(upload_to='Instructor/',default=None)
    # subscribers=[models.ForeignKey()]
    def __str__(self) -> str:
        return self.name
    
    def login(self,mail,pwd):
        var=Instructor.objects.get(mail)
        return True if(var.pswd==pwd) else False
            
    pass

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='Courses/')
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    # subscribers=models
    def __str__(self) -> str:
        return self.name

class Doubt(models.Model):
    id=models.AutoField(primary_key=True)
    question=models.TextField(default=None)
    answers=models.TextField(default=None)

class Video(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.TextField(default=None)
    img=models.ImageField(default=None,upload_to='videos/')
    url=models.URLField(default=None)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(default=None,unique=True)
    pswd=models.CharField(max_length=20)
    img=models.ImageField(default=None,upload_to='Students/')
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    Courses=models.ManyToManyField(Course)
    levels=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    def login(self,mail,pwd):
        var=staticmethod.objects.get(mail)
        return True if(var.pswd==pwd) else False
