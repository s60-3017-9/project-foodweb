from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Menu
# Create your views here.


def search_restaurant(request):
    return render(request,'foodapp/search_restaurant.html')

def show_restaurant(request):
    try:
        r_list = Restaurant.objects.filter(type=request.POST['t_food'])
    except(KeyError):
        return render(request, 'foodapp/search_restaurant.html')
    else:
        context ={'list_name_r':r_list}
        return render(request, 'foodapp/search_restaurant.html',context)

def detail_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {'restaurant':restaurant}
    return render(request, 'foodapp/detail_restaurant.html',context)


