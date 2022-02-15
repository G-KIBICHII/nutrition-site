from django.shortcuts import render,redirect
from cereals.forms import authform
from cereals.models import logg,cereal
# Create your views here.
def login(request):
    return render(request,'login.html')
def main(request):
    if(request.method=='POST'):
        form=authform(request.POST)
        if(form.is_valid()):
            obj=form.cleaned_data
            uname=request.POST.get('user')
            x=logg.objects.get(user=uname)
            pass1=request.POST.get('passer')
            if(x.passer==pass1):
                return render(request,'home.html',{'top':310,'left':440,'nn':"SeArCHf0oD!",'ww':''})
            else:
                return render(request,'login.html',{'test':'L0gIn aGAiN!'})
        
def change(request):
    if(request.method=='POST'):
        x=request.POST.get('search')
        w=cereal.objects.filter(name__icontains=x)
        ret=[]
        for i in w:
            new=[]
            new.append(i.name)
            new.append(i.calories)
            new.append(i.protein)
            new.append(i.fat)
            new.append(i.sodium)
            new.append(i.fiber)
            new.append(i.carbo)
            new.append(i.sugars)
            new.append(i.potass)
            new.append(i.vitamins)
            new.append(i.rating)
            ret.append(new)
            

        stt='n0 mATch f0uND!'
        return render(request,'home.html',{'values':ret,'top':30,'left':40,'nn':x,'ww':stt})

def logout(request):
    if(request.method=='POST'):
        return render(request,'login.html')