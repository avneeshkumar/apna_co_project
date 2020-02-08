from django.urls import path
from friend_connection.Views import AllFriendList, UserFriendList, FillDataBase

urlpatterns = [
    path('friends/', AllFriendList.AllFriendList.as_view()),
    path('createdummy/', FillDataBase.FillDataBase.as_view()),
    path('friends/<int:friend_id>', UserFriendList.UserFriendList.as_view()),

    #path('snippets/<int:pk>/', views.snippet_detail),
]