from models import Product, Vendor, PurchaseOrder

# ---------- PRODUCT FUNCTIONS ----------

def add_product(products, vendors):
    """Add a new product with validation."""
    product_id = input("Enter product ID: ").strip()
    if product_id in products:
        print("Error: Duplicate product ID.")
        return

    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()

    try:
        quantity_in_stock = int(input("Enter quantity in stock: "))
        reorder_level = int(input("Enter reorder level: "))
        reorder_quantity = int(input("Enter reorder quantity: "))
        unit_price = float(input("Enter unit price: "))
    except ValueError:
        print("Error: Quantity and price must be numeric.")
        return

    vendor_id = input("Enter vendor ID: ").strip()
    if vendor_id not in vendors:
        print("Error: Vendor ID not found.")
        return

    product = Product(product_id, name, category, quantity_in_stock,
                      reorder_level, reorder_quantity, unit_price, vendor_id)
    products[product_id] = product
    print("Product added successfully.")


def view_all_products(products):
    """Display all products."""
    if not products:
        print("No products found.")
        return

    for p in products.values():
        print(f"{p.product_id} | {p.name} | {p.category} | Qty: {p.quantity_in_stock} | "
              f"${p.unit_price:.2f} | Active: {p.active}")


def search_product_by_id(products, product_id):
    """Search for a product by ID."""
    return products.get(product_id)


def search_product_by_name(products, name):
    """Search for products by name (case-insensitive substring)."""
    name = name.lower()
    return [p for p in products.values() if name in p.name.lower()]


def search_product_by_category(products, category):
    """Search for products by category (case-insensitive exact match)."""
    category = category.lower()
    return [p for p in products.values() if p.category.lower() == category]


def edit_product(products):
    """Edit an existing product."""
    product_id = input("Enter product ID to edit: ").strip()
    product = products.get(product_id)
    if not product:
        print("Product not found.")
        return

    print(f"Editing {product.name} (leave blank to keep current value)")
    new_name = input(f"Name [{product.name}]: ").strip()
    if new_name:
        product.name = new_name

    new_category = input(f"Category [{product.category}]: ").strip()
    if new_category:
        product.category = new_category

    try:
        new_qty = input(f"Quantity [{product.quantity_in_stock}]: ").strip()
        if new_qty:
            product.quantity_in_stock = int(new_qty)

        new_rl = input(f"Reorder level [{product.reorder_level}]: ").strip()
        if new_rl:
            product.reorder_level = int(new_rl)

        new_rq = input(f"Reorder quantity [{product.reorder_quantity}]: ").strip()
        if new_rq:
            product.reorder_quantity = int(new_rq)

        new_price = input(f"Unit price [{product.unit_price}]: ").strip()
        if new_price:
            product.unit_price = float(new_price)
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    print("Product updated.")


def deactivate_product(products):
    """Deactivate a product (set active to False)."""
    product_id = input("Enter product ID to deactivate: ").strip()
    product = products.get(product_id)
    if not product:
        print("Product not found.")
        return
    product.active = False
    print("Product deactivated.")


def display_low_stock_products(products):
    """Display all low-stock products."""
    lows = [p for p in products.values() if p.is_low_stock() and p.active]
    if not lows:
        print("No low-stock products.")
        return
    for p in lows:
        print(f"{p.product_id} | {p.name} | Qty: {p.quantity_in_stock} | Reorder at: {p.reorder_level}")


# ---------- VENDOR FUNCTIONS ----------

def add_vendor(vendors):
    """Add a new vendor with validation."""
    vendor_id = input("Enter vendor ID: ").strip()
    if vendor_id in vendors:
        print("Error: Duplicate vendor ID.")
        return

    name = input("Enter vendor name: ").strip()
    contact_name = input("Enter contact name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address (city/state or full): ").strip()

    vendor = Vendor(vendor_id, name, contact_name, phone, email, address)
    vendors[vendor_id] = vendor
    print("Vendor added.")


def view_all_vendors(vendors):
    """Display all vendors."""
    if not vendors:
        print("No vendors found.")
        return

    for v in vendors.values():
        print(f"{v.vendor_id} | {v.name} | {v.contact_name} | {v.phone} | {v.email} | {v.address}")


def search_vendor_by_name(vendors, name):
    """Search vendors by name (case-insensitive substring)."""
    name = name.lower()
    return [v for v in vendors.values() if name in v.name.lower()]


def edit_vendor(vendors):
    """Edit vendor information."""
    vendor_id = input("Enter vendor ID to edit: ").strip()
    vendor = vendors.get(vendor_id)
    if not vendor:
        print("Vendor not found.")
        return

    print(f"Editing {vendor.name} (leave blank to keep current value)")
    new_name = input(f"Name [{vendor.name}]: ").strip()
    if new_name:
        vendor.name = new_name

    new_contact = input(f"Contact [{vendor.contact_name}]: ").strip()
    if new_contact:
        vendor.contact_name = new_contact

    new_phone = input(f"Phone [{vendor.phone}]: ").strip()
    if new_phone:
        vendor.phone = new_phone

    new_email = input(f"Email [{vendor.email}]: ").strip()
    if new_email:
        vendor.email = new_email

    new_address = input(f"Address [{vendor.address}]: ").strip()
    if new_address:
        vendor.address = new_address

    print("Vendor updated.")


# ---------- PURCHASE ORDER FUNCTIONS ----------

def create_purchase_order(products, vendors, purchase_orders):
    """Create a new purchase order."""
    po_number = input("Enter new PO number: ").strip()
    if po_number in purchase_orders:
        print("Error: Duplicate PO number.")
        return

    vendor_id = input("Enter vendor ID: ").strip()
    if vendor_id not in vendors:
        print("Vendor not found.")
        return

    po = PurchaseOrder(po_number, vendor_id)

    while True:
        product_id = input("Enter product ID to add (or blank to finish): ").strip()
        if not product_id:
            break

        product = products.get(product_id)
        if not product:
            print("Product not found.")
            continue

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Invalid quantity.")
            continue

        po.add_item(product_id, qty, product.unit_price)
        print(f"Added {qty} x {product.name} to PO.")

    if not po.items:
        print("No items added. PO not created.")
        return

    purchase_orders[po_number] = po
    print(f"PO {po_number} created. Total: ${po.total_cost:.2f}")


def view_purchase_orders(purchase_orders):
    """Display all purchase orders."""
    if not purchase_orders:
        print("No purchase orders found.")
        return

    for po in purchase_orders.values():
        print(f"PO {po.po_number} | Vendor: {po.vendor_id} | Date: {po.date_created} | "
              f"Status: {po.status} | Total: ${po.total_cost:.2f}")


def mark_po_received(products, purchase_orders):
    """Mark a PO as received and update inventory."""
    po_number = input("Enter PO number to receive: ").strip()
    po = purchase_orders.get(po_number)
    if not po:
        print("PO not found.")
        return

    if po.status == "RECEIVED":
        print("This PO has already been received.")
        return

    for item in po.items:
        product = products.get(item["product_id"])
        if product:
            product.quantity_in_stock += item["quantity"]
        else:
            print(f"Warning: Product {item['product_id']} not found; cannot update inventory.")

    po.mark_received()
    print(f"PO {po_number} marked as RECEIVED and inventory updated.")
