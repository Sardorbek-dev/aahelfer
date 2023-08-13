from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm, CustomerReviewForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactCreateView(TemplateView):
    template_name = 'contact.html'

class OurServicesView(TemplateView):
    template_name = 'our-services.html'

class PrivateMoveView(TemplateView):
    template_name = 'private-move.html'

class CompanyMoveView(TemplateView):
    template_name = 'company-move.html'

class ConsultingView(TemplateView):
    template_name = 'consulting.html'

class MontageView(TemplateView):
    template_name = 'montage.html'

class TransportView(TemplateView):
    template_name = 'transport.html'

class PackagingView(TemplateView):
    template_name = 'packaging.html'

class ProcessView(TemplateView):
    template_name = 'process.html'

class HouseholdLiquidationView(TemplateView):
    template_name = 'household-liquidation.html'

class CompanyLiquidationView(TemplateView):
    template_name = 'company-liquidation.html'

class HouseCleaningView(TemplateView):
    template_name = 'house-cleaning.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class ImprintView(TemplateView):
    template_name = 'imprint.html'

class DataProtectionView(TemplateView):
    template_name = 'data-protection.html'


class ContactCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact.html'

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user

            #send email
            template = render_to_string('email_template.html', {'name': self.request.POST['firstname']})
            email = EmailMessage(
                'Info A&A Team',
                template,
                settings.EMAIL_HOST_USER,
                [self.request.POST['email']]
            )
            fail_silently = False
            email.send()

            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"An error occurred: {e}")
            return self.form_invalid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        success_text = 'Vielen Dank! Ihre Anfrage ist eingegangen.<br> ' \
                       'Ihre Nachricht wurde erfolgreich übermittelt. Unser Team wird sich in Kürze mit Ihnen in Verbindung setzen! <br>'\
                       '<br>' \
                       'Mit freundlichen Grüßen,<br>' \
                       'A&A Team'
        messages.success(self.request, success_text)
        return reverse_lazy('contact')

class SendReviewView(CreateView):
    form_class = CustomerReviewForm
    template_name = 'send-review.html'

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user

            #send email
            template = render_to_string('email-template-success-review.html')
            email = EmailMessage(
                'Bewertung erfolgreich eingereicht',
                template,
                settings.EMAIL_HOST_USER,
                [self.request.POST['reviewer_email']]
            )
            fail_silently = False
            email.send()

            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"An error occurred: {e}")
            return self.form_invalid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        success_text = 'Vielen Dank! Ihre Bewertung ist eingegangen. <br>' \
                       'Ihre Bewertung wurde erfolgreich übermittelt. Wir schätzen Ihr Feedback sehr.<br> ' \
                       'Bei Fragen oder weiteren Anliegen stehen wir Ihnen gerne zur Verfügung!<br>' \
                       '<br>' \
                       'Mit freundlichen Grüßen,<br>' \
                       'A&A Team'
        messages.success(self.request, success_text)
        return reverse_lazy('send-review')
