from datetime import datetime

class Product:
    """Represents a product in inventory."""

    def __init__(self, product_id, name, category, quantity_in_stock,
                 reorder_level, reorder_quantity, unit_price,
                 vendor_id, active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = active

    def is_low_stock(self):
        """Return True if quantity is at or below reorder level."""
        return self.quantity_in_stock <= self.reorder_level

    def to_dict(self):
        """Convert Product to a serializable dict."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "quantity_in_stock": self.quantity_in_stock,
            "reorder_level": self.reorder_level,
            "reorder_quantity": self.reorder_quantity,
            "unit_price": self.unit_price,
            "vendor_id": self.vendor_id,
            "active": self.active
        }

    @staticmethod
    def from_dict(data):
        """Create Product from dict."""
        return Product(
            data["product_id"],
            data["name"],
            data["category"],
            data["quantity_in_stock"],
            data["reorder_level"],
            data["reorder_quantity"],
            data["unit_price"],
            data["vendor_id"],
            data.get("active", True)
        )


class Vendor:
    """Represents a vendor/supplier."""

    def __init__(self, vendor_id, name, contact_name, phone, email, address):
        self.vendor_id = vendor_id
        self.name = name
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        """Convert Vendor to a serializable dict."""
        return {
            "vendor_id": self.vendor_id,
            "name": self.name,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        """Create Vendor from dict."""
        return Vendor(
            data["vendor_id"],
            data["name"],
            data["contact_name"],
            data["phone"],
            data["email"],
            data["address"]
        )


class PurchaseOrder:
    """Represents a purchase order."""

    def __init__(self, po_number, vendor_id, date_created=None,
                 items=None, total_cost=0.0, status="OPEN"):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.date_created = date_created or datetime.now().strftime("%Y-%m-%d")
        self.items = items or []
        self.total_cost = total_cost
        self.status = status

    def add_item(self, product_id, quantity, unit_price):
        """Add an item to the PO and update total."""
        line_total = quantity * unit_price
        self.items.append({
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": line_total
        })
        self.total_cost += line_total

    def mark_received(self):
        """Mark PO as received."""
        self.status = "RECEIVED"

    def to_dict(self):
        """Convert PurchaseOrder to a serializable dict."""
        return {
            "po_number": self.po_number,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created,
            "items": self.items,
            "total_cost": self.total_cost,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """Create PurchaseOrder from dict."""
        return PurchaseOrder(
            data["po_number"],
            data["vendor_id"],
            data["date_created"],
            data["items"],
            data["total_cost"],
            data["status"]
        )
