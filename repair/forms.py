<<<<<<< HEAD

from django import forms

from . import models

#for updating status of order

class Updateform(forms.ModelForm):
    class Meta:
        model=models.Enquiry
        fields=['status']
=======

from django import forms

from . import models

#for updating status of order

class Updateform(forms.ModelForm):
    class Meta:
        model=models.Enquiry
        fields=['status']
>>>>>>> 82835c48c97b5622541c6cb9e52efcec4ece4bb2
