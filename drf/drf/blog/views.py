# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from rest_framework import serializers
from blog.serializer import PostSerializer

class PostView(APIView):

    def post(self,request):
        post_data = {}
        if 'author' not in request.data:
            return Response(data={"error": "Author name must be provided", "success": False},
                            status=status.HTTP_400_BAD_REQUEST)
        p = Post()
        p.author = request.data['author']
        p.text   = request.data['text']
        p.title  = request.data['title']
        response = p.publish(request.data)
        response = PostSerializer(response)
        print response.data
        return Response(data={"data": response.data,"success": True}, status=status.HTTP_200_OK)

    def get(self, request):
        # p = Post()

        res = Post.objects.all()
        response = PostSerializer(res, many=True)

        return Response(data={"data": response.data,"success": True}, status=status.HTTP_200_OK)


class SinglePostView(APIView):
    def get(self, request, post_id):
        res = Post.objects.get(id=15)
        response = PostSerializer(res)
        return Response(data= {"data": response.data, "success": True}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.title = request.data['title'];
        post.save()
        response = PostSerializer(post)
        return Response(data={"data":response.data,"success": True}, status=status.HTTP_200_OK)

    def delete(self,request, post_id):
        print post_id
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return Response(data={'data': "Post successfully deleted", "success": True}, status=status.HTTP_200_OK)
        except:
            return Response(data={'data': "No post is found with id", "success": True}, status=status.HTTP_200_OK)
