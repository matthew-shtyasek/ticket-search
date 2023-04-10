from django.contrib import admin

from search_app.models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    exclude = ['id']
    '''fields = ['departure_date',
              'arrive_date',
              'train_number',
              'destination',
              'departure',
              'cost']'''

