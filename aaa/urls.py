from django.urls import path

from aaa import views

urlpatterns = [
    path('', views.index),
    path('ad/', views.AdsView.as_view()),
    path('ad/<int:pk>/', views.AdsDetailView.as_view()),
    path('ad/create/', views.AdsCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view()),
    path('cat/', views.CatView.as_view()),
    path('cat/<int:pk>/', views.CatDetailView.as_view()),
    path('cat/create/', views.CatCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CatDeleteView.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
]


# handler404 = pageNotFound