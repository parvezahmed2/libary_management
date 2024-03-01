"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books.views import BookListView, BuyNowView, ReturnView,   DetailbookView, DetailbookView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='home'),
    path('category/<slug:category_slug>/', BookListView.as_view(), name='category_wise_book'),
    path('buy/<int:id>/', BuyNowView.as_view(), name='buy'),
    path('return/<int:id>/', ReturnView.as_view(), name='return'),
    path('details/<int:id>/', DetailbookView.as_view(), name='details'),
    path('accounts/', include('acounts.urls')),
    path('transaction/', include('transactions.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
