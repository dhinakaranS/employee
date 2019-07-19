from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Emp.models import employee #class should be caps
from django.contrib import messages
from Emp.emp_forms import Add_emp 

# Create your views here.

def emp_html(request):
    form = Add_emp()
    return render(request,'add_emp.html', {'addform' : form})

def list_employees(request):
    return render(request,'List_emp.html')

def save_emp(request):
    if (request.method == 'POST'):
        form = Add_emp(request.POST)
        if form.is_valid():            
            print('Saved')
            obj = employee() #gets new object
            obj.NAME = form.cleaned_data['NAME']
            obj.DESIGNATION = form.cleaned_data['DESIGNATION']
            obj.SALARY = form.cleaned_data['SALARY']
            obj.STATUS = form.cleaned_data['STATUS'] 
            obj.save()
            return HttpResponseRedirect('/employees')
        else:
            print('Form not valid')
            return HttpResponseRedirect('/')
    else:
        print('Not a valid request')
        return HttpResponseRedirect('/')
        

