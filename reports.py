
# reports.py

def full_inventory_report(products):
    """Print a full inventory report."""
    print("=== FULL INVENTORY REPORT ===")
    for p in products.values():
        print(f"{p.product_id} | {p.name} | {p.category} | Qty: {p.quantity_in_stock} | "
              f"Price: ${p.unit_price:.2f}")


def low_stock_report(products):
    """Print a low-stock report."""
    print("=== LOW STOCK REPORT ===")
    lows = [p for p in products.values() if p.is_low_stock() and p.active]
    if not lows:
        print("No low-stock items.")
        return
    for p in lows:
        print(f"{p.product_id} | {p.name} | Qty: {p.quantity_in_stock} | Reorder at: {p.reorder_level}")


def total_inventory_value_report(products):
    """Print total inventory value and per-category totals."""
    print("=== TOTAL INVENTORY VALUE REPORT ===")
    total = 0.0
    by_category = {}

    for p in products.values():
        value = p.quantity_in_stock * p.unit_price
        total += value
        by_category[p.category] = by_category.get(p.category, 0.0) + value

    for cat, val in by_category.items():
        print(f"Category {cat}: ${val:.2f}")

    print(f"TOTAL INVENTORY VALUE: ${total:.2f}")


def open_purchase_orders_report(purchase_orders):
    """Print all open purchase orders."""
    print("=== OPEN PURCHASE ORDERS ===")
    opens = [po for po in purchase_orders.values() if po.status == "OPEN"]
    if not opens:
        print("No open POs.")
        return
    for po in opens:
        print(f"PO {po.po_number} | Vendor: {po.vendor_id} | Date: {po.date_created} | "
              f"Total: ${po.total_cost:.2f}")


def reorder_suggestions_report(products):
    """Print reorder suggestions for low-stock products with estimated cost."""
    print("=== REORDER SUGGESTIONS ===")
    suggestions = [p for p in products.values() if p.is_low_stock() and p.active]
    if not suggestions:
        print("No reorder suggestions at this time.")
        return

    for p in suggestions:
        cost = p.reorder_quantity * p.unit_price
        print(f"{p.product_id} | {p.name} | Suggest reorder: {p.reorder_quantity} | "
              f"Est. cost: ${cost:.2f}")
