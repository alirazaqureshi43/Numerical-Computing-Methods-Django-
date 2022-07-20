from django.shortcuts import render, HttpResponse
from . import forms


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Jiye Muhahir")
            print(form.cleaned_data['name'])

    return render(request,'form_page.html',{'form':form})


  





      