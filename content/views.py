from django.shortcuts import render, redirect


from . import forms
from .import models

def content_create(request, id=0):
    if id == 0:
        if request.method == 'GET':
            form = forms.StudentForm()
            return render(request, 'content/content_index.html', { 'forms':form ,'active1':'active'})
        elif request.method == 'POST':
            form = forms.StudentForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('content:list')              
    else:
        student = models.BsitEmail.objects.get(id=id)
        if request.method == 'GET':
            form = forms.StudentForm(instance=student)
            return render(request, 'content/content_index.html', { 'forms':form,'active1':'active'})
        
        elif request.method == 'POST':
            form = forms.StudentForm(request.POST, instance=student) 
            if form.is_valid():
                form.save()
                return redirect('content:list')



def content_list(request):
    students = models.BsitEmail.objects.all().order_by('fullname')
    return render(request, 'content/content_list.html', {'students':students,'active2':'active'})


def content_delete(request, id):
    try:   
        student = models.BsitEmail.objects.get(id=id)
        student.delete()
        return redirect('content:list')
    except Exception as e:
        return redirect('content:list')

