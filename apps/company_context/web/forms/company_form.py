from django import forms
class CompanyForm(forms.Form):
    code=forms.CharField(max_length=50)
    name=forms.CharField(max_length=250)
    email=forms.EmailField()
    phone=forms.CharField(max_length=50,required=False)
    address=forms.CharField(required=False,widget=forms.Textarea)
