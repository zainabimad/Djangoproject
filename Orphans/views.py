from django.shortcuts import render
from project.models import Authentic
# Create your views here.
from Orphans import form
from Orphans import models
from django.http import HttpResponseRedirect
from project.models import AddAc
import datetime
# Create your views here.


def add_req(request, id):
    x = id
    ide = id.split("splitor")
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i .user_type == 'user':
                addlen = models.AddRe.objects.all()
                nameofre = models.AddOr.objects.all()

                nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
                print(nameofre)
                print(ide)
                if nameofre:
                    print(nameofre[0])
                    addre = form.AddFormRe()
                    if request.method == "POST":
                        addre = form.AddFormRe(request.POST)
                        if addre.is_valid():
                            addlen = models.AddRe.objects.create(locations=request.POST['locations'],
                                                                 detils=request.POST['detils'], success=False,
                                                                 name=nameofre[0], name_g=request.POST['name_g'])
                            addre.save(commit=False)

                            return HttpResponseRedirect("http://127.0.0.1:8000/orphans/add_request/" + str(x))

                    return render(request, 'add_request.html', {'form': addre, 'auth': authentic, 'id': id})
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def show_re(request, id):
    ide = id.split("splitor")
    forms = models.AddRe.objects.all()
    nameofre = models.AddOr.objects.all()
    nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i .user_type == 'user':
                if nameofre:
                    forms = forms.filter(name=nameofre[0])
                    len_request_or = len(forms)
                    if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            forms = models.AddRe.objects.all()
                            if request.GET['sort'] == '0':
                                forms = forms.filter(locations__icontains=request.GET['search'])
                            if request.GET['sort'] == '1':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(success=True)
                            if request.GET['sort'] == '2':
                                forms = forms.filter(locations__icontains=request.GET['search']).exclude(name_g='')
                            if request.GET['sort'] == '3':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(success=False)
                            if request.GET['sort'] == '4':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(name_g__icontains='')
                            len_request_or = len(forms)
                    return render(request, 'show_request.html', {'form': forms, 'auth': authentic, 'id': id, 'len_request_or': len_request_or})
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def ac_or(request, id):
    ide = id.split("splitor")
    nameofre = models.AddOr.objects.all()
    nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
    try:
        if nameofre:
            authentic = Authentic.objects.filter(user=request.user)
            for i in authentic:
                if i.user_type == 'user':
                    act = AddAc.objects.all()
                    act = act.exclude(up_date=datetime.date.today())
                    if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            if request.GET['sort'] == '0' or request.GET['sort'] == '1':
                                act = act.filter(name__icontains=request.GET['search']).exclude(up_date=datetime.date.today())
                            if request.GET['sort'] == '2':
                                act = act.filter(worked__icontains=request.GET['search']).exclude(up_date=datetime.date.today())
                    len_act_or = len(act)
                    return render(request, 'activities_or.html', {'act': act, 'auth': authentic, 'len_act_or': len_act_or, 'id': id})
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")
