from django.shortcuts import render
from ticket_search.models import UserProfile

# Create your views here.
def index(request):
    #people_offering = UserProfile.objects.filter(requesting=False)
    people_offering = UserProfile.objects.all()
    return render(request, 'ticket_search/index.html', {'people': people_offering})
