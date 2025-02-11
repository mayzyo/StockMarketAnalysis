# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # 需求描述
# 1. 国家是否扶持
#     * 找industry (boolean)
#     * 更改后续权重
# 3. 市净率
#     * 小于20%
# 4. 是否盈利
#     * 是
# 5. 找市值
#     * 超过100亿
#     * 不看超过2500
# %% [markdown]
# ## 国家是否扶持

# %%
def industry_check(stock, dict, ind=['Electronic Components', 'Metal Fabrication']):
    dict['industry'] = stock.info['industry']
    return stock.info['industry'] in ind

# %% [markdown]
# ## 市净率 (P/B Ratio)

# %%
def pb_check(stock, dict, cutoff=20):
    if 'priceToBook' in stock.info:
        dict['priceToBook'] = stock.info['priceToBook']
        return stock.info['priceToBook'] < cutoff
    else:
        print('错误：数据源未提供市净率')
        return False

# %% [markdown]
# ## 是否盈利

# %%
def profitable_check(stock, dict, key='profitMargins'):
    if key in stock.info:
        dict[key] = stock.info[key]
        return stock.info[key]
    else:
        print('错误：数据源未提供盈利数据')
        return False

# %% [markdown]
# ## 找市值

# %%
import math

def cap_check(stock, dict, min=100, max=2500):
    yi = math.pow(10, 8) # 一亿
    if 'marketCap' in stock.info:
        dict['marketCap'] = stock.info['marketCap'] / yi
        return (stock.info['marketCap'] >= min * yi) & (stock.info['marketCap'] <= max * yi)
    else:
        print('错误：数据源未提供市值')
        return False


# %%
# 基础分析
import yfinance as yf

def fundamental(ticker, debug=False):
    stock = yf.Ticker(ticker)
    out = { 'ok': True }
    # if industry_check(stock, out) == False:
    #     if debug: print('产业不符合条件')
    #     out['ok'] = False
    if pb_check(stock, out) == False:
        if debug: print('市净率不符合条件')
        out['ok'] = False
    elif profitable_check(stock, out) == False:
        if debug: print('当前未盈利')
        out['ok'] = False
    elif cap_check(stock, out) == False:
        if debug: print('市值不符合条件')
        out['ok'] = False

    if debug & out['ok']: 
        print('%s满足长线条件...'%stock.info['shortName'])
    return out
# def fundamental(ticker, debug=False):
#     stock = yf.Ticker(ticker)
#     out = calculate_stock(stock, debug)
#     if out: print(out)

def fundamentals(tickers, debug=False):
    stocks = yf.Ticker(tickers).tickers
    out = {}
    for stock in stocks:
        out[stock.ticker] = calculate_stock(stock, debug)
    print(out)

def calculate_stock(stock, debug=False):
    out = {}
    if industry_check(stock, out) == False:
        if debug: print('%s的产业不符合条件'%stock.ticker)
        return False
    elif pb_check(stock, out) == False:
        if debug: print('%s的市净率不符合条件'%stock.ticker)
        return False
    elif profitable_check(stock, out) == False:
        if debug: print('%s的当前未盈利'%stock.ticker)
        return False
    elif cap_check(stock, out) == False:
        if debug: print('%s的市值不符合条件'%stock.ticker)
        return False

    if debug: print('%满足长线条件...'%stock.info['shortName'])
    return out
    


# %%
# 测试
import yfinance as yf
stock = yf.Ticker('MSFT')


# %%
fundamental('600435.SS', True)


