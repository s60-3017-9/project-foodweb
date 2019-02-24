from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Menu,Reviews
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
# Create your views here.


def search_restaurant(request):
    return render(request,'foodapp/search_restaurant.html')

def show_restaurant(request):
    try:
        if request.GET['text_input']=="":
        # return render(request, 'foodapp/search_restaurant.html')
            try:
                r_list = Restaurant.objects.filter(type=request.GET['t_food'])
                context = {'list_name_r': r_list}
                return render(request, 'foodapp/search_restaurant.html', context)
            except(KeyError):
                context = {'error':'ใส่ข้อมูลร้าน'}
                return render(request, 'foodapp/search_restaurant.html',context)
        else:
            try:
                r_list = Restaurant.objects.filter(name__startswith=request.GET['text_input'],type=request.GET['t_food'])
                context = {'list_name_r': r_list}
                return render(request, 'foodapp/search_restaurant.html', context)
            except (KeyError,UnboundLocalError):
                r_list = Restaurant.objects.filter(name__startswith=request.GET['text_input'])
                if len(r_list)==0:
                    context = {'error': "ไม่พบรายชื่อร้านที่ค้นหา"}
                    return render(request, 'foodapp/search_restaurant.html', context)
                else:
                    context = {'list_name_r': r_list}
                    return render(request, 'foodapp/search_restaurant.html', context)
    except (KeyError):
        return render(request, 'foodapp/search_restaurant.html')

def detail_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {'restaurant': restaurant,'restaurant_reviews':restaurant.reviews_set.all().order_by('-review_date')}
    return render(request, 'foodapp/detail_restaurant.html', context)

def reviwe_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.POST["review"]=="":
        context = {'restaurant': restaurant,'error':'ใส่ข้อความรีวิว','restaurant_reviews':restaurant.reviews_set.all().order_by('-review_date')}
        return render(request, 'foodapp/detail_restaurant.html', context)
    else:
        try:
            restaurant.reviews_set.create(reviews_text=request.POST["review"], point=int(request.POST["point"]),review_date=timezone.now())
            return HttpResponseRedirect(reverse('food:detail_res', args=str(restaurant.id)))
        except (KeyError):
            context = {'restaurant': restaurant, 'error': 'ใส่คะแนนรีวิว','restaurant_reviews':restaurant.reviews_set.all().order_by('-review_date')}
            return render(request, 'foodapp/detail_restaurant.html', context)



