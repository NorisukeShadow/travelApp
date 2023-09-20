from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path("test/", views.TestView.as_view(), name="test"),
    path("form/", views.FormView.as_view(), name="form"),
    path('schedule/', views.scheduleView.as_view(), name='schedule'),
    path('resultPlace/', views.resultPlaceView.as_view(), name='resultPlace'),
    path('resultPerson/', views.resultPersonView.as_view(), name='resultPerson'),
]
