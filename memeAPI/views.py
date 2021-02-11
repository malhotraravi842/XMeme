from dashboard.models import Meme
from .serializers import MemeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'PUT', 'PATCH'])
def meme_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Meme.objects.get(pk=pk)
    except Meme.DoesNotExist:
        content = {'status_code' : status.HTTP_404_NOT_FOUND, 'detail' : 'Requested object is not available'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemeSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemeSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        meme_object = Meme.objects.get(pk=pk)
        data = request.data
        meme_object.caption = data.get('caption', meme_object.caption)
        meme_object.url = data.get('url', meme_object.url)
        meme_object.save()
        serializer = MemeSerializers(meme_object)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def meme_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets =  Meme.objects.all()
        serializer = MemeSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)