from django.urls import path
from Guarantor import views


urlpatterns = [
    path('show_all_request/<str:id>', views.show_all_re, name="show_all_request"),
    path('have_request/<str:id>', views.have_request, name="have_request"),
    path('save/<str:id>/<str:ide>', views.savee, name="save"),

]
