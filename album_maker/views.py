from django.shortcuts import render, redirect

from django.utils import timezone

from .models import Category, Album
from django.shortcuts import get_object_or_404
# Create your views here.


def gallery(request):
	category = request.GET.get('category')
	if category == None:
		photo = Album.objects.all()
	else:
		photo = Album.objects.filter(category__name=category)


	item = Category.objects.all()
	
	context = {'item': item, 'photo': photo}
	return render(request, 'album_maker/gallery.html', context)


def viewPhoto(request, pk):
	photo = Album.objects.get(id=pk)
	return render(request, 'album_maker/view_photo.html', {'photo': photo})


def addPhoto(request):
	categories = Category.objects.all()
	
	if request.method == 'POST':
		data = request.POST
		photo = request.FILES.get('image')

		# print('data:', data)
		# print('image:', photo)

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])
		elif data['new_category'] != '':
			category, created = Category.objects.get_or_create(name=data['new_category'])
		else:
			category = None

		photo = Album.objects.create(
				photo = photo,
				description = data['description'],
				category = category,

			)
		return redirect('gallery')

	context = {'categories': categories}
	return render(request, 'album_maker/add_photo.html', context)
	