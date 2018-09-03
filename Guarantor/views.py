from django.shortcuts import render
from Guarantor import models as mod
from Orphans import models
from project.models import Authentic
from django.http import HttpResponseRedirect
# Create your views here.


def show_all_re(request, id):
    ide = id.split("splitg")
    forms = models.AddRe.objects.all()
    nameofre = mod.AddGu.objects.all()
    nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i .user_type == 'superuser':
                if nameofre:

                    forms = models.AddRe.objects.all()
                    forms = forms.filter(locations__icontains='').filter(success=True).filter(name_g='')
                    print(forms)
                    len_request_or = len(forms)
                    if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            forms = models.AddRe.objects.all()
                            forms = forms.filter(locations__icontains=request.GET['search']).filter(success=True).filter(name_g='')
                            len_request_or = len(forms)
                    return render(request, 'show_all_request.html', {'form': forms, 'auth': authentic, 'id': id, 'len_request_or': len_request_or})
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def savee(request, id, ide):
    ids = ide.split('splitg')
    forms = models.AddRe.objects.filter(id=id)
    nameofre = mod.AddGu.objects.filter(id=ids[0])
    print(forms)
    for i in forms:
        models.AddRe.objects.create(locations=i.locations,
                                                                 detils=i.detils, success=True,
                                                                 name=i.name, name_g=nameofre[0])
    forms.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/guarantor/show_all_request/" + str(ide))


def have_request(request, id):
    ide = id.split("splitg")
    forms = models.AddRe.objects.all()
    nameofre = mod.AddGu.objects.all()
    nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i .user_type == 'superuser':
                if nameofre:

                    forms = models.AddRe.objects.all()
                    forms = forms.filter(locations__icontains='').filter(success=True).filter(name_g=nameofre[0])
                    print(forms)
                    len_request_or = len(forms)
                    if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            forms = models.AddRe.objects.all()
                            if request.GET['sort'] == '0' or request.GET['sort'] == '1':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(success=True).filter(name_g=nameofre[0])
                            if request.GET['sort'] == '2':
                                forms = forms.filter(name__icontains=request.GET['search']).filter(success=True).filter(name_g=nameofre[0])
                            len_request_or = len(forms)
                    return render(request, 'have_request.html', {'form': forms, 'auth': authentic, 'id': id, 'len_request_or': len_request_or})
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")
