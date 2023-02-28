股民都很熟悉KDJ指标，也都知道这个指标有时候灵、有时候不灵。其实，现在私募界流行的是基于KDJ改良的一个指标，而如果你还只会用KDJ，当然要被主力割韭菜了。

我是量化研究员芝士，今天的视频就给大家讲讲这个指标。内容都是干货，也可能有一定难度，建议你点赞收藏，下来后再仔细看。如果觉得指标好用，还可以转发给朋友，一起来研究。

我们今天要介绍的这个指标，就是SKDJ，与KDJ只有一个字母之差，它是慢速KDJ的意思。KDJ指标是属于较快的随机波动，SKDJ指标则是属于较慢的随机波动，依股市经验，SKDJ指标较适合用于做短线。由于它不易出现抖动的杂讯，买卖点较KDJ指标明确。SKDJ指标的K值在低档出现与股价背离时，应当作买点，尤其是K值第二次超越D值时。

用伪码表示为：
```
LOWV=N日内最低价的最低值
HIGHV=N日内最高价的最高值

RSV=(收盘价-LOWV)/(HIGHV-LOWV)*100的M日指数移动平均

K=RSV的M日指数移动平均
D=K的M日简单移动平均

# N一般取9, M一般取3
```

下面我们看看如何用python来实现这段伪码。我们通常使用talib来计算各种技术指标，不过，这个指标比较新，所以talib也没有提供。今天，我们就把这个秘密告诉大家：
```python
import omicron
from coretypes import BarsArray, FrameType
import pandas as pd
from omicron.talib import exp_moving_average as ema
from omicron.talib import moving_average as ma
from omicron.models.stock import Stock
import arrow

await omicron.init()

def skdj(bars: BarsArray, n: int=9, m: int=3):
    """慢速KDJ指标计算

    Args:
        bars: 行情数据
    """
    close = bars["close"]
    lowv = np.min(bars["low"][-n:])
    highv = np.max(bars["high"][-n:])

    rsv = ema((close - lowv) / (highv - lowv) * 100, m)
    k = ema(rsv, m)
    d = ma(k, m)

    return {
        'SKDJ_K': k,
        'SKDJ_D': d
    }

code = "000001.XSHG"
bars = await Stock.get_bars(code, 120, end=arrow.now().date(), frame_type=FrameType.DAY)

print(skdj(bars))
```

代码我们也可以提供，欢迎私聊主播获取。
