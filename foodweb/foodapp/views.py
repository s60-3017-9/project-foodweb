from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Manu
# Create your views here.


def search(request):
    return render(request,'foodapp/search.html')

def show(request):
    try:
        r_list = Restaurant.objects.filter(type=request.POST['t_food'])
    except(KeyError):
        return render(request, 'foodapp/search.html')
    else:
        context ={'list_name_r':r_list}
        return render(request, 'foodapp/search.html',context)

def detail(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {'restaurant':restaurant}
    return render(request, 'foodapp/detail.html',context)