from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Subscriber,Service
import json
# Create your views here.
def home(request):
    
    return render(request, 'main/home.html')

def about(request):
    
    return render(request, 'main/about.html')

def services(request):
    services = Service.objects.filter(display=True)
    return render(request, 'main/services.html', {'services': services})

def contact(request):
    return render(request, 'main/contact.html')\
 
@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('EMAIL')
        if email:
            Subscriber.objects.create(email=email)
            print(f'Received subscription from {email}')
            return JsonResponse({'message': 'Subscription successful'})
        else:
            return JsonResponse({'error': 'No email provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)