# -*- coding: utf-8 -*-
# Copyright 2017 Hibou Corp.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.component.core import Component


class ProductImporter(Component):
    _inherit = 'magento.product.product.importer'

    def _create(self, data):
        product = self._find_existing_product(data)
        if product:
            data['odoo_id'] = product.id
        return super(ProductImporter, self)._create(data)

    def _find_existing_product(self, data):
        dc = data.get('default_code')
        if dc:
            product_model = self.env['product.product']
            return product_model.search([('default_code', '=', dc)], limit=1)
        return None
