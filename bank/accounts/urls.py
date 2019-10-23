from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.accounts_list),
    path('accounts/<int:id>/', views.accounts_detail),
]
