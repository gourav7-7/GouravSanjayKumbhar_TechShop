from abc import ABC, abstractmethod

class IInventoryService(ABC):
    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def get_quantity_in_stock(self):
        pass

    @abstractmethod
    def add_to_inventory(self, quantity):
        pass

    @abstractmethod
    def remove_from_inventory(self, quantity):
        pass

    @abstractmethod
    def update_stock_quantity(self, new_quantity):
        pass

    @abstractmethod
    def is_product_available(self, quantity_to_check):
        pass

    @abstractmethod
    def get_inventory_value(self):
        pass

    @abstractmethod
    def list_low_stock_products(self):
        pass

    @abstractmethod
    def list_out_of_stock_products(self):
        pass

    @abstractmethod
    def list_all_products(self):
        pass
