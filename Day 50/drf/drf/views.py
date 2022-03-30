from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, requests, *args, **kwargs):
        data = {
            'username': 'admin',
            'years_active': 10,
        }
        return Response(data)