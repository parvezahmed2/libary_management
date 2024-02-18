from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView, FormView
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Book, BorroBook, Category, Review
from acounts.models import UserBankAccount
from .forms import  CommentForm, BorrowBookForm
from django.contrib import messages 
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


 

class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


 

    


@method_decorator(login_required, name='dispatch')
class BuyNowView(View):
    def get(self, request, id):
        user = request.user
        book = get_object_or_404(Book, id=id)
       
         
        if  request.user.account.balance >= book.borrowing_price:
            request.user.account.balance -= book.borrowing_price
            request.user.account.save()
            book.buy_book = True
            book.balace_after = request.user.accout.balance
            book.save()
            BorroBook.objects.create(user=user, book=book)
            return redirect('details', id=id)
        
        else:
            return redirect('details', id=id)




@method_decorator(login_required, name='dispatch')
class ReturnView(View):
    def get(self, request, id):
        user = request.user
        book = get_object_or_404(Book, id=id)
        borro_book = get_object_or_404(BorroBook, id=id)
       
        
        request.user.account.balance += book.borrowing_price
        request.user.account.save()
        book.buy_book = True
        book.balace_after = 0
        book.save()
        borro_book.delete()
        return redirect('profile')
        
         


 

 
 



 

class DetailbookView(DetailView):
    model =  Book
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'

    def post(self, request, *args, **kwargs):
        comment_form =CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post 
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object   # post model er object  ekhane store korlam 
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments']  = comments
        context['comment_form'] = comment_form
        return context  




# class DetailbookView(FormMixin, DetailView):
#     model = Book
#     template_name = 'book_detail.html'
#     context_object_name = 'book'
#     form_class = CommentForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = Review.objects.filter(book=self.object)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         rating = form.cleaned_data['rating']
#         comment = form.cleaned_data['comment']
#         Review.objects.create(user=self.request.user, book=self.object, comment=comment)
#         return super().form_valid(form)

#     def get_success_url(self):
#         return self.request.path








 