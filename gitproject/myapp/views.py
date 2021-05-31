from django.shortcuts import render
from .forms import studentForm

# Create your views here.
# @api_view(['get','post'])
def views_login(request):
    form=studentForm()
    if(request.method=='GET'):
        return render(request,'login.html',{'form':form})
    print(request.FILES)
    form=studentForm(request.POST,request.FILES)
    print(form)
    print(form.cleaned_data)
    if(form.is_valid()):
        form.save()
    return render(request,'login.html',{'form':form})