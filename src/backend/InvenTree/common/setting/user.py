"""User settings definition."""

from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from common.setting.type import InvenTreeSettingsKeyType
from plugin import PluginMixinEnum, registry


def label_printer_options():
    """Build a list of available label printer options."""
    printers = []
    label_printer_plugins = registry.with_mixin(PluginMixinEnum.LABELS)
    if label_printer_plugins:
        printers.extend([
            (p.slug, p.name + ' - ' + p.human_name) for p in label_printer_plugins
        ])
    return printers


USER_SETTINGS: dict[str, InvenTreeSettingsKeyType] = {
    'LABEL_INLINE': {
        'name': _('内联标签显示'),
        'description': _(
            'Display PDF labels in the browser, instead of downloading as a file'
        ),
        'default': True,
        'validator': bool,
    },
    'LABEL_DEFAULT_PRINTER': {
        'name': _('默认标签打印机'),
        'description': _('配置默认情况下应选择哪个标签打印机'),
        'default': '',
        'choices': label_printer_options,
    },
    'REPORT_INLINE': {
        'name': _('内联报告显示'),
        'description': _(
            'Display PDF reports in the browser, instead of downloading as a file'
        ),
        'default': False,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_PARTS': {
        'name': _('搜索零件'),
        'description': _('在搜索预览窗口中显示零件'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_SUPPLIER_PARTS': {
        'name': _('搜索供应商零件'),
        'description': _('在搜索预览窗口中显示供应商零件'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_MANUFACTURER_PARTS': {
        'name': _('搜索制造商零件'),
        'description': _('在搜索预览窗口中显示制造商零件'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_HIDE_INACTIVE_PARTS': {
        'name': _('隐藏非活动部分'),
        'description': _('在搜索预览窗口中排除非活动部件'),
        'default': False,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_CATEGORIES': {
        'name': _('搜索类别'),
        'description': _('在搜索预览窗口中显示零件类别'),
        'default': False,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_STOCK': {
        'name': _('搜索库存'),
        'description': _('在搜索预览窗口中显示库存商品'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_HIDE_UNAVAILABLE_STOCK': {
        'name': _('隐藏缺货商品'),
        'description': _(
            '从搜索预览窗口中排除不可用的库存商品从搜索预览窗口中排除不可用的库存商品'
        ),
        'validator': bool,
        'default': False,
    },
    'SEARCH_PREVIEW_SHOW_LOCATIONS': {
        'name': _('搜索地点'),
        'description': _('在搜索预览窗口中显示库存地点'),
        'default': False,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_COMPANIES': {
        'name': _('搜索公司'),
        'description': _('在搜索预览窗口中显示公司'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_BUILD_ORDERS': {
        'name': _('搜索生产订单'),
        'description': _('在搜索预览窗口中显示生产订单'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_PURCHASE_ORDERS': {
        'name': _('搜索采购订单'),
        'description': _('在搜索预览窗口中显示采购订单'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_EXCLUDE_INACTIVE_PURCHASE_ORDERS': {
        'name': _('排除非活动采购订单'),
        'description': _('从搜索预览窗口中排除非活动采购订单'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_SALES_ORDERS': {
        'name': _('搜索销售订单'),
        'description': _('在搜索预览窗口中显示销售订单'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_EXCLUDE_INACTIVE_SALES_ORDERS': {
        'name': _('排除非活动销售订单'),
        'description': _('从搜索预览窗口中排除非活动销售订单'),
        'validator': bool,
        'default': True,
    },
    'SEARCH_PREVIEW_SHOW_SALES_ORDER_SHIPMENTS': {
        'name': _('搜索销售订单发货'),
        'description': _('在搜索预览窗口中显示销售订单发货'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_SHOW_RETURN_ORDERS': {
        'name': _('搜索退货单'),
        'description': _('在搜索预览窗口中显示退货单'),
        'default': True,
        'validator': bool,
    },
    'SEARCH_PREVIEW_EXCLUDE_INACTIVE_RETURN_ORDERS': {
        'name': _('排除非活动退货单'),
        'description': _('从搜索预览窗口中排除非活动退货单'),
        'validator': bool,
        'default': True,
    },
    'SEARCH_PREVIEW_RESULTS': {
        'name': _('搜索预览结果'),
        'description': _('每个搜索预览窗口部分中显示的结果数'),
        'default': 10,
        'validator': [int, MinValueValidator(1)],
    },
    'SEARCH_REGEX': {
        'name': _('正则表达式搜索'),
        'description': _('在搜索查询中启用正则表达式'),
        'default': False,
        'validator': bool,
    },
    'SEARCH_WHOLE': {
        'name': _('全字匹配'),
        'description': _('搜索查询返回完全匹配的结果'),
        'default': False,
        'validator': bool,
    },
    'SEARCH_NOTES': {
        'name': _('搜索笔记'),
        'description': _('搜索查询会返回项目备注中的匹配结果'),
        'default': False,
        'validator': bool,
    },
    'FORMS_CLOSE_USING_ESCAPE': {
        'name': _('退出键关闭窗体'),
        'description': _('使用 Esc 键关闭模态窗体'),
        'default': False,
        'validator': bool,
    },
    'STICKY_HEADER': {
        'name': _('固定导航栏'),
        'description': _('导航栏位置固定在屏幕顶部'),
        'default': False,
        'validator': bool,
    },
    'STICKY_TABLE_HEADER': {
        'name': _('固定表头'),
        'description': _('表格标题固定在表格顶部'),
        'default': False,
        'validator': bool,
    },
    'SHOW_SPOTLIGHT': {
        'name': _('显示聚焦'),
        'description': _('启用聚光灯导航功能'),
        'default': True,
        'validator': bool,
    },
    'ICONS_IN_NAVBAR': {
        'name': _('导航图标'),
        'description': _('在导航栏中显示图标'),
        'default': False,
        'validator': bool,
    },
    'DATE_DISPLAY_FORMAT': {
        'name': _('日期格式'),
        'description': _('首选的日期显示格式'),
        'default': 'YYYY-MM-DD',
        'choices': [
            ('YYYY-MM-DD', '2022-02-22'),
            ('YYYY/MM/DD', '2022/22/22'),
            ('DD-MM-YYYY', '22-02-2022'),
            ('DD/MM/YYYY', '22/02/2022'),
            ('MM-DD-YYYY', '02-22-2022'),
            ('MM/DD/YYYY', '02/22/2022'),
            ('MMM DD YYYY', 'Feb 22 2022'),
        ],
    },
    'DISPLAY_STOCKTAKE_TAB': {
        'name': _('显示库存历史'),
        'description': _('在零件详情页面显示库存历史信息'),
        'default': True,
        'validator': bool,
    },
    'ENABLE_LAST_BREADCRUMB': {
        'name': _('显示最后一个面包屑'),
        'description': _('在面包屑中显示当前页面'),
        'default': False,
        'validator': bool,
    },
    'SHOW_FULL_LOCATION_IN_TABLES': {
        'name': _('在表格中显示完整库存地点'),
        'description': _(
            'Disabled: The full location path is displayed as a hover tooltip. Enabled: The full location path is displayed as plain text.'
        ),
        'default': False,
        'validator': bool,
    },
    'SHOW_FULL_CATEGORY_IN_TABLES': {
        'name': _('在表格中显示完整零件类别'),
        'description': _(
            'Disabled: The full category path is displayed as a hover tooltip. Enabled: The full category path is displayed as plain text.'
        ),
        'default': False,
        'validator': bool,
    },
    'NOTIFICATION_ERROR_REPORT': {
        'name': _('Receive error reports'),
        'description': _('Receive notifications for system errors'),
        'default': True,
        'validator': bool,
    },
    'LAST_USED_PRINTING_MACHINES': {
        'name': _('Last used printing machines'),
        'description': _('Save the last used printing machines for a user'),
        'default': '',
    },
}
