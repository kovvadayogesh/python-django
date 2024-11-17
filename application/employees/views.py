from django.shortcuts import render
from .serializers import EmployeeDetailsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import EmployeeDetails
import logging

# Create your views here.

logging = logging.getLogger(__name__)
@api_view(['GET'])
def emp_details(request):

    if request.method == 'GET':
        logging.info('Fetching all Records.')
        details = EmployeeDetails.objects.all()
        empDetails = EmployeeDetailsSerializers(details,many=True)
        logging.info("data has been received")
        return Response(empDetails.data)
        
