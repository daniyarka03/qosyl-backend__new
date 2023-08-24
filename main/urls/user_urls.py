
from django.urls import path
from main.views import user_views as views


# Creating routes urls
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name="register"),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/edit/', views.updateUser, name="update-profile"),
    path('profile/delete/', views.deleteUser, name="delete-profile"),
    path('<str:pk>/', views.getUser, name="user-info"),
    path('', views.getUsers, name="users"),

    # path('posts/delete/<int:pk>', views.deletePost, name="delete-post"),
    # path('posts/update/<int:pk>', views.updatePost, name="update-post"),
    #path('products/', views.getProducts, name="products"),
    #path('products/<str:pk>/', views.getProduct, name="product"),
    #path('projects/', views.getProjects, name="projects"),
]