from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class formularioRegistro(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


    def clean(self):
        cleaned_data = super(formularioRegistro, self).clean() #Importante el clean es para obetener valores del formulario
        captcha = cleaned_data.get('captcha')

        if captcha == None:
            raise forms.ValidationError('Por favor completa el recapcha')


        
        