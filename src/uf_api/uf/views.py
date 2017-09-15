from decimal import Decimal
from datetime import datetime, date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uf.models import UF
from uf.serializers import UFSerializer

@csrf_exempt
def list(request):
    if request.method == 'GET':
        all_uf = UF.objects.all()
        serie = UFSerializer(all_uf, many=True)
        return JsonResponse(serie.data, safe=False)
    else:
        return JsonResponse({'error': 'only GET method allowed'}, status=400)

def price(request):
    if request.method == 'GET':
        date_str = request.GET.get('date', '')
        value_str = request.GET.get('value', '')
        try:
            date = datetime.strptime(date_str, '%Y%m%d').date()
            value =  Decimal(value_str)
        except ValueError:
            return JsonResponse({'error': 'value error'}, status=400)
        try:
            uf = UF.objects.get(date=date)
        except UF.DoesNotExist:
            return JsonResponse({'error':'date not found'}, status=404)
        price = uf.value * value
        return JsonResponse({'price': price})
    else:
        return JsonResponse({'error': 'only GET method allowed'}, status=400)

