from abc import ABC, abstractmethod

class IOrderService(ABC):
    @abstractmethod
    def calculate_total_amount(self, order_id):
        pass

    @abstractmethod
    def get_order_details(self, order_id):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def create_order(self, order_details):
        pass

    @abstractmethod
    def update_order(self, order_id, new_order_details):
        pass

    @abstractmethod
    def calculate_subtotal(self, order_detail_id):
        pass

    @abstractmethod
    def get_order_detail_info(self):
        pass

    @abstractmethod
    def update_quantity_by_order_id(self, order_detail_id, new_quantity):
        pass

    @abstractmethod
    def add_discount(self, order_detail_id, discount_amount):
        pass
