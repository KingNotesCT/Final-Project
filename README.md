# Inventory and Purchase Order System

## Project Description
This program manages products, vendors, and purchase orders for a small business. It allows users to add, edit, and deactivate products and vendors, create and receive purchase orders, and generate detailed inventory reports. The system is menu-driven and stores all data in a JSON file for easy saving and loading.

## Features
- Add, view, edit, and deactivate products
- Add, view, and edit vendors
- Create and receive purchase orders
- Display low-stock products
- Generate reports:
  - Full inventory report
  - Low-stock report
  - Total inventory value report
  - Open purchase orders report
  - Reorder suggestions report (extra feature)
- Save and load data automatically from JSON

## Required Files
- `main.py` — main program and menu system  
- `models.py` — class definitions for Product, Vendor, and PurchaseOrder  
- `inventory_manager.py` — functions for managing products, vendors, and purchase orders  
- `file_manager.py` — handles loading and saving data to JSON  
- `reports.py` — generates inventory and purchase order reports  
- `sample_data.json` — stores all product, vendor, and purchase order data  

## Instructions for Running the Program
1. Place all files in the same folder.  
2. Open a terminal or command prompt in that folder.  
3. Run the program using:
   ```bash
   python main.py
