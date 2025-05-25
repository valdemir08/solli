from django.db import models
from core.models import BaseProposal
from users.models import User


# Create your models here.

class ProposalForDonation(BaseProposal):
    donation = models.ForeignKey("donations.Donation", on_delete=models.CASCADE, related_name="proposals")
    #related name para facilitar consultas de qtd de propostas nas doações
    #exemplo de uso doacao.proposals.all()
    solicitor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="solicitors")

class ProposalForSolicitation(BaseProposal):
    solicitation = models.ForeignKey("solicitations.Solicitation", on_delete=models.CASCADE, related_name="proposals")
    potential_donor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="potential_donors")
