from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'joined_date']
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'})
        }
