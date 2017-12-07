from django import forms

from .models import registrados

#clase regform para los formularios
class RegModelForm(forms.ModelForm):
	class Meta:
		model = registrados
		fields = ["nombre", "email"]

	#medotos para validaciones
	#def clean_email(self): # definir nuestras propias validaciones
	#	email = self.cleaned_data.get("email")
	#	email_base, proveedor = email.split("@")
	#	dominio, extension = proveedor.split(".")
	#	if not extension == "com":
	#		raise forms.ValidationError("Por favor utilice un email con la dirección .com")
	#	return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)