
''' APIView '''
# # 데이터 처리 대상
# from post.models import Post
# from post.serializer import PostSerializer
# # status에 따라 직접 Response를 처리할 것
# from django.http import Http404 
# from rest_framework.response import Response
# from rest_framework import status
# # APIView를 상속받은 CBV
# from rest_framework.views import APIView
# # PostDetail 클래스의 get_object 메소드 대신 이거 써도 된다
# from django.shortcuts import get_object_or_404


# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True) # 쿼리셋 넘기기 (many=True인자)
#         return Response(serializer.data) # 직접 Response 리턴해주기 : serializer.data

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():   # 직접 유효성 검사
#             serializer.save()       # 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     '''
#     def delete(self, request):
#         pass
#     def put(self, request):
#         pass
#     '''
# # PostList 클래스와는 달리 pk값을 받음 (메소드에 pk인자)
# class PostDetail(APIView):

#     # get_object_or_404를 구현해주는 helper function
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         # post = get_object_or_404(Post, pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     # 위 post 메소드와 비슷비슷한 논리
#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

''' mixins '''
# # 데이터 처리 대상 : 모델, Serializer import 시키기
# from post.models import Post
# from post.serializer import PostSerializer

# from rest_framework import mixins
# from rest_framework import generics

# # mixin 직접 보기 : https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py
# # genericAPIView 직접 보기 : https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all() # 쿼리셋 등록!
#     serializer_class = PostSerializer # Serializer 클래스 등록!

#     # get은 list메소드를 내보내는 메소드
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # post는 create를 내보내는 메소드
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     # DetailView의 get은 retrieve를 내보내는 메소드
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     # put은 update를 내보내는 메소드
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     # delete는 destroy를 내보내는 메소드
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

''' generic Class Based Views '''
# from post.models import Post
# from post.serializer import PostSerializer
# from rest_framework import generics


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

''' ViewSet '''
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

# # ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능

# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")