from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Advocate

from .serializers import CompanySerializer, AdvocateSerializer

@api_view(['GET'])
def get_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_company(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_advocates(request):
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_advocate(request, id):
    advocate = Advocate.objects.get(id=id)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
