from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import registrados
# Create your views here.
def inicio(request):
	titulo = "hola"
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	
	context = {	#diccionario
		"titulo" : titulo,
		"form": form,
	}

	if form.is_valid(): #si el formulario es valido limpia los fields del formulario
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "Persona"
		instance.save()

		context = {
			"titulo" : "Gracias %s!" %(email)
		}

		if not nombre:
			context = {
				"titulo" : "Gracias %s!"
			}

		print(instance)
		print(instance.timestamp)


	return render(request, "inicio.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Formulario de contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "juniorrk50@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
	context = {
		"form" : form,
	}
	return render(request, "forms.html", context)