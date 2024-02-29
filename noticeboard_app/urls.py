from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="postlist"), 
    path('<int:pk>', PostDetail.as_view(), name="postdetail"),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('comments/', CommentList.as_view(), name="commentlist"),
    path('comments/<int:pk>', CommentDetail.as_view(), name='commentdetail'),
    path('comments/create/', CommentCreate.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
    path('comments/<int:pk>/accept/', accept_comment, name='accept_comment'),
    path('comments/<int:pk>/reject/', reject_comment, name='reject_comment'),
    path('comments/<int:pk>/reset/', reset_comment_status, name='reset_comment_status'),
    path('userpage/', UserPage.as_view(), name="userpage"),
    path("error403/", error403, name="error403"),
]
