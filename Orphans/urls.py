from django.urls import path
from Orphans import views


urlpatterns = [
    path('add_request/<str:id>', views.add_req, name="add_request"),
    path('activities_or/<str:id>', views.ac_or, name="activities_or"),
    path('show_request/<str:id>', views.show_re, name="show_request"),

]
