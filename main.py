from file_manager import load_data, save_data
from inventory_manager import (
    add_product, view_all_products, edit_product, deactivate_product,
    display_low_stock_products, add_vendor, view_all_vendors,
    edit_vendor, create_purchase_order, view_purchase_orders,
    mark_po_received
)
from reports import (
    full_inventory_report, low_stock_report,
    total_inventory_value_report, open_purchase_orders_report,
    reorder_suggestions_report
)

def main_menu():
    """Main menu loop."""
    products, vendors, purchase_orders = load_data()

    while True:
        print("\n=== INVENTORY & PURCHASE ORDER SYSTEM ===")
        print("1. Product Management")
        print("2. Vendor Management")
        print("3. Purchase Orders")
        print("4. Reports")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            product_menu(products, vendors)
        elif choice == "2":
            vendor_menu(vendors)
        elif choice == "3":
            po_menu(products, vendors, purchase_orders)
        elif choice == "4":
            reports_menu(products, purchase_orders)
        elif choice == "5":
            save_data(products, vendors, purchase_orders)
        elif choice == "6":
            save_data(products, vendors, purchase_orders)
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


def product_menu(products, vendors):
    """Product management submenu."""
    while True:
        print("\n--- Product Management ---")
        print("1. Add product")
        print("2. View all products")
        print("3. Edit product")
        print("4. Deactivate product")
        print("5. Display low-stock products")
        print("6. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_product(products, vendors)
        elif choice == "2":
            view_all_products(products)
        elif choice == "3":
            edit_product(products)
        elif choice == "4":
            deactivate_product(products)
        elif choice == "5":
            display_low_stock_products(products)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def vendor_menu(vendors):
    """Vendor management submenu."""
    while True:
        print("\n--- Vendor Management ---")
        print("1. Add vendor")
        print("2. View all vendors")
        print("3. Edit vendor")
        print("4. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_vendor(vendors)
        elif choice == "2":
            view_all_vendors(vendors)
        elif choice == "3":
            edit_vendor(vendors)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def po_menu(products, vendors, purchase_orders):
    """Purchase order submenu."""
    while True:
        print("\n--- Purchase Orders ---")
        print("1. Create purchase order")
        print("2. View purchase orders")
        print("3. Receive shipment")
        print("4. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_purchase_order(products, vendors, purchase_orders)
        elif choice == "2":
            view_purchase_orders(purchase_orders)
        elif choice == "3":
            mark_po_received(products, purchase_orders)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def reports_menu(products, purchase_orders):
    """Reports submenu."""
    while True:
        print("\n--- Reports ---")
        print("1. Full inventory report")
        print("2. Low-stock report")
        print("3. Total inventory value report")
        print("4. Open purchase orders report")
        print("5. Reorder suggestions (unique feature)")
        print("6. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            full_inventory_report(products)
        elif choice == "2":
            low_stock_report(products)
        elif choice == "3":
            total_inventory_value_report(products)
        elif choice == "4":
            open_purchase_orders_report(purchase_orders)
        elif choice == "5":
            reorder_suggestions_report(products)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
