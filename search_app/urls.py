from django.urls import path

from search_app.views import TicketListView

app_name = 'search_app'

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='tickets'),  # localhost:8000/search/tickets/ | search:tickets
]
