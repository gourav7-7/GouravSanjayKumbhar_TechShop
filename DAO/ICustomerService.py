from abc import ABC, abstractmethod

class ICustomerService(ABC):

    @abstractmethod
    def GetCustomers(self):
        pass

    @abstractmethod
    def GetCustomerById(self, customerID):
        pass

    @abstractmethod
    def UpdateCustomer(self):
        pass

    @abstractmethod
    def DeleteCustomer(self):
        pass

    @abstractmethod
    def RegisterCustomer(self):
        pass
