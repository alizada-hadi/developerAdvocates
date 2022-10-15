from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Advocate
from .serializers import CompanySerializer, AdvocateSerializer

from rest_framework.pagination import PageNumberPagination

"""*
I am using function base views to create the following endpoints. 
"""


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
    paginator.page_size = 2

    page = paginator.paginate_queryset(companies, request)
    serializer = CompanySerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def get_single_company(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)



# ! Advocate endpoints

@api_view(['GET'])
def get_advocates(request):
    query = request.query_params.get("query")
    if query == None:
        query = ''
    paginator = PageNumberPagination()
    advocates = Advocate.objects.filter(name__icontains=query)
    paginator.page_size = 2

    page = paginator.paginate_queryset(advocates, request)
    serializer = AdvocateSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def get_single_advocate(request, id):
    advocate = Advocate.objects.get(id=id)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
