from django.urls import path
from . import views
from .views import list_books
from .views import admin_view, member_view, library_view, home
from django.views.generic import TemplateView
from relationship_app.views import SignUpView
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('', home, name='home'), 
    path('library/<int:pk>/',views.LibraryDetailView.as_view(), name="library_view" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path("register/", SignUpView.as_view(template_name="relationship_app/register.html"), name="templates/relationship_app/register"),
   # path("register/", views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    
]
urlpatterns = [
   path('admin-view/', admin_view, name='admin_view'),
   path('member-view', member_view , name='member_view'),
   path('library-view', library_view, name='library_view'),
]

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'), 
]