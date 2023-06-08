from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Profile,Skill,userSkill
from .forms import ProfileUpdateForm,SkillUpdateForm
# from django import form
from django.contrib.auth import get_user_model



# Create your views here.
@login_required()
def my_profile(request):
    you=request.user
    profile= Profile.objects.filter(user=you).first()
    skills=userSkill.objects.filter(user_skills=you)
    if request.method== 'POST':
        form=SkillUpdateForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=you
            data.save()
            return redirect ('my-profile')
    else:
        form=SkillUpdateForm()
    context={
        "user":you,
        "data":profile,
        "skills":skills,
        "form":form,
        "profil_Page":"active",
    }
    return render(request,"candidate/profile.html",context)
        


