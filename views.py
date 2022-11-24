from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
# Create your views here.

# @login_required(login_url='/cadastrar/')
def cadastrar_user(request):
    return render(request, 'cadastrousuario.html')   

def login_user(request):
    return render(request, 'login.html')

#acessando login, com usuaro e senha
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Tente novamente.')
    return redirect('/login/')

def submit_cadastrar(request):
    name = request.POST.get('name')
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    usuario_id = request.POST.get('usuario_id')
    description = description 
    usuario = Usuario.objects.create(name=name, email=email, phone=phone, city=city, description=description,
                                user=user, photo=file)
    # url = '/castrar/submit/'.format(pet.id)
    return redirect('/cadastrar/submit/')





#depois que logar vai para essa página

@login_required(login_url='/login/')

#deslogar

def logout_user(request):
    logout(request)
    return redirect('/login/')
#listas pets
def list_usuario_all(request):
    usuario = Usuario.objects.filter(active =True)
    print(usuario.query)
    return render(request, 'list.html', {'usuario':usuario})

def list_user_usuario(request):
    usuario = Usuario.objects.filter(active =True, user=request.user)
    return render(request, 'list.html', {'usuario':usuario})


def usuario_detalhes(request, id):
    usuario = Usuario.objects.get(active =True, id = id)
    print(usuario.id)
    return render(request, 'usuario.html', {'usuario':usuario})

@login_required(login_url='/login/')
def register_usuario(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def submit_usuario(request):
    name = request.POST.get('name')
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    pet_id = request.POST.get('usuario_id')
    description = description 
    usuario = Usuario.objects.create(name=name, email=email, phone=phone, city=city, description=description,
                                user=user, photo=file)
    url = '/usuario/detalhes/{}/'.format(usuario.id)
    return redirect(url)


@login_required(login_url='/login/')
def usuario_delete(request, id):
    usuario = Usuario.objects.get(id = id)
    if usuario.user == request.user:
       usuario.delete()
    return  redirect( '/')