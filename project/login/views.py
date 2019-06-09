from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Fonction de connexion
def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'login/login_page.html', {})

# Fonction de déconnexion
def log_out(request):
    logout(request)
    return redirect('/')


# Fonction de création de compte
def create(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        mail = request.POST.get('mail', False)
        error_messages = []
        if username == "":
            error_messages += ['Veuillez renseigner votre nom d\'utilisateur.']
        if password == "":
            error_messages += ['Le champ mot de passe est requis.']
        if mail == "":
            error_messages += ['Votre adresse mail est requise.']
        if(len(error_messages) > 0):
            return render(request, 'login/create-account.html', {
                'errors' : error_messages,
                'username' : username,
                'mail' : mail,
            })
        isUser = User.objects.filter(username=username).count()
        if isUser > 0:
            error_messages += ['Cet utilisateur existe déjà.']
            return render(request, 'login/create-account.html', {
                'errors' : error_messages,
                'username' : username,
                'mail' : mail,
            })
        isMail = User.objects.filter(email=mail).count()
        if isMail > 0:
            error_messages += ['Cette adresse mail est déjà utilisée.']
            return render(request, 'login/create-account.html', {
                'errors' : error_messages,
                'username' : username,
                'mail' : mail,
            })
        user = User.objects.create_user(username, mail, password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login/create-account.html', {})


# Edition de profil
@login_required
def edit(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        error_messages = []
        if username == "":
            error_messages += ['Veuillez renseigner votre nom d\'utilisateur.']
        if mail == "" :
            error_messages += ['Votre adresse mail est requise.']
        if(len(error_messages) > 0):
            return render(request, 'login/edit-account.html', {
                'errors' : error_messages,
            })
        isUser = User.objects.filter(username=username).exclude(username=request.user.username).count()
        if isUser > 0:
            error_messages += ['Ce nom d\' utilisateur est déjà pris : ' + username]
            return render(request, 'login/edit-account.html', {
                'errors' : error_messages,
                'username' : username,
                'mail' : mail,
            })
        isMail = User.objects.filter(email=mail).exclude(email=request.user.email).count()
        if isMail > 0:
            error_messages += ['Cette adresse mail est déjà utilisée : ' + mail]
            return render(request, 'login/edit-account.html', {
                'errors' : error_messages,
            })
        request.user.username = username
        request.user.email = mail
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        return redirect('/')
    else:
        return render(request, 'login/edit-account.html', {})
