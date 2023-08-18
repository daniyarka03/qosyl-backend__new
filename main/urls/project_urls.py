
from django.urls import path
from main.views import project_views as views


# Creating routes urls
urlpatterns = [
    path('', views.getProjects, name="projects"),

    # path('posts/delete/<int:pk>', views.deletePost, name="delete-post"),
    # path('posts/update/<int:pk>', views.updatePost, name="update-post"),
    #path('products/', views.getProducts, name="products"),
    #path('products/<str:pk>/', views.getProduct, name="product"),
    #path('projects/', views.getProjects, name="projects"),
]