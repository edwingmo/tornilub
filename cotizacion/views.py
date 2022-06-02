from django.shortcuts import render, redirect
from tienda.models import Productos
from accounts.models import User
from django.contrib import messages
from .form import formularioRegistro

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

# Create your views here.
def solicitarcot(request, id_product = None):
    form = formularioRegistro()

    producto_email = None

    if id_product != None:
        try:
            producto_email = Productos.objects.get(id=id_product)
        except:
            messages.error(request, 'El producto no existe')
    else:
        pass
    
    context = {
        'producto_email':producto_email,
        "capcha_form":form,
    }
      
    return render(request, 'cotiz.html', context)

def enviarcotiz(request):

    form = formularioRegistro()

    if request.method == "POST":
        email = request.POST['email']
        form = formularioRegistro(request.POST)   
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            if form.is_valid():

                mail_subtect = request.POST['asunto']
                body = render_to_string('enviarcotizacion.html', {
                    'email':user.email,
                    'texto':request.POST['pregunta'],
                    'nombre':user.first_name,
                    'apellido':user.last_name,
                })

                to_email = 'tornilub.noreply@gmail.com'
                send_email = EmailMessage(mail_subtect, body, to=[to_email])
                send_email.send()

                messages.success(request, 'El Correo de cotizacion fue enviado')
            else:
                messages.error(request, 'Completa el Capcha')
    else:
        pass

    return redirect('solicitarcot')