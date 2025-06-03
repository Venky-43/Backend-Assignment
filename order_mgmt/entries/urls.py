from django.urls import path
from .views import GoogleOAuthView, EntryCreateView, EntryListView

urlpatterns = [
    path('oauth/', GoogleOAuthView.as_view()),
    path('entries/', EntryCreateView.as_view()),
    path('entries/list/', EntryListView.as_view()),
]
