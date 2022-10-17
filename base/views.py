from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Advocate, Project
from .serializers import CompanySerializer, AdvocateSerializer, ProjectSerializer

from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

"""*
I am using function base views to create the following endpoints. 

"""
@api_view(['GET'])
def endpoints(request):
    apis = [
        "https://developer-advocate.herokuapp.com/api/companies", 
        "https://developer-advocate.herokuapp.com/api/company/1", 
        "https://developer-advocate.herokuapp.com/api/advocates",  
        "https://developer-advocate.herokuapp.com/api/advocate/1", 
        "https://developer-advocate.herokuapp.com/api/projects", 

    ]

    return Response(apis)


# fetch all companies
@api_view(['GET'])
# @permission_classes([AllowAny, ]) since we do not implement the auth funcs
def get_companies(request):
    # implement searching and filtering
    query = request.query_params.get("query")
    if query == None:
        query = ''
    # paginate the data
    paginator = PageNumberPagination()
    # filter data based on received search and filter params
    companies = Company.objects.filter(name__icontains=query)
    # items per page
    paginator.page_size = 1

    page = paginator.paginate_queryset(companies, request)
    serializer = CompanySerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

# get company detail
@api_view(['GET'])
def get_single_company(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)



# ! Advocate endpoints
# get all advocates, implement pagination, filtering, and searching
@api_view(['GET'])
def get_advocates(request):
    query = request.query_params.get("query")
    if query == None:
        query = ''
    paginator = PageNumberPagination()
    advocates = Advocate.objects.filter(
        Q(name__icontains=query) |
        # filter advocates based on thier skills
        Q(skill__title=query)
        ).distinct() # to avoid returning duplicate data we use distinct method
    paginator.page_size = 2
    page = paginator.paginate_queryset(advocates, request)
    serializer = AdvocateSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)


# get advocate detail
@api_view(['GET'])
def get_single_advocate(request, id):
    advocate = Advocate.objects.get(id=id)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ! projects endpoints
@api_view(['GET'])
def get_projects(request):
    query = request.query_params.get("query")
    if query == None:
        query = ''
    paginator = PageNumberPagination()
    projects = Project.objects.filter(
        # filter based on project title and description
        Q(title__icontains=query) |
        Q(description__icontains=query)
        )
    paginator.page_size = 2
    page = paginator.paginate_queryset(projects, request)
    serializer = ProjectSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)
