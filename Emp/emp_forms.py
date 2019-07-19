from django import forms

STATUS_CHOICES = (
    (1,"Current"),
    (0,"Releaved")
)

class Add_emp(forms.Form):
    NAME = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}))
    DESIGNATION = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}))
    SALARY = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    STATUS = forms.ChoiceField(choices = STATUS_CHOICES,widget=forms.Select(attrs={'class': "form-control"}))