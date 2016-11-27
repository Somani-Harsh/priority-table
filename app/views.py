from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.db import connection
# Create your views here.
# import MySQLdb
from .models import Person

def table(request):
	data = {}
	person = Person.objects.all().order_by("position")
	data = {
		"person" : person,
	}
	data.update(csrf(request))
	return render_to_response("table.html",data)

def save_order(request):
	print(request.POST.getlist("row[]"))
	print(request.POST.values())
	
	count = 0
	# with connection.cursor() as c:
	str_ = ""
	for item in request.POST.getlist("row[]"):
		count += 1
		str_ += " WHEN %s THEN %d"%(item,count)
		
	query = "UPDATE app_person "+\
	   "SET position = CASE id "+\
	                      str_ +\
	                      " END "+\
	"WHERE id IN("+ ",".join(request.POST.getlist("row[]"))+")"   

	with connection.cursor() as c:

		print(query)
		c.execute(query)

	return HttpResponse("hello")