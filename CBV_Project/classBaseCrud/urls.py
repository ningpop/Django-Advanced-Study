from django.urls import path
from . import views

# path함수는 두번째 인자로 함수를 받으므로 클래스이름.as_view()를 넣어줌
urlpatterns = [
    path('', views.BlogView.as_view(), name='list'),
    path('newblog/', views.BlogCreate.as_view(), name='create'),
    path('detail/<int:pk>', views.BlogRead.as_view(), name='read'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='delete'),
]