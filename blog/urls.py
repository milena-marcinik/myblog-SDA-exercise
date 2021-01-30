from django.urls import path

# import views
# from .views import main_page
from . import views

urlpatterns = [
    path('', views.main_page, name="blog_main_page"),
    path('send_email', views.send_email, name="send_email"),
    path('wpisy/', views.all_entries, name="all_entries"),
    path('wpisy/<int:entry_id>', views.show_entry, name="show_entry")
]