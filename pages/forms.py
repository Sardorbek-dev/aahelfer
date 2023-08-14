from django import forms
from .models import CustomerReview, ContactUs

class ContactUsForm(forms.ModelForm):
    # salutation = forms.CharField(widget=forms.RadioSelect(attrs={'class': "form-control my-2"}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vorname*', 'class': "form-control my-2"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nachname*', 'class': "form-control my-2"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Adresse*', 'class': "my-2 form-control new-Email"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefonnummer*', 'class': "form-control my-2"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Straße und Hausnummer*', 'class': "form-control my-2"}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postleitzahl*', 'class': "form-control my-2"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject*', 'class': "form-control my-2"}))
    data_protection = forms.BooleanField(required=True, error_messages={'required': "Sie haben die Datenschutzerklärung nicht akzeptiert"})

    class Meta:
        model = ContactUs
        fields = ['salutation', 'firstname', 'lastname', 'email', 'phone_number', 'address', 'zip_code', 'subject', 'content', 'data_protection']
        widgets = {
            'salutation': forms.RadioSelect()
        }

class CustomerReviewForm(forms.ModelForm):
    reviewer_firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vorname*', 'class': "form-control my-2"}))
    reviewer_lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nachname*', 'class': "form-control my-2"}))
    reviewer_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Adresse*', 'class': "my-2 form-control new-Email"}))

    class Meta:
        model = CustomerReview
        fields = ['reviewer_salutation', 'reviewer_firstname', 'reviewer_lastname', 'reviewer_email', 'reviewer_serviceType', 'reviewer_rating', 'reviewer_content', 'reviewer_confirmation',]
        widgets = {
            'reviewer_salutation': forms.RadioSelect(),
            'reviewer_rating': forms.RadioSelect(),
            'reviewer_confirmation': forms.RadioSelect()
        }