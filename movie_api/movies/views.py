from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import GenreSerializer
from .models import Genre, Movie, Comment
from .serializers import MovieSerializer, MovieListSerializer, GenreListSerializer, CommentSerializer,CommentListSerializer

# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse


# Create your views here.
API_KEY = '611b17e08929eff3b420b33f2d24c4bb'

@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    print(genre)
    movies = Movie.objects.filter(genres_ids=genre).all()
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

@api_view(['DELETE'])
def delete_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return Response(status=200)

@api_view(['PUT'])
def modify_movie(request, movie_pk):
    movie =  get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

def like(request):
    pass

@api_view(['GET'])
def get_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_genre(request):
    serializer = GenreListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)
    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def delete_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    genre.delete()
    return Response(status=200)
    

@api_view(['PUT'])
def modify_genre(request, genre_pk):
    genre =  get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreListSerializer(genre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)


@api_view(['POST'])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        serializer.save(movie_id=movie, user=user)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_comments(request,movie_pk):
    comments = Comment.objects.filter(movie_id=movie_pk).all()
    serializer = CommentListSerializer(comments,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_comment(reqeust, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=200)