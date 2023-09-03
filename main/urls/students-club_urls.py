
from django.urls import path
from main.views import student_club_views as views


# Creating routes urls
urlpatterns = [
    path('', views.getStudentsClubs, name="clubs"),
    path('create/', views.addStudentsClub, name="add-club"),
    path('<str:pk>/delete/', views.deleteStudentsClub, name="delete-club"),
    path('<str:pk>/update/', views.updateStudentsClub, name="update-club"),
    path('<str:pk>', views.getStudentsClub, name="club"),
]