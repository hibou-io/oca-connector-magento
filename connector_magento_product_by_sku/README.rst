.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Magento Connector - Product by SKU
==================================

Allows binding an existing product to a Magento product by exact match on the Magento SKU attribute.

Installation
============

This is an optional module and can be installed by searching in Apps for ``connector_magento_product_by_sku``

Usage
=====

This module will find an existing product where the Odoo product attribute ``default_code`` matches the Magento
attribute ``sku`` and will use it instead.

This means that it will not create a duplicate product, but will override
certain attributes such as the product ``name``, ``description`` and ``categ_id``.  The new binding still becomes a
checkpoint for review.

The binding to an existing product works both when importing batch products, and when importing an order dependency.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/connector-magento/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Jared Kipe <jared@hibou.io>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

