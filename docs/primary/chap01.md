在量化分析中，投资者使用计算机编写程序，以历史市场数据为基础，通过模型建立和优化来判断市场趋势和进行投资决策。数据（包括行情数据、基本面数据、财务数据等等）是量化分析的基础。

1990年底，上交所成立时，交易是依靠红马甲喊单撮合的。每个交易日，各家券商交易员挤在一起，手中抓着标着股票代码的小纸条，用力地喊着出价。每当一家券商的交易员大喊“买入”，一群卖方交易员便紧张地挤在一起，争相抛售股票。在这个拥挤的大厅里，每个人都面带紧张的表情，眼睛紧盯着交易屏幕，寻找着最新的交易信息。而每当一只股票价格发生波动，整个交易厅就会一片骚动。有些人会立即举起手中的纸条，向交易员报价，希望能够抓住市场机会。在这个手工竞价交易的时代，每个交易员的工作都非常繁琐，需要手动记录和处理大量的数据和信息。交易员们通常需要长时间地待在交易厅里，时刻准备着应对市场的变化。显然这种落后的交易方式下，是无法提供量化需要的条件的。

A股的量化史可以追溯到2005年8月，当时嘉实元和稳健成长证券投资基金成立，主打量化投资策略。在此前后，一些券商、金融机构和软件服务商开始了相关数据的收集与整理。比如成立于1997年的万得(Wind)财经，它提供的数据涵盖了A股市场的股票、基金、债券、衍生品等多个领域，是A股市场的重要数据来源之一。随后，又出现了一批象通达信、同花顺、东方财富这样的行情软件开发商，他们也开始提供面向终端的行情数据和基于API的数据服务。

上面提到的这些厂商主要服务于金融机构。随着量化热潮的兴起，出现了向个人量化开发者和中小型投资机构出售量化数据的需求。这里面代表性的产品包括pytdx[^pytdx]，tushare, akshare, baostock, 聚宽等等。

考虑到这门课的受众是刚入门的量化爱好者，因此我们选择数据源时，要综合考虑价格、质量和易用性等多个因子。我们将按照价格从低到高的顺序，为大家着重介绍一些个人投资者可以承担的产品。至于更高端的产品，您可以在精通量化策略开发，能产生稳定的收益之后，再自行接入使用。

在深入到具体的各个数据源之前，我们需要先了解一点基础的证券知识。

# 1. 交易所及证券代码

A股有三个交易所，即上交所、深交所和北交所。上交所成立最早，其下有主板和科创板两个板块；深交所次之，它下面有主板、中小板和创业板三个板块；北交所则刚刚成立一年多，只有一个板块。

设立多个交易所和板块，是因为资本市场需要为不同成长风格的企业都能提供融资，这也是世界范围内证券交易所的常态，比如我们熟知的美国市场，纳斯达克交易所就以接纳全球高科技企业为主，我们科创板的定位就类似于纳斯达克。在同一个板块的所有股票，它们都有相同的起始编号，不同的板块，起始号码则各不相同。比如创业板最初是以300和301起头，科创板则以688起头，中小板以002起头，等等。

股票代码在每个交易所内的编号都是唯一的，但在不同的交易所之间，可能存在冲突的情况。所有的号码段都是为股票分配的，那么在编制指数时，应该安排什么号段呢？由于指数的编制机制与股票发行机制大不相同，所以，我们没法给它分配固定的号段，只能由交易所自己见机行事。因此，指数的编号就有可能与其它交易所中经营的股票品种相冲突。比如，深发展[^sfz]是A股发行较早[^first_8]的一支股票（现名平安银行），它的编号是000001，在深交所上市。而上交所在成立半年多后，开始编制综合指数，也使用了000001的编号，这就与深发展相冲突了。

因此，我们要了解的第一个概念，就是只有证券名称加上交易所代码，才能惟一确定一支证券品种。比如，有的软件系统使用XSHE指代深交所，使用XSHG来指代上交所。如此一来，000001.XSHE就惟一指向深发展，而000001.XSHG就惟一指向上综指。这是一种比较科学的方法。我们也可以把000001.XSHG称为上综指的规范名称，而把000001称为深发展或者上综指的简码。

股民在交流中，往往只使用简码。但当我们通过量化程序来获取数据时，则必须使用无歧义的代码。不同的系统使用了不同的方法。Akshare中，一般使用'sz'、'sh'和'bj'来分别代码深交所、上交所和北交所。

# 2. 别人家的孩子
作为zillionare的开发者，我们对数据有自己的处理方式，不过，在介绍我们自己的宝贝之前，我们先看看一些优秀的别人家的孩子。
## 2.1. Akshare
AkShare是基于爬虫的财经数据接口库，目的是实现对股票、期货、期权、基金、外汇、债券、指数、数字货币等金融产品的基本面数据、实时和历史行情数据、衍生数据从数据采集、数据清洗到数据落地的一套工具。它自身没有服务器，也不存储数据，数据来源于对大型财经网站的爬取，因此会受到网站限流等反爬措施限制。
Akshare是一个Python库，我们使用pip来安装：
```shell
$ pip install akshare
```
akshare是免费数据，也无须注册账号。所以我们现在就可以使用它来获取沪深A股的行情数据了。


在akshare中，获取证券数据的API格式多为{type}_{zh|sz|sh|bj|cy|kc}_a_{spot|hist}_{server}的形式。显然，这里的'a'并表明是取A股数据。

type是指证券的类型，即是'stock'还是'index'；board or exchange这个字段对应交易所（或者板块），其取值可以是'zh'（取所有A股数据）、'sz'（取所有深证A股）、'sh'（取所有上证A股），'bj'（取所有北京交易所A股），'cy'（取所有创业板A股），'kc'（取所有科创板A股）等。

第三个字段用来区分要获取的数据是实时数据，还是历史数据，我们需要在spot和hist中进行选择。如果选择spot，则表明是取实时数据，如果选择hist，则表明是取历史数据。

server字段可以为空（此时不需要带最后的'_')，此时表明从新浪服务器上取数据；也可以是'em'（表明从东方财富网上取数据），还可以是'tx'（表明从腾讯财经获取数据）。当然，不同的服务器，它们能提供的数据品种可能有所区别。

### 2.1.1. 实时股票数据

下面，我们就以获取创业板实时股票数据为例演示一下。根据上面的介绍，这个api应该是stock_cy_a_spot：

```python
import akshare as ak

bars = ak.stock_cy_a_spot()
bars[:10]
```
运行后提示错误：在akshare中没有stock_cy_a_spot这个方法。原因是，这个方法隐含的服务器是新浪财经，但新浪财经并不提供实时数据。不过，东方财富提供了这个数据，所以，我们可以用stock_cy_a_spot_em这个API：
```python
import akshare as ak

bars = ak.stock_cy_a_spot_em()
bars[:10]
```
现在我们看到了10股票的最新价格数据。在我们的实践中，我们尝试过每5秒更新一次全A市场的最新价格，因此可以在实盘中当准实时数据来使用。

### 2.1.2. 股票历史数据
在上一节，我们已经熟悉了akshare的API风格。获取股票历史数据的api与获取实时数据的类似，区别在于，我们需要将'spot'换成'hist'，并且还需要传入一些参数。

比如，我们要获取'603777'这支股票在2022年下半年的日线数据：
```python
import akshare as ak

bars = ak.stock_zh_a_hist('603777', 'daily', '20220701', '20221231', adjust='qfq')
bars[-10:]
```
这里的参数依次是股票简码、周期类型、起始日期和复权方式。周期类型支持'daily'（日线），'weekly'（周线）, 'monthly'（月线）。复权方式[^fq]支持前复权（'qfq')和后复权（'hfq'）。如果需要未复权的原始价格，则可省略此参数。

### 2.1.3. 证券列表
我们在获取股票历史数据时，已经接触到了具体的股票代码。要记住所有的代码几乎是不可能的，因为现在A股已经到了5000支左右股票的规模。因此，我们需要一个索引，或者证券列表，让我们可以查询股票的代码、名字、上市日期等基本信息。

这个API就是`stock_info_{sh|sz|bj}_name_code`。中间的字段是交易所的代码。

```python
import akshare as ak

ak.stock_info_sh_name_code()
```
这会返回一个DataFrame，共有'公司代码', '公司简称', '公司全称', '上市日期'等四列数据。如果我们将交易所代码替换成'sz'或者'bj'，则会得到总股本、流通股本、所属行业、地区、报告日期等额外五列数据。同样类型的请求，返回结果在字段上不一致，这会带来策略使用上的一些不便。

### 2.1.4. 交易日历

交易日历在量化中起到非常重要的作用。比如，我们要取截止`end`日期的250根K线数据。如果使用的API只支持按起始日期来获取数据，那么我们将不得不自己来计算这个起始日期。而这个计算，我们不能依赖自然日历。此外，有了交易日历，一些后台任务也才能合理的规划。比如，如果这一周只交易到周三，那么对于机构来说，一般就应该在周三交易结束之后，进行周线级别的策略分析，而不是等到周六。

我们可以这样获取交易日历:
```python
import akshare as ak

calendar = ak.tool_trade_date_hist_sina()
print(f"日历起始日：{calendar.iloc[0,0]}\n日历截止日：{calendar.iloc[-1,0]}")
```
在我们编写这门课的时候，上述代码运行将输出1990-12-19和2023-12-29这样两个日期。

Akshare还提供了许多其它数据，比如象全市场市盈率这样比较重要的择时数据，不过，这些不属于基础内容，我们在这里就不展开了。这些内容及数据的使用，我们将在高级课程中提供。

Akshare轻量、免注册，还能获取实时价格数据。由于数据直接来源于大的财经网站，因此准确度较高，这也是我们推荐它的原因。不过，如果我们要在正式产品中使用akshare的话，也要注意以下问题：

1. 服务器会对爬虫进行限流。在调用akshare失败后，我们需要采用退火算法进行延时等待；反之，如果我们不断重试的话，可能导致整个IP都被封掉。退火算法的实现需要一定的专业度，建议akshare官方实现这个功能。
2. akshare在其代码中引入了tqdm，这是一个非常有名的进度条工具。但这个工具也引起了一些问题，比如你不能在一个没有连接到终端的程序中使用它（会导致异常退出）。在生产环境下，应用往往是以服务方式运行的，这些服务都不会连接到终端，因此，这些服务中，都不能使用akshare。
3. akshre发出网络请求时，是以同步调用的方式进行的，可以改为异步调用以优化性能。
4. akshare的api设计中，绑定了服务器的指定。其实对普通用户来讲，我们只关心能否快速、精准地获取数据，不关心数据来自于哪个服务器。不仅如此，如果现在的这些服务器将来不能用了，要使用新的服务器，这也会使得我们必须修改自己的策略代码。因此，建议大家在使用akshare时，自己先进行一些封装和修改，再在策略里调用自己的封装包，以便即使akshare的一些API被弃用了，也不用改我们的策略代码，只用将接口实现改一下就好了。

## 2.2. tushare
Tushare是一个提供股票、期货、基金等金融数据的Python库。要使用Tushare获取A股数据，您需要首先安装Tushare库，并在Tushare[^tushare]官网注册一个账号以获取Token，这个Token用于验证您的数据访问权限。

在tushare中，如果某个调用需要传入交易所代码参数，一般使用SSE指代上交所，SZSE指代深交所，BSE指代北交所，HKEX指代港交所。对应地，其股票规范码的后缀则是.SH, .SZ, .BJ和.HK。

tushare暂时没有在盘中提供实时数据。它所提供的数据，除了数字货币之外，都是盘后数据。

### 2.2.1. 股票历史数据
以下是一个简单的示例，用于获取某只股票的历史价格数据：
```python
import tushare as ts
import os

# 在Tushare官网注册并获取token
token = os.environ.get("tushare_token")
ts.set_token(token)

# 初始化pro接口
pro = ts.pro_api()

# 获取某只股票的历史价格数据
df = pro.daily(ts_code='000001.SZ', start_date='20190101', end_date='20220218')

# 打印历史价格数据
print(df[:10])
```
在上面的代码中，我们首先通过调用ts.set_token()函数设置Tushare的Token，以验证我们的数据访问权限。然后，我们初始化Tushare的pro接口，以便进行数据访问。接着，我们调用pro.daily()函数，用于获取某只股票（000001.SZ）的历史价格数据，包括起始日期和结束日期。最后，我们将数据打印出来。

这里我们看到了另一种交易所代码表示方式。在tushare里，上交所的代码后缀是.SH，深交所的代码后缀是.SZ，北交所的代码后缀是.BJ。tushare还能提供港交所的数据，它的后缀是.HK。
### 2.2.2. 证券列表
我们通过stock_basic来获取证券列表。
```python
import tushare as ts
import os

# 在Tushare官网注册并获取token
token = os.environ.get("tushare_token")
ts.set_token(token)

# 初始化pro接口
pro = ts.pro_api()

df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(df[:10])
```
输出字段包括了规范代码、简码、名称、地区、行业和上市日期。此外，还支持获取其拼音缩写、市场类型（主板/创业板、科创板）、是否沪深港通标的等字段。

### 2.2.3. 交易日历
tushare的交易日历返回的是自然日历，但在日期后面通过is_open进行了标注。此外，它还支持按起始日期进行查询：

```python
import tushare as ts
import os

# 在Tushare官网注册并获取token
token = os.environ.get("tushare_token")
ts.set_token(token)

# 初始化pro接口
pro = ts.pro_api()

# 获取某只股票的历史价格数据
pro.trade_cal(exchange='', start_date='20180101', end_date='20250101')
```
上述查询返回了一个自然日历，不过在每一行中，通过is_open来显示该日是否为交易日。tushare这样做，可能在一定程度上减轻调用都后续计算的工作量。不过，关系到交易日历的计算十分复杂，我们必须使用专门的库才行。

tushare是一个老牌的数据服务提供商。起初完全免费，后来升级到pro版本后，开始使用积分制。用户反馈较多的可能也是这个积分制。它的积分体系比较复杂。一个注册的新用户，会有100积分，拥有获取股票日线的权限，但如果要获取证券列表，则需要120积分。权限粒度过细，会导致用户体验下降。尽管如此，它仍然是一个优秀的、可获得的数据源。

## 2.3. 聚宽本地数据

聚宽[^joinquant]是相对于tushare更贵的选择，它的价格在逐年攀升，免费试用期[^free_trial]也在逐年减少。当前应该是给用户提供了3个月的试用期[^free_trial]。一个合用的授权版本大概是6999元每年。不过它的数据质量和服务不错。

按照官方文档，聚宽并不提供实时数据，但目前我们仍能在盘获取粒度低至一分钟的准实时数据。不过，使用者应该尽早排除对这种非官方支持的数据调用的依赖。

聚宽通过jqdatasdk向用户提供本地数据[^jqdata]，这是一个python的SDK。我们通过以下命令来安装使用jqdatasdk：

```
$ pip install jqdatasdk
```
我们在使用它之前，需要登录聚宽的主页申请使用，然后进行认证和获得授权。
```python
import jqdatasdk as jq
import os

account = os.environ.get("jq_account")
password = os.environ.get("jq_password")

jq.auth(account, password)
quota = jq.get_query_count()
print(quota)

jq.logout()
```
如果认证成功，就会打印出auth success。注意jqdatasdk对同时登录的会话数有要求，如果当前使用完成，最好调用jq.logout来退出，以释放会话。

我们还要注意在购买聚宽的数据时，它有一个每日使用的quota限制[^jq_quota]，一旦超出这个限制，当日将不能继续使用。

在聚宽中，上交所的代码是.XSHG，深交所的代码是.XSHE。我们可以按照这个规则来拼出股票和指数的规范代码。

### 2.3.1. 股票历史数据

我们可以使用get_price与get_bars两个API[^jq_diff][^pitfalls]来获得股票的历史数据。这里我们仅以get_bars为例来演示其用法：
```python
import jqdatasdk as jq
import os

account = os.environ.get("jq_account")
password = os.environ.get("jq_password")

jq.auth(account, password)
quota = jq.get_query_count()
spare= quota.get('spare')
bars = jq.get_bars("000001.XSHE", 250, unit='1d',
             fields=('date', 'open', 'high', 'low', 'close', 'volume', 'money', 'factor'),
             include_now=False,
             end_dt=None,
             fq_ref_date=None,
             df=False)

print(bars[:10])
quota = jq.get_query_count()
print("消耗的流量为:", spare - quota.get('spare'))
jq.logout()
```
返回的数据将包括记录所属的时间、开盘价、最高价、最低价、收盘价、成交量（以股为单位）、成交金额（以元为单位）和复权因子。上述查询，消耗了250条流量。

输入参数中，"000001.XSHE"是证券标的，250在这里是要获取的记录数，unit是指记录的时间周期，比如是日线、周线这样日线级别的周期，还是象1分钟，30分钟这样的分钟级别的周期。

如果当天是交易日，我们在盘中获取某支标的的当日行情数据，此时jqdatasdk会面临两个选择，是返回截止到当前的日线数据呢，还是返回截止到上一个成交日收盘时的行情数据呢？这就是include_now这个参数的意义，它告诉jqdata_sdk应该如何返回数据。

end_dt是指我们请求的数据，将截止到哪一天。如果不传入，则会获取到调用时（如果是非交易时间，则是上一个收盘时间）。

fq_ref_date告诉jqdatasdk如何处理复权。如果不提供这个参数，则返回的数据将不会复权。如果提供了这个日期，则在日期之前，相当于前复权，在日期之后，相当于后复权。这是与其它库不一样的地方。

### 2.3.2. 证券列表
在聚宽中，获取证券列表的函数是get_all_securities[^pitfalls]。
```python
import jqdatasdk as jq
import os

account = os.environ.get("jq_account")
password = os.environ.get("jq_password")

jq.auth(account, password)
quota = jq.get_query_count()
spare= quota.get('spare')
bars = jq.get_all_securities()

print(bars[:10])
quota = jq.get_query_count()
print("消耗的流量为:", spare - quota.get('spare'))
jq.logout()
```
查询返回了5000多条记录。返回的记录包含了字段中文名称（如平安银行）、缩写简称（如PAYH）、上市日期、退市日期和证券类型（如stock, index, futures等）。返回的记录种类跟账户的权限相关。

### 2.3.3. 交易日历
我们通过get_trade_days这个API来获取指定时间范围内的交易日历，使用get_all_trade_days这个API来获取所有交易日历。
```python
import jqdatasdk as jq
import os

account = os.environ.get("jq_account")
password = os.environ.get("jq_password")

jq.auth(account, password)
quota = jq.get_query_count()
spare= quota.get('spare')
calendar = jq.get_trade_days(count=10)

print(calendar)

calendar = jq.get_all_trade_days()

print(calendar[-10:])
quota = jq.get_query_count()
print("消耗的流量为:", spare - quota.get('spare'))
jq.logout()
```

## 2.4. Baostock
Baostock是一个免费、开源的证券数据平台，大概从2018年起开始对外提供服务。它可以提供到5分钟级的数据。Baostock使用上无需注册，但它有会话的概念，仍然需要登录。它只能提供历史数据。从官网来看，提供的数据种类较少。使用稳定性、响应速度等指标上能见到的报道不多。另外，我们也没找到它提供交易日历的相关函数。

Baostock的证券代码使用前缀式标示法，即采用"证券交易所代码"加"证券简码"的方式来表示。其中，上交所代码为"sh"， 深交所为"sz"。举例来说，中国平安的代码就是"sz.000001"，沪指的代码就是"sh.000001"

我们通过以下命令来安装：
```
$ pip install baostock
```
### 2.4.1. 股票历史数据
我们可以通过下面的代码来获取历史数据。

```python
import baostock as bs
import pandas as pd

# 登录baostock
lg = bs.login()

# 获取个股行情数据
rs = bs.query_history_k_data_plus("sz.000001", "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST", start_date='2021-01-01', end_date='2021-12-31', frequency="d", adjustflag="3")
print('query_history_k_data_plus respond error_code:' + rs.error_code)
print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

# 打印结果
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(result)

# 登出baostock
bs.logout()
```
### 2.4.2. 证券列表
我们可以通过下面的代码来获取证券列表。
```python
import baostock as bs

# 登录baostock
lg = bs.login()

# 获取股票列表
rs = bs.query_stock_industry()
print('query_stock_industry respond error_code:' + rs.error_code)
print('query_stock_industry respond  error_msg:' + rs.error_msg)

# 打印结果
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(result)

# 登出baostock
bs.logout()

```

## 2.5. yfinance

yfinance是一个Python库，它可以用来获取Yahoo Finance的数据，包括股票、ETF、指数、期货等多种金融产品的历史价格和相关信息。在使用yfinance之前，需要先安装该库，可以使用pip命令来安装：
```
$ pip install yfinance
```

yfinance可以用来获取全球市场的数据，包括美国、加拿大、欧洲、亚洲等地的股票和其他金融产品，但是从2021年11月起，中国大陆用户已不能使用yfinance。这里介绍它，只是作为一个参考，以防学员需要使用其它地区的金融数据。

下面是使用yfinance来获取股价的一个例子：
```python
import yfinance as yf

# 获取某只股票的历史价格数据
msft = yf.Ticker("MSFT")
msft_history = msft.history(period="max")
print(msft_history)
```
上述代码中，我们通过yf.Ticker函数指定了要获取的股票，这里以微软公司（MSFT）为例。然后，我们调用history方法来获取该股票的历史价格数据，使用period="max"表示获取该股票的所有历史数据。


[^pytdx]: pytdx是破解通达信通讯协议后，提供的一个数据获取的API。大约在2020年前后，其开发者归档了这个项目，不再持续开发。pytdx在早期为量化开发者提供了非常好的练习环境。

[^first_8]: A股最早发行的一批股票共8支，被称为老八股，是1990年12月在上海交易所上市的。这八股当中，两股已经退市(600656，原浙江凤凰和600652，原爱使股份，两股当前被ST（600601，方正科技和600654，飞乐股份）。

[^sfz]: 深发展1991年上市日开盘价为65.74，当前（2023年2月17日）后复权收盘价为2492元。作为二级市场投资者，如果您在32年前以开盘价买入，到现在为止上涨37倍，年化12%。作为二级市场的投资者，这个收益您还满意吗？

[^akshare]: akshare的文档在 https://akshare.xyz/ 

[^fq]: 由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。 若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。 为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。<br>前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。 前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。 这种方法虽然很常见，但也有两个缺陷需要注意。<br>为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。 这会导致在不同时点看到的历史前复权价可能出现差异。<br>对于有持续分红的公司来说，前复权价可能出现负值。<br>后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。 后复权价格和真实股票价格可能差别较大，不适合用来看盘。 其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。

[^tushare]: tushare的主页是 https://tushare.pro/，开发者人称米哥。

[^joinquant]: 聚宽的主页是 https://www.joinquant.com/。作为聚宽数据的使用者，对他们的服务有较深的印象。他们的客服会及时响应用户提出的数据相关问题，不管是晚上还是周末。
[^free_trial]: 最初聚宽提供了一年的免费试用，后来逐渐缩减到半年和三个月。三个月试用期对新人来说可能过短。此外，试用版还只能获取近一年的数据，这对实际的策略回测也是远远不够的。

[^jqdata]: 这里的本地数据是聚宽的提法，是相对于通过聚宽在线平台而言的。但是，我们在使用时，这些数据仍然是从聚宽服务器上实时获取的。因此，获取的速度取决于网络延时和聚宽服务器的处理能力。

[^jq_diff]: 这两个API虽然都能用于获取数据，但在用法和返回结果上有微妙的区别。get_price可以额外获取涨跌停价、是否停牌、前一天收盘价信息等。在复权处理上，get_price默认使用前复权，get_bars使用不复权。get_price只使用起始时间来进行查询，而get_bars还可以指定要获取的记录条数。此外，还有一些差别，请学员在使用前，仔细阅读https://www.joinquant.com/help/api/doc?name=JQDatadoc&id=10278。

[^pitfalls]: 此处有坑，请老师提醒学员可以加老师微信请教，没必要自己花太多时间去趟这些坑。我们开设这门课，一是要帮学员理清知识体系，二是要帮学员避开这些坑，减少时间浪费。这也是这门课的意义所在。

[^baostock]: baostock的文档在 http://baostock.com
