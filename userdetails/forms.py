from django import forms
from .models import Size_Chart, Image_Chart

class PostForm(forms.ModelForm):
    image = forms.FileField()
    Gender = forms.CharField()
    class Meta:
        model = Image_Chart
        fields =[
        	"image",
        	"Gender",
        ]