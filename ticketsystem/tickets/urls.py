from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	path('category/', views.CategoryList.as_view()),
	path('single-ticket/', views.TicketData.as_view()),
	path('single-category/', views.CategoryData.as_view()),
	path('tickets/', views.TicketsList.as_view()),
	path('', views.index, name='index'),
	path('create-ticket/', views.createTicket, name='create-ticket'),
	path('update-ticket/', views.updateTicket, name='update-ticket'),
	path('search-ticket/', views.searchTicket, name='search-ticket'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
