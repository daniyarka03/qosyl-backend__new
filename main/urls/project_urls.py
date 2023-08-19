
from django.urls import path
from main.views import project_views as views


# Creating routes urls
urlpatterns = [
    path('', views.getProjects, name="projects"),
    path('create/', views.createProject, name="add-project"),
    path('<str:pk>/update/', views.updateProject, name="update-project"),
    path('<str:pk>/', views.getProject, name="delete-project"),
    path('<str:pk>/delete/', views.deleteProject, name="delete-project"),
    # path('posts/delete/<int:pk>', views.deletePost, name="delete-post"),
    # path('posts/update/<int:pk>', views.updatePost, name="update-post"),
    #path('products/', views.getProducts, name="products"),
    #path('products/<str:pk>/', views.getProduct, name="product"),
    #path('projects/', views.getProjects, name="projects"),
]