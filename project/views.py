from django.shortcuts import render
from .models import Authentic
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from Orphans.models import AddOr
from Orphans.models import AddRe
from Orphans.form import AddForm
from Orphans.form import AddFormRe
from Guarantor.form import AddFormG
from Guarantor.models import AddGu
from .form import AddFormAc
from .models import AddAc

# Create your views here.


def base(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        print(authentic)
        for i in authentic:
            if i.user_type == 'user':
                ide = id.split("splitor")
                nameofre = AddOr.objects.all()
                nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
                if nameofre:
                    return render(request, 'base.html', {'auth': authentic, 'id': id})
            if i.user_type == 'superuser':
                ide = id.split("splitg")
                nameofre = AddGu.objects.all()
                nameofre = nameofre.filter(id=ide[0]).filter(name=ide[1])
                if nameofre:
                    return render(request, 'base.html', {'auth': authentic, 'id': id})
            else:
                return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect("http://127.0.0.1:8000/")
    return render(request, 'login.html')


def signor(request):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'user':
                form = AddForm()
                count = AddOr.objects.all()
                if request.method == "POST":
                    form = AddForm(request.POST, request.FILES)
                    vaild = request.POST['name'].split(" ")
                    print(len(vaild))
                    if len(vaild) < 3:
                        pass
                    if len(vaild) >= 3 and vaild[2] != '':
                        if form.is_valid():
                            form.save()
                            count = count.filter(name=request.POST['name'])
                            print(True)
                            for i in count:
                                print(i.name)
                                return HttpResponseRedirect("http://127.0.0.1:8000/" + str(i.id) + "splitor" + str(i.name))
                        else:
                            print(False)
                            return render(request, 'login_or.html', {'form': form, 'auth': False})
                return render(request, 'login_or.html', {'form': form})
            if i.user_type == 'superuser':
                form = AddFormG()
                count = AddGu.objects.all()
                if request.method == "POST":
                    form = AddFormG(request.POST, request.FILES)
                    vaild = request.POST['name'].split(" ")
                    print(len(vaild))
                    if len(vaild) < 3:
                        pass
                    if len(vaild) >= 3 and vaild[2] != '':
                        if form.is_valid():
                            form.save()
                            count = count.filter(name=request.POST['name'])
                            for i in count:
                                print(i.work)
                                return HttpResponseRedirect("http://127.0.0.1:8000/" + str(i.id) + "splitg" + str(i.name))
                        else:
                            print(False)
                            return render(request, 'login_or.html', {'form': form, 'auth': False})
                return render(request, 'login_or.html', {'form': form})
            if i.user_type == 'admin':
                return render(request, 'login_or.html', {'auth': authentic})

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def have(request):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'user':
                form = AddForm()
                count = AddOr.objects.all()
                if request.method == "POST":
                        form = AddForm(request.POST)
                        print(form)
                        count = count.filter(name=request.POST['name']).filter(number=request.POST['number'])
                        print(count)
                        if count:
                            for x in count:
                                print(x.name)
                                return HttpResponseRedirect("http://127.0.0.1:8000/" + str(x.id) + "splitor" + str(x.name))
                        else:
                            return render(request, 'have.html')
                return render(request, 'have.html')
            if i.user_type == 'superuser':
                form = AddFormG()
                count = AddGu.objects.all()
                if request.method == "POST":
                        form = AddFormG(request.POST)
                        count = count.filter(name=request.POST['name']).filter(number=request.POST['number'])
                        if count:
                            for x in count:
                                print(x.work)
                                return HttpResponseRedirect("http://127.0.0.1:8000/" + str(x.id) + "splitg" + str(x.name))

                return render(request, 'have.html')
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def all_gua(request):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddGu.objects.all()
                if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            nameofre = AddGu.objects.all()
                            nameofre = nameofre.filter(name__icontains=request.GET['search'])
                        return render(request, 'all_gua.html', {'form': nameofre, 'auth': authentic})
                return render(request, 'all_gua.html', {'form': nameofre, 'auth': authentic})
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def del_gua(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddGu.objects.filter(id=id)
                forms = AddRe.objects.filter(name_g=nameofre[0])
                for i in forms:
                    AddRe.objects.create(locations=i.locations,
                                                                             detils=i.detils, success=True,
                                                                             name=i.name, name_g='')

                print(forms)
                nameofre.delete()
                forms.delete()
                return HttpResponseRedirect("http://127.0.0.1:8000/all_gua/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def all_or(request):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddOr.objects.all()
                if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            nameofre = AddOr.objects.all()
                            nameofre = nameofre.filter(name__icontains=request.GET['search'])
                        return render(request, 'all_or.html', {'form': nameofre, 'auth': authentic})
                return render(request, 'all_or.html', {'form': nameofre, 'auth': authentic})
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def del_or(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddOr.objects.filter(id=id)

                nameofre.delete()
                return HttpResponseRedirect("http://127.0.0.1:8000/all_or/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def ac(request):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                forms = AddFormAc()
                act = AddAc.objects.all()
                if request.method == 'POST':
                    forms = AddFormAc(request.POST)
                    if forms.is_valid():
                        forms.save()
                        return HttpResponseRedirect("http://127.0.0.1:8000/activities/")
                    else:
                        return render(request, 'Activities.html', {'form': forms, 'act': act, 'auth':authentic})
                act = AddAc.objects.all()
                return render(request, 'Activities.html', {'form': forms, 'act': act, 'auth': authentic})
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def del_act(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddAc.objects.filter(id=id)

                nameofre.delete()
                return HttpResponseRedirect("http://127.0.0.1:8000/activities/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def show_all_re_ad(request):
    forms = AddRe.objects.all()
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i .user_type == 'admin':

                    forms = AddRe.objects.all()
                    forms = forms.filter(locations__icontains='')
                    print(forms)
                    len_request_or = len(forms)
                    if request.method == "GET":
                        if 'search' in request.GET and request.GET['search'] != '':
                            forms = AddRe.objects.all()
                            if request.GET['sort'] == '0' or request.GET['sort'] == '1':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(success=True)
                            if request.GET['sort'] == '2':
                                forms = forms.filter(locations__icontains=request.GET['search']).filter(success=False)
                            len_request_or = len(forms)
                    return render(request, 'show_all_request_ad.html', {'form': forms, 'auth': authentic, 'len_request_or': len_request_or})

            else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/")
    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def delete_request(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                nameofre = AddRe.objects.filter(id=id)
                nameofre.delete()
                return HttpResponseRedirect("http://127.0.0.1:8000/show_ad/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def accept(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                forms = AddRe.objects.filter(id=id)
                for i in forms:
                    AddRe.objects.create(locations=i.locations,
                                                                             detils=i.detils, success=True,
                                                                             name=i.name, name_g=i.name_g)
                forms.delete()
                return HttpResponseRedirect("http://127.0.0.1:8000/show_ad/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


def edit(request, id):
    try:
        authentic = Authentic.objects.filter(user=request.user)
        for i in authentic:
            if i.user_type == 'admin':
                msg = ""

                form = AddFormRe()
                lic = AddRe.objects.filter(id=id)
                if request.method == "POST":
                    form = AddFormRe(request.POST, instance=lic.get(id=id))
                    if form.is_valid():
                        form.save()
                        msg = 'Done'
                        return render(request, 'admin_edit.html', {'form': form, 'edit_mode': True, 'lis': lic, 'msg': msg})
                    else:
                        form = AddFormRe(instance=lic.get(id=id))
                return render(request, 'admin_edit.html', {'form': form, 'edit_mode': True, 'lis': lic})
            else:
                return HttpResponseRedirect("http://127.0.0.1:8000/login/")

    except:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")


