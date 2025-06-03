import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer

class GoogleOAuthView(APIView):
    """
    Exchange Google OAuth authorization code for access tokens.
    """
    def post(self, request):
        code = request.data.get("code")
        redirect_uri = request.data.get("redirect_uri")

        if not code or not redirect_uri:
            return Response(
                {"error": "Both 'code' and 'redirect_uri' are required."},
                status=400,
            )

        data = {
            'code': code,
            'client_id': os.getenv("GOOGLE_CLIENT_ID"),
            'client_secret': os.getenv("GOOGLE_CLIENT_SECRET"),
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code'
        }

        token_response = requests.post('https://oauth2.googleapis.com/token', data=data)

        return Response(token_response.json(), status=token_response.status_code)

class EntryCreateView(generics.CreateAPIView):
    """
    Create a new Entry associated with the authenticated user.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EntryListView(generics.ListAPIView):
    """
    List Entries filtered by the authenticated user and optional title query param.
    """
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        title = self.request.query_params.get('title')
        queryset = Entry.objects.filter(user=self.request.user)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
