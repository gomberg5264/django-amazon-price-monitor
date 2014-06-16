from price_monitor.api.serializers.PriceSerializer import PriceSerializer
from price_monitor.models.Price import Price

from rest_framework.generics import ListAPIView


class PriceListView(ListAPIView):
    model = Price
    serializer_class = PriceSerializer

    def get_queryset(self):
        queryset = super(PriceListView, self).get_queryset()
        return queryset.filter(product__asin=self.kwargs.get('asin'))
