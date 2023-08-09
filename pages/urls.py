from django.urls import path
from .views import HomePageView, AboutPageView, ContactCreateView, OurServicesView, PrivateMoveView, \
                    CompanyMoveView, ConsultingView, MontageView, TransportView, PackagingView, ProcessView, \
                    HouseholdLiquidationView, CompanyLiquidationView, HouseCleaningView, FaqView, ImprintView, \
                    DataProtectionView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('process', ProcessView.as_view(), name='process'),
    path('faq', FaqView.as_view(), name='faq'),
    path('imprint', ImprintView.as_view(), name='imprint'),
    path('data-protection', DataProtectionView.as_view(), name='data-protection'),
    path('our-services', OurServicesView.as_view(), name='our-services'),
    path('private-move', PrivateMoveView.as_view(), name='private-move'),
    path('company-move', CompanyMoveView.as_view(), name='company-move'),
    path('consulting', ConsultingView.as_view(), name='consulting'),
    path('mon-and-demontage', MontageView.as_view(), name='mon-and-demontage'),
    path('transport', TransportView.as_view(), name='transport'),
    path('packaging', PackagingView.as_view(), name='packaging'),
    path('household-liquidation', HouseholdLiquidationView.as_view(), name='household-liquidation'),
    path('company-liquidation', CompanyLiquidationView.as_view(), name='company-liquidation'),
    path('house-cleaning', HouseCleaningView.as_view(), name='house-cleaning'),
]