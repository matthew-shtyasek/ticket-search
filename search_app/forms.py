from django import forms

from search_app.models import Ticket


class TicketForm(forms.ModelForm):
    def __init__(self, data=None):
        super().__init__(data)
        for key in self.fields:
            self.fields[key].required = False

    class Meta:
        model = Ticket
        exclude = ['train_number',
                   'id']
