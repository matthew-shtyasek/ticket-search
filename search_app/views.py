from copy import copy

from django.shortcuts import render
from django.views.generic import ListView

from search_app.forms import TicketForm
from search_app.models import Ticket


class TicketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'search_app/ticket_list.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return render(request=request,
                          template_name='search_app/ticket_list_item.html',
                          context=self.get_context_data(object_list=self.model.objects.all()))
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        if not self.request.GET:
            form = TicketForm()
        else:
            form = TicketForm(self.request.GET)
        if form.is_valid():
            cd = copy(form.cleaned_data)
            for key,value in form.cleaned_data.items():
                if not value:
                    del cd[key]
            try:
                cd['departure_date__year'] = cd['departure_date'].year
                cd['departure_date__month'] = cd['departure_date'].month
                cd['departure_date__day'] = cd['departure_date'].day
                del cd['departure_date']
            except:
                pass
            try:
                cd['arrive_date__year'] = cd['arrive_date'].year
                cd['arrive_date__month'] = cd['arrive_date'].month
                cd['arrive_date__day'] = cd['arrive_date'].day
                del cd['arrive_date']
            except:
                pass

            if cd:
                context[self.context_object_name] = Ticket.objects.filter(**cd)
            else:
                context[self.context_object_name] = []
            form = TicketForm()

        context['form'] = form
        return context
