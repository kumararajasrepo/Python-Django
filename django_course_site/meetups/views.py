from django.shortcuts import render

# Create your views here.
def index(request):
    meetups=[
        {'title': 'A first meetup'},
        {'title': 'A second meetup'}        
    ]
    return render(request,'meetups/index.html',{
        'show_meetups':True,
        'meetups':meetups
    })
