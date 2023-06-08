from django.forms import ModelForm
from .models import Profile,Skill,userSkill


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude=["user"]
class SkillUpdateForm(ModelForm):
    class Meta:
        model = userSkill
        fields= '__all__'

 