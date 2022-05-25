from django.shortcuts import render, redirect
from .formulario_registro import formularioRegistro
from .models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from tienda.views import _crear_favoritos
from tienda.models import Favoritos, itemFavoritos

# Importes para enviar el correo
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

def register(request):
    #Este envia la informacion del formulario a la template
    form = formularioRegistro()

    if request.method=='POST':
        form = formularioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']

            """encsha256 = hashlib.sha256()
            encsha256.update(password.encode('utf8'))"""

            user = User.objects.create_user(username=username, first_name=name, last_name=apellido, email=email, password=password, phone_number=phone_number)
            user.save()

            #Metodo para enviar el correo
            current_site = get_current_site(request)
            mail_subject = 'Correo de activacion de cuenta Tornilub.'
            body = render_to_string('email_verification.html', {
                'name':name,
                'apellido':apellido,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), # forma de codificar un dato
                'token':default_token_generator.make_token(user), #mandando un token
                'domain':current_site,
            })

            to_email = email # para quien sera el correo
            send_email = EmailMessage(mail_subject, body, to=[email])#objeto para mandar el correo junto con los parametros necesarios
            send_email.send()#Enviando el correo

            #mensaje de usuario registrado exitosamente
            messages.success(request, 'Se registro el Usuario exitosamente')

            #from irsmain.whatsapp import whatsapp_welcome as wsw

            #wsw(phone_number)

            return redirect('/account/login/?command=verification&email='+email)       

    context = {
        'form':form,
    }

    return render(request, 'tienda/registrarse.html', context)

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:

            try:
                favoritos = Favoritos.objects.get(id_favorito=_crear_favoritos(request))
                existen_favoritos = itemFavoritos.objects.filter(favorit=favoritos).exists()
                if existen_favoritos:
                    favoritos_items = itemFavoritos.objects.filter(favorit=favoritos) #esto devuelve una lista
                    for item in favoritos_items:
                        item.user = user
                        item.save()
            except:
                pass

            auth.login(request, user)
            messages.success(request, 'Bienvenido')
            return redirect('dashboard')
        else:
            messages.error(request, 'Nombre de Usuario o Contrase;a incorrectos')
            redirect('login')

    return render(request, 'tienda/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)

    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Felicidades tu cuenta esta activa!')
        return redirect('login')
    else:
        messages.error(request, 'La activacion es invalida')
        return redirect('login')

@login_required(login_url='login')
def dashboard(request):

    return render(request, 'accounts/dashboard.html')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Felicidades tu cuenta ha sido activada!')
        return redirect('login')
    else:
        messages.error(request, 'La activacion es invalida')
        return redirect(request, 'registrarse')

# Create your views here.
def forgotpassword(request):

    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            current_site = get_current_site(request)
            mail_subtect = 'Restrablacer contrase;a'
            body = render_to_string('cambiarpassword.html', {
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })

            to_email = email
            send_email = EmailMessage(mail_subtect, body, to=[to_email])
            send_email.send()

            messages.success(request, 'El correo para restablecer contrase;a fue enviado')
            return redirect('login')
        else:
            messages.error('El email no existe')
            return redirect('forgotpassword')

    return render(request, 'accounts/forgotpassword.html')

def resetearpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, User.DoesNotExist, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'porfavor reinicia tu password')
        return redirect('resetearpassword')

    else:
        messages.error(request, 'El link ha expirado')
        return redirect('login')

def resetearpassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_passowrd = request.POST['confirm_password']

        if password == confirm_passowrd:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)

            user.set_password(password)
            user.save()
            messages.success(request, 'La contrase;a se ha cambiado con exito!')
            return redirect('login')

        else:
            messages.error(request, 'las contrase;as no coinciden')
            return redirect('resetearpassword')

    return render(request, 'resetearpassword.html')