import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_move_line_product',
        'odoo13-addon-account_move_line_stock_info',
        'odoo13-addon-scrap_reason_code',
        'odoo13-addon-stock_account_change_qty_reason',
        'odoo13-addon-stock_available_unreserved',
        'odoo13-addon-stock_change_qty_reason',
        'odoo13-addon-stock_cubiscan',
        'odoo13-addon-stock_demand_estimate',
        'odoo13-addon-stock_demand_estimate_matrix',
        'odoo13-addon-stock_inventory_chatter',
        'odoo13-addon-stock_inventory_discrepancy',
        'odoo13-addon-stock_inventory_exclude_sublocation',
        'odoo13-addon-stock_inventory_include_exhausted',
        'odoo13-addon-stock_inventory_lockdown',
        'odoo13-addon-stock_location_bin_name',
        'odoo13-addon-stock_location_position',
        'odoo13-addon-stock_location_tray',
        'odoo13-addon-stock_location_zone',
        'odoo13-addon-stock_move_common_dest',
        'odoo13-addon-stock_move_location',
        'odoo13-addon-stock_orderpoint_manual_procurement',
        'odoo13-addon-stock_orderpoint_move_link',
        'odoo13-addon-stock_orderpoint_purchase_link',
        'odoo13-addon-stock_orderpoint_route',
        'odoo13-addon-stock_orderpoint_uom',
        'odoo13-addon-stock_removal_location_by_priority',
        'odoo13-addon-stock_request',
        'odoo13-addon-stock_request_kanban',
        'odoo13-addon-stock_request_purchase',
        'odoo13-addon-stock_request_tier_validation',
        'odoo13-addon-stock_reserve_rule',
        'odoo13-addon-stock_secondary_unit',
        'odoo13-addon-stock_warehouse_calendar',
        'odoo13-addon-stock_warehouse_orderpoint_stock_info',
        'odoo13-addon-stock_warehouse_orderpoint_stock_info_unreserved',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
