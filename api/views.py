import time

from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.test import TestCase
from django.http import JsonResponse

from .models import Fibo

def fibonacci_calculation(number):
    a, b = 0, 1
    for i in xrange(1, number+1):
        a, b = b, a+b

    return a

class Fibonacci(generics.RetrieveAPIView):
    
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request):
        number = 0
        result = 0
        time_taken = 0
        status = True

        if request.query_params.get('number'):
            import pdb;pdb.set_trace()
            number = request.query_params.get('number')
            try:
                number = int(number)
            except:
                status = False
                message = "provide a valid number"
                return Response({'status':status, 'message':message}, template_name='fail.html')

            if number<=0:
                status = False
                if number==0:
                    message = "zero is not allowed"
                else:
                    message = "negative integer is not allowed"
                return Response({'status':status, 'message':message}, template_name='fail.html')
                
            start_time = time.time()
            
            if not Fibo.objects.filter(number=number):
                result = fibonacci_calculation(number)
                obj = Fibo.objects.create(number=number, result=str(result))
                obj.save()
            else:
                result = int(Fibo.objects.values_list('result').filter(number=number).\
                    first()[0])
            
            time_taken = time.time() - start_time
        return Response({'number': number,'result': result,'time_taken': \
            time_taken}, template_name='home.html')
