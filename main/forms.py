
from django import forms




MY_CHOICES = (
    ('1', 'model'),
    ('2', 'medimg'),

)

class ImgOptions(forms.Form):
	imgOptions = forms.ChoiceField(choices=MY_CHOICES)

class UploadMedImgForm(forms.Form):
	file = forms.FileField()
	name = forms.CharField()

class UploadModelForm(forms.Form):
	file = forms.FileField()
	name = forms.CharField(required=False)


class ROIForm(forms.Form):
    x1 = forms.IntegerField(label='x1',  required=True)
    y1 = forms.IntegerField(label='y1', required=True)
    x2 = forms.IntegerField(label='x2',  required=True)
    y2 = forms.IntegerField(label='y2',  required=True)

class CompForm(forms.Form):
    id = forms.IntegerField()