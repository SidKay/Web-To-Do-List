from . import views
from django.urls import path

app_name = 'todolist'
urlpatterns = [
	# Displays all available lists.
	path('', views.index, name='index'),

	# Displays a specified list and it's contents.
	path('<int:list_id>/', views.display_list, name='display-list'),
]