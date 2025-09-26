---
title: 货币兑换混合类（Currency Exchange Mixin）
---

## CurrencyExchangeMixin

`CurrencyExchangeMixin` 类允许插件提供自定义后端，用于更新货币汇率信息。

任何实现类都必须提供 `update_exchange_rates` 方法。

### 内置插件

用于处理货币汇率的默认内置插件是 `InvenTreeCurrencyExchangePlugin` 类。

::: plugin.builtin.integration.currency_exchange.InvenTreeCurrencyExchange
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []


### 示例插件

下面展示了一个简单的示例（使用虚假数据）。

```python

from plugin import InvenTreePlugin
from plugin.mixins import CurrencyExchangeMixin

class MyFirstCurrencyExchangePlugin(CurrencyExchangeMixin, InvenTreePlugin):
    """示例货币兑换插件"""

    ...

    def update_exchange_rates(self, base_currency: str, symbols: list[str]) -> dict:
        """更新货币汇率。

        该方法*必须*由插件类实现。

        参数:
            base_currency: 用于汇率的基础货币
            symbols: 要检索汇率的货币符号列表

        返回值:
            一个汇率字典，如果更新失败则返回 None

        异常:
            如果更新失败，可以引发任何异常
        """

        rates = {
            'base_currency': 1.00
        }

        for sym in symbols:
            rates[sym] = random.randrange(5, 15) * 0.1

        return rates
```
