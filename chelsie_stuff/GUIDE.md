## 使用介绍
---
### 基本代码

`now = datetime.datetime.now()` 此代码获取可当前日期。

`start = now - datetime.timedelta(days=365)` 此代码用`now`减去365天来获取一年前的日期。

`stock = pdr.get_data_yahoo('300712.SZ', start=start, end=now.date())` 此代码在Yahoo财经上获取一支股票从`start`至`now.date()`的日交易数据。

`stock.head()` 此代码将获取到的`stock`中的头**5**条交易数据显示出来，便以确保数据获取无误。可替换使用`stock.tail()`来获取最近**5**条交易数据。

### 功能代码

`exponent_trend(stock=stock)` 此代码将构图出给予的`stock`函数所包含的交易数据中的**倍量位**，并可通过修改`growth_rate`函数来调整次日应当递增的比例，例如`exponent_trend(stock=stock, growth_rate=2.5)`将会找出次日为当日至少250%成交量的**倍量位**。默认为1.7。

`staircase_trend(stock=stock)` 此代码将构图出给予的`stock`函数所包含的交易数据中的**梯量位**，并可通过修改`growth_rate`函数来调整后续3日应当递增的比例，例如`staircase_trend(stock=stock, growth_rate=1.03)`将会找出后续3日每日至少103%成交量的**梯量位**。默认为1.01。

`shrinkage_trend(stock=stock)` 此代码将构图出给予的`stock`函数所包含的交易数据中的**缩量**。

`plateau_trend(stock=stock)` 此代码将构图出给予的`stock`函数所包含的交易数据中的**平量位**，并可通过修改`volume_range`函数来调整交易量区间范围，例如`plateau_trend(stock=stock, volume_range=.1)`将会找出区间范围为10%成交量的**平量位**。默认为.01。

`leap_trend(stock=stock)` 此代码将构图出给予的`stock`函数所包含的交易数据中**未补的跳空缺口**。

上述**功能代码**均可独立使用，通过修改为`exponent_trend(ticker='300712.SZ', time_range=365)`即可无需提供交易数据直接使用。不过，统一获取交易数据运行会快很多。接下来会提供统一使用的例子。

## 使用例子
---
先按左上角**+**加号添加单元格，并把以下代码放入独立的单元格中按**播放键**运行
```python
now = datetime.datetime.now()
start = now - datetime.timedelta(days=365)
stock = pdr.get_data_yahoo('300712.SZ', start=start, end=now.date())
```

接下来再次按左上角**+**加号添加另外的单元格，并把以下代码放入独立的单元格中按**播放键**运行
```python
exponent_trend(stock=stock)
staircase_trend(stock=stock)
shrinkage_trend(stock=stock)
plateau_trend(stock=stock)
leap_trend(stock=stock)
```

未来每次需要更改股票时才去修改并运行第一个单元格，这样在修改使用**功能代码**就不会去不断地重新下载股票了。