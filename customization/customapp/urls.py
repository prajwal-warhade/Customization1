from django.urls import path
from customapp import views
# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    path('about',views.about),
    path('Custom',views.Custom),
]
