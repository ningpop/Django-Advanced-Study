from rest_framework.pagination import PageNumberPagination

# 이 뷰에서만 적용한 페이지네이션 클래스
class MyPagination(PageNumberPagination):
    page_size = 5