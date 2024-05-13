from abc import ABC, abstractmethod

class IProductService(ABC):
    @abstractmethod
    def get_products(self):
        """Abstract method to get all products."""
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        """Abstract method to get a product by its ID."""
        pass

    @abstractmethod
    def add_product(self, product):
        """Abstract method to add a new product."""
        pass

    @abstractmethod
    def update_product(self, product):
        """Abstract method to update an existing product."""
        pass

    @abstractmethod
    def delete_product(self, product_id):
        """Abstract method to delete a product."""
        pass
