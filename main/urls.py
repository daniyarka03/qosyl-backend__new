
from django.urls import path
from . import views


# Creating routes urls
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('posts/', views.getPosts, name="posts"),
    path('posts/create/', views.addPost, name="add-post"),
    path('projects/', views.getProjects, name="projects"),
    path('example/', views.example_view, name='example'),
    path('login/', views.get_user_data, name='get_user_data'),

    # path('posts/delete/<int:pk>', views.deletePost, name="delete-post"),
    # path('posts/update/<int:pk>', views.updatePost, name="update-post"),
    #path('products/', views.getProducts, name="products"),
    #path('products/<str:pk>/', views.getProduct, name="product"),
    #path('projects/', views.getProjects, name="projects"),
]