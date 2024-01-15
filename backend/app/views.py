from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import User

import random
import string , json

def generate_unique_card_number():
    card_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    while not User.objects.filter(card_number=card_number).exists():
        return card_number

@csrf_exempt
def index(req):
    if req.method == 'POST':
        user_data = json.loads(req.body)
        user_data['card_number'] = generate_unique_card_number()


        allValues = all([not val in [None,""] for val in user_data.values() ])
        print('ALL VALUES:',allValues)
        if allValues:
            try:
                User.objects.create(**user_data)
                return JsonResponse({'user':user_data})
            except IntegrityError as e:
                return JsonResponse({'error':str(e)})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Missing values'})
        
    return JsonResponse({'error': 'method not allowed'}, status=405)



@csrf_exempt
def get_card_details(req):
    data = json.loads(req.body)
    card_number = str(data['card_number'])
    user = User.objects.filter(card_number = card_number)

    try:
        user = User.objects.get(card_number = card_number)
        return JsonResponse({
            'user':{
                'fullname':user.fullname,
                'email':user.email,
                'user_type':user.user_type,
                'card_number':user.card_number
                }
            })
    except User.DoesNotExist:
        return JsonResponse({'error': 'No user found with the specified card number.'}, status=404)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

