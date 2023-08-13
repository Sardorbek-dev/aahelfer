from django.contrib import admin
from .models import CustomerReview, ContactUs

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(CustomerReview)