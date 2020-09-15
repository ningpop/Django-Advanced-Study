from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')
    # 어떤 칼럼을 기준으로 검색을 할 건지 -> 튜플

    def get_queryset(self):
        # 여기 내부에서 쿼리셋을 지지고 볶은 다음에
        qs = super().get_queryset()
        
        # .filter .exclude
        # qs = qs.filter(author__id = 2)
        
        # 만약 로그인이 안되어있다면 -> 비어있는 쿼리넷을 리턴해라
        if self.request.user.is_authenticated:
            # 지금 만약 로그인이 되어있자면 -> 로그인한 유저의 글만 필터링 해라
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        
        return qs