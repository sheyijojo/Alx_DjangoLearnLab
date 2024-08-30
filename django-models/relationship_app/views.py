from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book, UserProfile
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from core.mixins import RoleCheckMixin



# Create your views here.
## create a function-based view
def list_books(request):
      books = Book.objects.all()
      
      return render(request, 'list_books.html',{'books':books} )

##Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.


class LibraryDetailView(DetailView):
      model = Library
      context_object_name = 'library_view'
      template_name = 'relationship/library_details.html'

## create a user registration form in form.py and reference it in the registration view here
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

"""
For User registration, is either i use Createview class that does a lot of stuff lile validity
or use a function like below
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('profile')  # Redirect to the profile page or another page
    else:
        form = RegistrationForm()
    return render(request, 'registration/accounts/register.html', {'form': form})

"""

## Create three separate views to manage content access based on user roles:
## admin. librarian, member

class AdminView(RoleCheckMixin, TemplateView):
    template_name = 'admin_dashboard.html'
    role_required = 'Admin'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




class AdminView(RoleCheckMixin, TemplateView):
    template_name = 'admin_view.html'
    role_required = 'Admin'

    def admin_view(user):
        return user.is_authenticated and user.userprofile.role == "Admin"
    
    @login_required
    @user_passes_test(admin_view)
    def admin_dashboard(request):
        return render(request, 'admin_view')


    def librarian_check(user):
     return user.is_authenticated and user.userprofile.role == "lbrarian"
def member_check(user):
     return user.is_authenticated and user.userprofile.role == "Member"



@login_required
@user_passes_test(librarian_check)
def librarian_dashboard(request):
    return render(request, 'librarian_view')

@login_required
@user_passes_test(member_check)
def member_dashboard(request):
    return render(request, 'member_view')