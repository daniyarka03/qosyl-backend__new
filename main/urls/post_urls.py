
from django.urls import path
from main.views import posts_views as views


# Creating routes urls
urlpatterns = [
    path('', views.getPosts, name="posts"),
    path('create/', views.addPost, name="add-post"),
    path('<str:pk>/delete/', views.deletePost, name="delete-post"),
    path('<str:pk>/update/', views.updatePost, name="update-post"),
    path('<str:pk>', views.getPost, name="post"),


    # path('posts/delete/<int:pk>', views.deletePost, name="delete-post"),
    # path('posts/update/<int:pk>', views.updatePost, name="update-post"),
    #path('products/', views.getProducts, name="products"),
    #path('products/<str:pk>/', views.getProduct, name="product"),
    #path('projects/', views.getProjects, name="projects"),
]