import json
from models import Product, Vendor, PurchaseOrder

DATA_FILE = "sample_data.json"

def load_data(filename=DATA_FILE):
    """Load products, vendors, and purchase orders from JSON file."""
    products, vendors, purchase_orders = {}, {}, {}

    try:
        with open(filename, "r") as f:
            data = json.load(f)

        for p in data.get("products", []):
            prod = Product.from_dict(p)
            products[prod.product_id] = prod

        for v in data.get("vendors", []):
            ven = Vendor.from_dict(v)
            vendors[ven.vendor_id] = ven

        for po in data.get("purchase_orders", []):
            po_obj = PurchaseOrder.from_dict(po)
            purchase_orders[po_obj.po_number] = po_obj

    except FileNotFoundError:
        print(f"Data file '{filename}' not found. Starting with empty data.")
    except json.JSONDecodeError:
        print("Error reading JSON data. Starting with empty data.")

    return products, vendors, purchase_orders


def save_data(products, vendors, purchase_orders, filename=DATA_FILE):
    """Save products, vendors, and purchase orders to JSON file."""
    data = {
        "products": [p.to_dict() for p in products.values()],
        "vendors": [v.to_dict() for v in vendors.values()],
        "purchase_orders": [po.to_dict() for po in purchase_orders.values()]
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {filename}.")
