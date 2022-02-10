from django.shortcuts import render

# Create your views here.
rooms =[
    {'id' : 1,'name' : 'Samir'},
    {'id' : 2,'name' : 'Souad'},
    {'id' : 3,'name' : 'Hamid'},
]
def home(request):
 return render(request, 'home.html')

def room(request):
 return render(request, 'room.html', {'roomss':rooms})
