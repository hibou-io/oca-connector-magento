from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping, only_create


class ProductImportMapper(Component):
    _inherit = 'magento.product.product.import.mapper'

    @only_create
    @mapping
    def product_by_sku(self, record):
        product = self.env['product.product']
        sku = record.get('sku')
        if sku:
            product = product.search([('default_code', '=', sku)],
                                     limit=1)
        return {'odoo_id': product.id}
