from django.shortcuts import render
from django.views.generic import TemplateView

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