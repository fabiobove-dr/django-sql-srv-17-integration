from django.shortcuts import render
from .models import Test
from django.db import connections
import pyodbc

def test_list(request):
    try:
        with connections['secondary'].cursor() as cursor:
            cursor.execute('SELECT * FROM [dbo].[tab_test]')
            rows = cursor.fetchall()
            # Get the column names from the cursor description
            columns = [col[0] for col in cursor.description]
            # Convert the list of tuples into a list of dictionaries
            data = [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        data = str(e)

    return render(request, 'test_list.html', {'test_data': data})
