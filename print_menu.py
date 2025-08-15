def print_menu():
    print("Welcome to the Inventory System. Please choose which menu to enter below.\n"
          "\n======= Inventory Menu ======="
          "\n1. Search Products"
          "\n2. Add Products"
          "\n3. Remove Products"
          "\n4. Edit Products"
          "\n5. Sell Products"
          "\n6. Restock Products"
          "\n7. Low Stock Report"
          "\n8. Inventory Summary"
          "\n9. List Products by Category"
          "\n10. Product Index"
          "\n11. Print Products")
    menu_choice = input("\nSelect a menu (1 to 11): ")
    return menu_choice
