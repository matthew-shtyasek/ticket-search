from django.shortcuts import render
from django.views.generic import ListView

from search_app.models import Ticket


class TicketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'search_app/ticket_list.html'
