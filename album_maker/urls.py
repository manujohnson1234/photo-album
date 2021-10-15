from django.urls import path

from . import views


urlpatterns = [

	path('', views.gallery, name='gallery'),
	path('view/<str:pk>', views.viewPhoto, name='view_photo'),
	path('add_photo', views.addPhoto, name='add_photo'),
]