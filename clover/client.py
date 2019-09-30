from clover.auth import Auth
from clover.api.merchant import Merchant
from clover.api.cash import Cash
from clover.api.customer import Customer
from clover.api.employee import Employee
from clover.api.inventory import Inventory
from clover.api.notification import Notification
from clover.api.order import Order
from clover.api.payment import Payment
from clover.api.app import App


class Client(object):
    def __init__(self, api_key, merchant_id, api_url):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = Auth(api_key=api_key)
        # Define s
        self.merchant = Merchant(self.auth, self.url, self.merchant_id)
        self.cash = Cash(self.auth, self.url, self.merchant_id)
        self.customer = Customer(self.auth, self.url, self.merchant_id)
        self.employee = Employee(self.auth, self.url, self.merchant_id)
        self.inventory = Inventory(self.auth, self.url, self.merchant_id)
        self.notification = Notification(self.auth, self.url, self.merchant_id)
        self.order = Order(self.auth, self.url, self.merchant_id)
        self.payment = Payment(self.auth, self.url, self.merchant_id)
        self.app = App(self.auth, self.url, self.merchant_id)
