from django import forms
from .models import Enquiry
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','organisation','email','phone','topic','message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your name'}),
            'organisation': forms.TextInput(attrs={'placeholder':'Organisation'}),
            'email': forms.EmailInput(attrs={'placeholder':'Business email'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone / WhatsApp'}),
            'topic': forms.Select(choices=[('', 'Select an advisory topic'),('Quality strategy','Quality strategy & governance'),('Operational excellence','Operational excellence'),('Customer quality','Customer quality / complaints'),('Supplier quality','Supplier quality / development'),('NPI / APQP','NPI / APQP / PFMEA'),('Digital quality','Digital quality transformation'),('Capability academy','Capability building / Lean Six Sigma'),('Executive advisory','Board / CXO advisory')]),
            'message': forms.Textarea(attrs={'rows':6,'placeholder':'What problem are you trying to solve? Include timing, scale and business impact where possible.'}),
        }
