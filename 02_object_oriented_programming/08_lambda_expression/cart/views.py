# views.py
from django.shortcuts import render
from django.http import JsonResponse

# Sample products
PRODUCTS = [
    {'id': 1, 'name': 'Product A', 'price': 150},
    {'id': 2, 'name': 'Product B', 'price': 250},
    {'id': 3, 'name': 'Product C', 'price': 100},
]

def products_view(request):
    return render(request, 'product.html', {'products': PRODUCTS})

def calculate_total(request):
    # Receive selected product IDs and calculate the total
    selected_ids = request.GET.getlist('selected_ids[]')
    total = sum((lambda p: p['price'])(p) for p in PRODUCTS if str(p['id']) in selected_ids)
    return JsonResponse({'total': total})
