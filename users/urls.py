from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.detail import DetailView
from .views import HomeListView, SignUpView, PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
urlpatterns=[
  path('post/<int:pk>/delete/', PageDeleteView.as_view(), name='post_delete'),
  path('post/<int:pk>/edit/', PageUpdateView.as_view(), name='post_edit'),
  path('post/new/', PageCreateView.as_view(), name='post_new'),
  path('post/<int:pk>/', PageDetailView.as_view(), name='post_detail'),
  path('pages/', PageListView.as_view(), name='pages'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('', HomeListView.as_view(), name='home'),
  
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)