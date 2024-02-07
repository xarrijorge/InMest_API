# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index1 (request):

    return JsonResponse(
        data = {
        "name":"Karen",
        "email":"karen@gmail.com",
        "number":"07968877666"}
    )

# def filter_queries(request):
#     return JsonResponse(
        
#     )


def filter_queries(request, id):
    queries = [
       {
        'id': 1,
        'title': "Jairus Musa Karenzo",
        'description': "Kind,Handsome",
        'status': "Inlove",
        'submitted_by': "Otanga " ,
        },

        {
            'id': 2,
        'title': "Jairus Otanga Karenzo",
        'description': "Kind,Handsome",
        'status': "Inlove",
        'submitted_by': "Otanga " ,
        }
    ]


    filtered_query=[query for query in queries if query["id"] == id]

    query = filtered_query[0]

    return JsonResponse(query, safe=False)




class QueryView(View):

 queries= [
        {"id":"1","title":"Karen"},
        {"id":"2","title":"Jairus"}
        ]
 def get(self,request):
    
    return JsonResponse(self.queries,safe=False)