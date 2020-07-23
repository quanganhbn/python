from django.shortcuts import render

# Create your views here.
def me(request):
    return render(request, 'jobs/me.html')