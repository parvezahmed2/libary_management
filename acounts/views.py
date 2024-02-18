from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, ListView, DetailView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from books.models import Book
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserBankAccount
from books.models import BorroBook
# Create your views here.
 




# class Profile(TemplateView):
#     template_name = 'accounts/profile.html'
#     def get(self, request):
#         book_id = request.GET.get('id')
#         book = None
#         if book_id:
#             book = get_object_or_404(Book, id=book_id)
             
#         return render(request, 'accounts/profile.html', {'book': book})




class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    # context_object_name = 'user'

    def get_object(self, queryset=None):
        # Return the current logged-in user as the object
        return self.request.user


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrowing_history'] = BorroBook.objects.filter(user=self.request.user)
        context['transactions'] = UserBankAccount.objects.filter(user=self.request.user)
        return context

 







class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake 
    


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLgoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')




class UserAccountUpdateView(View):
    template_name = 'accounts/update_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('update_profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    


 