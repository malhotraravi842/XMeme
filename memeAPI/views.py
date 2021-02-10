from django.db.models.query import QuerySet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from dashboard.models import Meme
from .serializers import MemeSerializers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class MemeViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = MemeSerializers
    queryset = Meme.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Original Response (inside the `CreateModelMixin` class)
        # return Response(
        #     serializer.data, 
        #     status=status.HTTP_201_CREATED, 
        #     headers=headers
        # )

        # We will replace the original response with this line 
        return Response(
            {'id': serializer.data.get('id')},
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

    def get(self, request, *args, **kwargs):
        response =  self.retrieve(request, *args, **kwargs)
        return response

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)