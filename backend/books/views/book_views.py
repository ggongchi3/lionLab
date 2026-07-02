from rest_framework import filters, viewsets
from rest_framework.decorators import action  # 추가: 커스텀 엔드포인트
from rest_framework.response import Response  # 추가
from django.db.models import Min, Avg, Count  # 추가: 통계 계산
from ..models import Book
from ..serializers.book_serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'isbn', 'authors', 'publisher']
    ordering_fields = ['created_at', 'original_price', 'price']

    # 추가: 가격 비교 엔드포인트
    @action(detail=True, methods=['get'])
    def price_compare(self, request, pk=None):
        book = self.get_object()
        listings = book.listings.filter(status='available')

        if not listings.exists():
            return Response({
                'book_id': book.id,
                'title': book.title,
                'original_price': book.original_price,
                'listing_count': 0,
                'min_price': None,
                'avg_price': None,
                'max_discount_rate': 0,
            })

        stats = listings.aggregate(
            min_price=Min('price'),
            avg_price=Avg('price'),
            listing_count=Count('id'),
        )

        best_listing = min(listings, key=lambda l: l.price)

        return Response({
            'book_id': book.id,
            'title': book.title,
            'original_price': book.original_price,
            'listing_count': stats['listing_count'],
            'min_price': stats['min_price'],
            'avg_price': round(stats['avg_price']),
            'max_discount_rate': best_listing.discount_rate,
        })