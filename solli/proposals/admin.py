from django.contrib import admin

from proposals.models import ProposalForDonation, ProposalForSolicitation

# Register your models here.
admin.site.register(ProposalForDonation)
admin.site.register(ProposalForSolicitation)