import ccxt
import traceback

api_key = 'YOURAPI'
api_secret = 'YOURAPISECRET'

try:
    #setBybit
    exchange = ccxt.bybit({
        'apiKey': api_key,
        'secret': api_secret,
    })

    exchange.set_sandbox_mode(True)

    exchange.create_order(symbol="BTC/USDT:USDT",type="market",side="sell",amount=0.001)

except:
    print("エラー\n" + traceback.format_exc())