from django import forms
from .models import User_Feedback

class UserFeedback(forms.ModelForm):
    class Meta:
        model = User_Feedback
        fields = ['name','feedback']
        widgets = {
            'name' : forms.TextInput(attrs ={'class':'form-control'}), 
            'feedback' : forms.Textarea(attrs = {'class':'form-control'}),
        }
        