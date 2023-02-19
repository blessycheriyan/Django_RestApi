
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer
# # def homepage(request:HttpRequest):
    
# #     response={"message": "Welcome to Django bless"}
# #     return JsonResponse(data=response,status=status.HTTP_200_OK)
    
# @api_view(http_method_names=["GET","POST"])
# def homepage(request:Request):
#     if request.method == "POST":
#         data=request.data
#         response={"message": "Welcome to Django bless","data": data}
#         return Response(data=response,status=status.HTTP_201_CREATED)
        
#     response={"message": "Welcome to Django bless"}
#     return Response(data=response,status=status.HTTP_200_OK)
     
# @api_view(http_method_names=["GET","POST"])
# def list_posts(request:Request):
#     posts=Post.objects.all()
#     if request.method == "POST":
#         data=request.data
#         serializer=PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response={
#                 "message": "Posts Created successfully",
#                 "data": serializer.data
#                 }
#             return Response(data=response,status=status.HTTP_200_OK)    
#         return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)    
    
#     serializer=PostSerializer(instance=posts,many=True)
#     response={
#         "message": "posts",
#         "data": serializer.data
#         }
#     return Response(data=response,status=status.HTTP_200_OK)    

# @api_view(http_method_names=["GET"])
# def post_details(request:Request,post_id:int):
#     post=get_object_or_404(Post,pk=post_id)
   
#     serializer=PostSerializer(instance=post)
#     response={
#         "message": "posts",
#         "data": serializer.data
#         }
#     return Response(data=response,status=status.HTTP_200_OK)  

# @api_view(http_method_names=["PUT"])
# def post_update(request:Request,post_id:int):
#         post=get_object_or_404(Post,pk=post_id)

#         data=request.data
#         serializer=PostSerializer(instance=post,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response={
#                 "message": "Posts Updated successfully",
#                 "data": serializer.data
#                 }
#             return Response(data=response,status=status.HTTP_200_OK)    
#         return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)    
    
 

# @api_view(http_method_names=["DELETE"])
# def post_delete(request:Request,post_id:int):
#         post=get_object_or_404(Post,pk=post_id)

#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    

#  url
 
#  path("update/<int:post_id>/", views.post_update, name="post_update"),
#     path("delete/<int:post_id>/", views.post_delete, name="post_delete"),       



     
# class PostListCreateView(APIView):
#     serializer_class = PostSerializer
#     def get(self, request, *args, **kwargs):
#             post=Post.objects.all()
#             serializer=self.serializer_class(instance=post,many=True)
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
        
#     def post(self, request, *args, **kwargs):
#             data=request.data    
#             serializer=self.serializer_class(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 response={
#                     "message": "Posts Created successfully",
#                     "data": serializer.data
#                     }
#                 return Response(data=response,status=status.HTTP_200_OK)    
#             return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)    
    
 
      
# class PostRetrieveUpdateView(APIView):
#     serializer_class = PostSerializer
    
#     def get(self, request:Request,post_id:int):
#          post=get_object_or_404(Post,pk=post_id)
#          serializer=self.serializer_class(instance=post)
#          return Response(data=serializer.data,status=status.HTTP_200_OK)    
         
#     def put(self, request:Request,post_id:int):   
#            post=get_object_or_404(Post,pk=post_id)
#            data =request.data
#            serializer=self.serializer_class(instance=post,data=data)
#            if serializer.is_valid():
#                 serializer.save()
#                 response={"message": "Posts Updated successfully","data": serializer.data}
#                 return Response(data=response,status=status.HTTP_200_OK)    
#            return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)    
    
#     def delete(self, request:Request,post_id:int):   
#            post=get_object_or_404(Post,pk=post_id)
#            post.delete()
#            return Response(status=status.HTTP_204_NO_CONTENT)    
           
 