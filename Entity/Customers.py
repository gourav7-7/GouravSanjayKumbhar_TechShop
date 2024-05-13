class Customers:
    def __init__(self):
        self._CustomerID = ''
        self._FirstName = ''
        self._LastName = ''
        self._Email = ''
        self._Phone ='' 
        self._Address = ''

    
    def getCustomerID(self):
        return self._CustomerID

    def setCustomerID(self, CustomerID):
        self._CustomerID = CustomerID

    def getFirstName(self):
        return self._FirstName

    def setFirstName(self, FirstName):
        self._FirstName = FirstName

    def setEmail(self,Email):
        self._Email = Email

    def setPhone(self, Phone):
        self._Phone = Phone

    def setAddress(self,Address):
        self._Address = Address

    def setLastName(self,LastName):
        self._LastName = LastName

    def getLastName(self):
        return self._LastName
    
    def setPhoneNumber(self,PhoneNumber):
        self._Phone = PhoneNumber

    def getPhoneNumber(self):
        return self._Phone 

    