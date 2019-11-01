from django.shortcuts import render
from .models import PostProd



# Create your views here.
#series1
def GetView(request):
	page = PostProd.objects.all()
	context = {
	'page': page
	}
	return render(request, 'style.html', context)

