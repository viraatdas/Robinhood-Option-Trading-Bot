from Robinhood import Robinhood
from config import username, password, QR

my_trader = Robinhood()
my_trader.login(username=username, password=password, qr_code=QR)
