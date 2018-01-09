from django.shortcuts import render
from .models import Owner, Pet

# Create your views here.
def index(request):
	# jeff = Owner.objects.get(id=1)
	# print jeff.pets.all()
	return render(request, "pets_app/index.html", {"pets": Pet.objects.all(), "owners": Owner.objects.all()})