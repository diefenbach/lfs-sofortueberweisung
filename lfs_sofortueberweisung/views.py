# django imports
from django.conf import settings

# lfs imports
from lfs.cart.utils import get_cart
from lfs.plugins import PaymentMethod
from lfs.plugins import PM_ORDER_IMMEDIATELY
from lfs.plugins import PM_STATE_ACCEPTED


class SofortUeberweisungPaymentMethod(PaymentMethod):
    """
    Provides payment processment with sofortueberweisung.de.
    """
    def process(self, request, cart=None, order=None):
        return {
            "state": PM_STATE_ACCEPTED,
            "redirect_to": "https://www.sofortueberweisung.de/payment/start?user_id=%s&project_id=%s&reason_1=Project&reason_2=Test&amount=%s&currency=EUR" % \
                (settings.SOFORTUEBERWEISUNG_USERID, settings.SOFORTUEBERWEISUNG_PROJECT_ID, order.price)
        }

    def get_pay_link(self, order):
        return "https://www.sofortueberweisung.de/payment/start?user_id=48879&project_id=119215&reason_1=Project&reason_2=Test&amount=1.00&currency=EUR"

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY
