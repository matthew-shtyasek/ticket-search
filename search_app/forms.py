from django import forms

from search_app.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['train_number',
                   'id']
