from django.urls import path
from . import views

app_name = "BeReady"

urlpatterns = [
    path("", views.home, name="home"),
    path("HR/", views.view_hr, name="view_hr"),
    path("Profile/", views.profile, name="profile"),
    path("HR/Profile/<int:user_id>/", views.profile_detail, name="profile_detail"),
    path("comment/<user_id>/", views.add_comment, name="comment"),

    path("HR/<int:user_id>/appointment/", views.appointment, name="appointment"), 
    path("add/appointment/<int:user_id>/", views.add_appointment, name="add_appointment"),

    path("BeReady/About", views.about, name="about"),
    path("BeReady/Contact", views.contact, name="contact"),

]

