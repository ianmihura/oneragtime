from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime

from .models import Bills
from investments.models import Investments
from investors.models import Investors
from .serializers import BillSerializer


class BillListAPIView(generics.ListAPIView):
    """
    List all bills
    """
    queryset = Bills.objects.all()
    serializer_class = BillSerializer


class BillCreateAPIView(generics.CreateAPIView):
    """
    Create bills for an investor_id
    """
    queryset = Bills.objects.all()
    serializer_class = BillSerializer

    def get_investment_bill(self, investment):
        """
        Returns bill dict based on investment fees
        Used to create bill with BillSerializer
        """
        april_2019 = datetime(year=2019, month=4, day=1)
        # tm_yday_percentage is % of year that has passed, at time of investment
        tm_yday_percentage = (
            365 - investment.date_added.timetuple().tm_yday) / 365
        # base_fee is fee * invested_amount
        base_fee = (investment.percentage_fees / 100) * \
            investment.invested_amount

        if investment.fees_type == 'upfront':
            # Upfront payment will be payed this year
            # Other years are already filtered out
            fees_amount = base_fee * 5

        elif investment.date_added.replace(tzinfo=None) < april_2019:
            # Yearly payment based on pre-2019
            if investment.date_added.year == datetime.now().year:
                # First year (won't happen)
                fees_amount = base_fee * tm_yday_percentage
            else:
                # Other years
                fees_amount = base_fee

        elif investment.date_added.replace(tzinfo=None) >= april_2019:
            # Yearly payment based on post-2019
            if investment.date_added.year == datetime.now().year:
                # First year
                fees_amount = base_fee * tm_yday_percentage
            elif investment.date_added.year == datetime.now().year - 1:
                # Second year
                fees_amount = base_fee
            elif investment.date_added.year == datetime.now().year - 2:
                # Third year
                fees_amount = (
                    (investment.percentage_fees - 0.2) / 100) * investment.invested_amount
            elif investment.date_added.year == datetime.now().year - 3:
                # Fourth year
                fees_amount = (
                    (investment.percentage_fees - 0.5) / 100) * investment.invested_amount
            else:
                # Following years
                fees_amount = ((investment.percentage_fees - 1) /
                               100) * investment.invested_amount

        return {
            "investor_id": investment.investor_id,
            "investment_id": investment.id,
            "fees_amount": round(fees_amount, 2),
            "date_added": investment.date_added,
            "fees_type": investment.fees_type,
        }

    def get_investor_bill(self, investor):
        """
        Returns bill dict based on investor membership
        Used to create bill with BillSerializer
        """
        return {
            "investor_id": investor.id,
            "investment_id": None,
            "fees_amount": 3000,
            "date_added": datetime.now(),
            "fees_type": "membership",
        }

    def investor_is_exempt(self, id):
        """
        Returns True if investor is exempt of membership fee in current year
        (given they invested over 50_000)
        Returns False otherwise
        """
        investors = Investments.objects.all().values('investor_id').annotate(
            total=Sum('invested_amount')).filter(
            date_added__gte=datetime.now().replace(month=1, day=1))
        try:
            return investors.get(investor_id=id)['total'] > 50_000
        except BaseException:
            return False

    def post(self, request, *args, **kwargs):
        # get investment bills (yearly & upfront)
        data = [self.get_investment_bill(x) for x in Investments.objects.all()
                if not (x.date_added.year < datetime.now().year and x.fees_type == 'upfront')]

        # get investor bills (membership fees)
        data = data + [self.get_investor_bill(x) for x in Investors.objects.all()
                       if not self.investor_is_exempt(x.id)]

        serializer = self.get_serializer(data=data, many=True)

        # default code of generic view
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BillInvestorAPIView(generics.ListAPIView):
    """
    Filters bills for an investor_id
    """
    queryset = Bills.objects.all()
    serializer_class = BillSerializer

    def get(self, request, *args, **kwargs):
        queryset = Bills.objects.filter(investor_id=kwargs['investor_id'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
