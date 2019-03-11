from rest_framework import generics
from rest_framework.response import Response
from .models import Tickets, Category
from .serializers import TicketsSerializer, CategorySerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
	action = ''
	try:
		if request.GET['action'] == 'delete':
			action = 'delete'
		
	except:
		action = 'view'
	if action == 'delete':
		Tickets.objects.filter(id=request.GET['id']).delete()	

		template = loader.get_template('tickets/index.html')
		ticketsList = Tickets.objects.all()
		categoryList = Category.objects.all()
		context = {'tickets': ticketsList, 'categories': categoryList}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('tickets/index.html')
		ticketsList = Tickets.objects.all()
		categoryList = Category.objects.all()
		context = {'tickets': ticketsList, 'categories': categoryList}
		return HttpResponse(template.render(context, request))

def searchTicket(request):
	if request.method == 'POST':
		category_id = ''
		stage = ''
		try:
			if request.POST['stage'] != "" and request.POST['category'] != "":
				stage = request.POST['stage']
				category = request.POST['category']
				category_id = request.POST['category']
				category = Category.objects.get(id = category)
				ticketsList = Tickets.objects.filter(stage=stage, category=category)
		except:
			pass	
			
		try:
			if request.POST['stage']:
				stage = request.POST['stage']
				ticketsList = Tickets.objects.filter(stage=stage)
		except:
			pass	

		try:
			if request.POST['category'] != "":
				category = request.POST['category']
				category_id = request.POST['category']
				category = Category.objects.get(id = category)
				ticketsList = Tickets.objects.filter(category=category)
		except:
			pass

		try:
			if ticketsList:
				pass
		except:
				ticketsList = Tickets.objects.all()
		
		template = loader.get_template('tickets/search-ticket.html')
		categoryList = Category.objects.all()
		context = {'tickets': ticketsList, 'categories': categoryList, stage: stage, category_id: category_id}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('tickets/search-ticket.html')
		ticketsList = Tickets.objects.all()
		categoryList = Category.objects.all()
		context = {'tickets': ticketsList, 'categories': categoryList, 'category_id': '', 'stage':''}
		return HttpResponse(template.render(context, request))

def updateTicket(request):
	if request.method == 'POST':
		title = request.POST['title']
		id = request.POST['id']
		description = request.POST['description']
		stage = request.POST['stage']
		category = Category.objects.get(id=request.POST['category'])
		t = Tickets.objects.get(id=id)
		t.title = title
		t.description = description
		t.stage = stage
		t.category = category 
		t.save()

		template = loader.get_template('tickets/update-ticket.html')
		categoryList = Category.objects.all()
		ticket = Tickets.objects.get(id=id)
		context = {'categories': categoryList, 'isUpdated': True, 'ticketId': t.id, 'ticket': ticket, 'id': id}
		return HttpResponse(template.render(context, request))
	else:
		id = ''
		try:
			if request.GET['id']:
				id = request.GET['id']

		except:
			template = loader.get_template('tickets/error.html')
			categoryList = Category.objects.all()
			context = {'categories': categoryList, 'isUpdated': False}
			return HttpResponse(template.render(context, request))

		template = loader.get_template('tickets/update-ticket.html')
		categoryList = Category.objects.all()
		ticket = Tickets.objects.get(id=id)
		context = {'categories': categoryList, 'isCreated': False, 'id': id, 'ticket': ticket}
		return HttpResponse(template.render(context, request))
	

def createTicket(request):
	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		stage = request.POST['stage']
		category = Category.objects.get(id=request.POST['category'])
		t = Tickets(title = title, description = description, stage = stage, category = category)
		t.save()

		template = loader.get_template('tickets/create-ticket.html')
		categoryList = Category.objects.all()
		context = {'categories': categoryList, 'isCreated': True, 'ticketId': t.id}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('tickets/create-ticket.html')
		categoryList = Category.objects.all()
		context = {'categories': categoryList, 'isCreated': False}
		return HttpResponse(template.render(context, request))

class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def list(self, request):
		queryset = self.get_queryset()
		serializer =  CategorySerializer(queryset, many=True)
		return Response(serializer.data)


class TicketsList(generics.ListCreateAPIView):
	queryset = Tickets.objects.all()
	serializer_class = TicketsSerializer

	def list(self, request):
		id_id = self.request.query_params.get('id')
		queryset = self.get_queryset()
		serializer = TicketsSerializer(queryset, many=True)
		return Response(serializer.data)


class TicketData(generics.ListAPIView):
	queryset = Tickets.objects.all()
	serializer_class = TicketsSerializer

	def list(self, request):
		try:
			id_id = self.request.query_params.get('id')
			queryset = Tickets.objects.get(id=id_id)

			#queryset = self.get_queryset()
			serializer = TicketsSerializer(queryset, many=False)
			return Response(serializer.data)
		except:
			category_category = self.request.query_params.get('category')
			queryset = Tickets.objects.filter(category=category_category)

			#queryset = self.get_queryset()
			serializer = TicketsSerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			pass

class CategoryData(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def list(self, request):
		try:
			id_id = self.request.query_params.get('id')
			queryset = Category.objects.get(id=id_id)

			#queryset = self.get_queryset()
			serializer = CategorySerializer(queryset, many=False)
			return Response(serializer.data)
		except:
			pass
