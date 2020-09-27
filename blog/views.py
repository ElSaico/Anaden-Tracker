from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from users.api.fishing.models import Fish


def home(request):
    return render(request, 'blog/home.html')


def legal(request):
    return render(request, 'blog/legal.html')


@login_required
def fishing(request):
    context = {
        'fishes': Fish.objects.filter(user=request.user),
        'caught': Fish.objects.filter(user=request.user).aggregate(fishes=Sum('actual_catch')),
        'stones': Fish.objects.filter(user=request.user).aggregate(total=Sum('stones')),
        'dimension_hook': Fish.objects.filter(user=request.user).aggregate(until=(1215 - Sum('stones'))),
        'c_stones': Fish.objects.filter(user=request.user).aggregate(total=Sum('c_stones')),
    }
    return render(request, 'fishing/fishing.html', context)


def test_view(request):
    current_user = request.user
    context = {'username': current_user.username,
               'current_user': current_user}
    return render(request, 'home.html', context)
