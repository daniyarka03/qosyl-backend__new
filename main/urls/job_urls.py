
from django.urls import path
from main.views import job_views as views


# Creating routes urls
urlpatterns = [
    path('', views.getJobs, name="jobs"),
    path('create/', views.addJob, name="add-job"),
    path('<str:pk>/delete/', views.deleteJob, name="delete-job"),
    path('<str:pk>/update/', views.updateJob, name="update-job"),
    path('<str:pk>', views.getJob, name="job"),
]