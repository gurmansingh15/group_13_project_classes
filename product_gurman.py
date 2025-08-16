class Product:
    
    categories_list = ["Electronics", "Clothing", "Home", "Grocery", "Books", "Toys", 
                "Sports", "Beauty", "Automotive", "Others"]

    # This is a class for products in the inventory system.

    def __init__(self, product_id, name, category, quantity = 0, price = 0.0, reorder_level = 0):
        # The class attributes
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.reorder_level = reorder_level
    
    #Getters for Attributes
    def get_product_id(self):
        return self.product_id
    
    def get_name(self):
        return self.name 
    
    def get_category(self):
        return self.category
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price
    
    def get_reorder_level(self):
        return self.reorder_level
    
    # Additional Methods
    def get_category_name(self):
        if 0 <= self.category <= 9:
            self.category = Product.categories_list[self.category]
        return self.category

    def needs_restock(self):
        if self.quantity <= self.reorder_level:
            return True
    
    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            return True
    
    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:
            return False
    
    # Setters for Attributes
    def set_product_id(self, new_product_id):
        self.product_id = new_product_id
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_category(self, new_category):
        self.category = new_category
    
    def set_price(self, new_price):
        self.price = new_price
    
    def set_reorder_level(self, new_reorder_level):
        self.reorder_level = new_reorder_level

    # String Output
    def __str__(self):
        return f"{self.product_id} {self.name} {self.category} {self.quantity} ${self.price}"


