from django import forms

class Contactform(forms.Form):
    full_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    content=forms.CharField(widget=forms.Textarea)

    def clean_full_name(self, *args, **kwargs):
        full_name= self.cleaned_data.get('full_name')
        if not full_name.isalpha():
            raise forms.ValidationError("this is no a valid name")
        return full_name


    