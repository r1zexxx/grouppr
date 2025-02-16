from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.

def insert_data(request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users_user (column1, column2) VALUES (%s, %s)", ['value1', 'value2'])
    return HttpResponse("Data inserted successfully!")