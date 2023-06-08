from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="Profile") #On_...Different Approaches
    first_Name=models.CharField(max_length=50,null=True,blank=True)
    middle_Name=models.CharField(max_length=50,null=True,blank=True)
    last_Name=models.CharField(max_length=50,null=True,blank=True)
    country=CountryField(null=True,blank=True)
    location=models.CharField(max_length=50,null=True,blank=True,verbose_name='City')
    resume=models.FileField(upload_to='resumes',null=True,blank=True)
    profile_Photo=models.FileField(upload_to="profile_Photo",null=True,blank=True)
    passing_year=models.IntegerField(blank=True)
    CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

    looking_for=models.CharField (choices=CHOICES,default="Full Time",null=True,max_length=30)
    experience=models.IntegerField(null=True,blank=True,verbose_name="Experience In Years")
     
    # SlugField <-Think
    def __str__(self):
        return self.user.username

class Skill(models.Model):
    skills=models.CharField(max_length=50,unique=True)

class userSkill(models.Model):
    user_skills=models.ForeignKey(User,related_name="user_skills",on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class Applied Jobs...
# class Saved Jobs...
# Think about Validators
# Different cases of blank and null
# File,FilePath ,FileField, FieldFile
