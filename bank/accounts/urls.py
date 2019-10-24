from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:id>/', views.account_detail),
]
