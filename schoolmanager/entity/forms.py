from django import forms
from .models import Class
 

class SearchTeacher(forms.Form):
    """Form for searching teacher"""

    teacher = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Search Teacher Name:"}))

    def save(self, query):
        try:
            teacher = Class.objects.filter(teacher__full_name__icontains=query)
        except Class.DoesNotExist:
            teacher = None
        return teacher