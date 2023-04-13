from .views import *
from django.urls import path


urlpatterns = [
	path('', menu, name='menu'),
	path('create/', create, name='create'),
	path('about_us/', about_us, name='about_us'),
	path('contact/', contact, name='contact'),
	path('pinterest/', pinterest, name='pinterest'),
	path('search/', search, name='search'),
	path('rubric/<int:rubric_id>', rubrics),
	path('chanel/', chanels, name='chanels'),
	path('<int:pk>', details.as_view(), name='deteil'),
	path('<int:pk>/delete/', deletes),
]