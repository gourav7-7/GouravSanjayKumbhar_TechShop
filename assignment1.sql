-- TASK 1
create database TechShop;
use TechShop;

create table Customers(
CustomerID int primary key not null,
FirstName varchar(50),
LastName varchar(50),
Email varchar(50) check (Email like '%@gmail.com'),
Phone varchar(50) unique ,
Address varchar(50));

create table Products(
ProductID int not null primary key,
ProductName varchar(50),
Description varchar(100),
Price float);

create table Orders(
OrderID int not null primary key,
CustomerID int references Customers(CustomerID) on delete cascade,
OrderDate date,
TotalAmonut int);

create table OrderDetails(
orderDetailID int not null primary key,
OrderID int references Orders(OrderID) on delete cascade,
ProductID int references Products(ProductID) on delete cascade,
Quantity int);

create table Inventory(
InventoryID int not null primary key,
ProductID int references Products(ProductID) on delete cascade,
QuantityInStock int,
LastStockUpdate date);

select * from customers where firstname = 'jane';

insert into Customers
values
(1, 'John', 'Doe', 'johndoe@gmail.com', '1234567890', 'Amsterdam') ,
(2, 'Jane', 'Smith', 'janesmith@gmail.com', '9876543210', 'Amsterdam'),
(3,  'Robert','Johnson', 'robert@gmail.com', '5551234567', 'New York'),
(4, 'Sarah', 'Brown', 'sarah@gmail.com', '5441234567', 'London'),
(5, 'David', 'Lee', 'david@gmail.com', '6651234567', 'Paris'),
(6, 'Laura', 'Hall', 'laura@gmail.com', '5771234567', 'Sydney'),
(7, 'Michael', 'Davis', 'michael@gmail.com', '8851234567', 'Mumbai'),
(8, 'Emma', 'Wilson', 'emma@gmail.com', '5551234599', 'Pune'),
(9,  'William', 'Taylor', 'william@gmail.com', '5552034567', 'Benglore'),
(10, 'Olivia', 'Adams', 'olivia@gmail.com', '755454567', 'Hyderabad');

select * from Customers;

insert into  Products (ProductID, ProductName, Description, Price)
values
(1, 'Laptop', 'High-performance laptop', 90000),

(2, 'Smartphone', 'Latest smartphone model', 50000),
(3, 'tablet', 'Portable tablet device', 40000),
(4, 'Desktop PC', 'Powerful desktop computer', 200000),
(5, 'Wireless Mouse', 'Ergonomic wireless mouse', 1000),
(6, 'Bluetooth Headphones', 'Noise-canceling headphones', 3500),
(7, 'External Hard Drive', '1TB external hard drive', 10000),
(8, 'Smartwatch', 'Fitness tracking smartwatch', 8000),
(9, 'Printer', 'All-in-one printer', 34000),
(10, 'Gaming Console', 'Next-gen gaming console', 56000);



insert into  Orders (OrderID, CustomerID, OrderDate, TotalAmonut)
values
(1, 1, '2024-04-3', 90000),
(2, 2, '2024-04-4', 50000),
(3, 3, '2024-04-5', 40000),
(4, 4, '2024-04-6', 200000),
(5, 5, '2024-04-7', 2000),
(6, 6, '2024-04-8', 3500),
(7, 7, '2024-04-9', 10000),
(8, 10, '2024-04-10', 16000),
(9, 9, '2024-04-11', 34000),
(10, 8, '2024-04-12', 56000);


insert into OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
values
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 3, 1),
(4, 4, 4, 1),
(5, 5, 5, 2),
(6, 6, 6, 1),
(7, 7, 7, 1),
(8, 8, 8, 2),
(9, 9, 9, 1),
(10, 10, 10, 1);



insert into Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate)
values
(1, 1, 10, '2024-04-12'),
(2, 2, 20, '2024-04-12'),
(3, 3, 15, '2024-04-12'),
(4, 4, 5, '2024-04-12'),
(5, 5, 50, '2024-04-12'),
(6, 6, 20, '2024-04-12'),
(7, 7, 30, '2024-04-12'),
(8, 8, 10, '2024-04-12'),
(9, 9, 8, '2024-04-12'),
(10, 10, 3, '2024-04-12');


--TASK 2
--1. Write an SQL query to retrieve the names and emails of all customers.  
select FirstName,LastName,Email from Customers;

--2.Write an SQL query to list all orders with their order dates and corresponding customer names.
select O.OrderID,O.OrderDate,concat((C.firstname),' ',(C.lastname)) as Name
from Orders as O 
left join Customers as C
on O.CustomerID=C.CustomerID;

/*3. Write an SQL query to insert a new customer record 
into the "Customers" table. Include customer information 
such as name, email, and address.*/
insert into Customers values
(11, 'Jacob', 'cappuccin', 'jacobcap@gmail.com', '741852963', 'Sydney');

--4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table by increasing them by 10%.
update Products
set price = price+(price*0.10)


--5. Write an SQL query to delete a specific order and its associated order details from the "Orders" and "OrderDetails" tables. Allow users to input the order ID as a parameter. 
delete from Orders where OrderID=3;


--6. Write an SQL query to insert a new order into the "Orders" table. Include the customer ID, order date, and any other necessary information.
insert into Orders values(3,3,'2024-04-05',54000)
select * from Orders


--7. Write an SQL query to update the contact information (e.g., email and address) of a specific customer in the "Customers" table. Allow users to input the customer ID and new contact information. 
update Customers
set email = 'jacobc123@gmail.com' , address = 'London' 
where customerID = 11


--8. Write an SQL query to recalculate and update the total cost of each order in the "Orders" table based on the prices and quantities in the "OrderDetails" table. 
update Orders 
set TotalAmonut = OC.TotalCost
from Orders
join (
    select OrderID, sum(Quantity * Price) AS TotalCost
    from OrderDetails as OD
    join Products as P on OD.ProductID = P.ProductID
    group by  OrderID
) as OC on Orders.OrderID = OC.OrderID;



--9. Write an SQL query to delete all orders and their associated order details for a specific customer from the "Orders" and "OrderDetails" tables. Allow users to input the customer ID as a parameter.
delete from Orders
where CustomerID = 5


--10. Write an SQL query to insert a new electronic gadget product into the "Products" table, including product name, category, price, and any other relevant details. 
insert into Products values(11, 'Calculator', 'Scientefic calculator', 500);


--11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from "Pending" to "Shipped"). Allow users to input the order ID and the new status.


--12. Write an SQL query to calculate and update the number of orders placed by each customer in the "Customers" table based on the data in the "Orders" table.
alter table Customers
add NumOrders int;

update Customers 
set NumOrders = OrderCounts.NumOrders
from Customers
join (
    select CustomerID, COUNT(*) as NumOrders
    from Orders
    group by  CustomerID
) as OrderCounts on Customers.CustomerID = OrderCounts.CustomerID;

--TASK 3

/*
1. Write an SQL query to retrieve a list of all orders along with customer information (e.g., 
customer name) for each order.
*/
select O.*,C.FirstName,C.LastName from Orders as O
left join Customers as C on O.CustomerID = C.CustomerID 



/*
2. Write an SQL query to find the total revenue generated by each electronic gadget product. 
Include the product name and the total revenue.
*/
select P.ProductName, sum(OD.Quantity*P.Price)as Total_Revenue from OrderDetails as OD 
join Products as P on OD.ProductID = P.ProductID
group by P.ProductName

/*
3. Write an SQL query to list all customers who have made at least one purchase. Include their 
names and contact information. 
*/
select C.FirstName,C.LastName,C.Email from Customers as C 
right join Orders as O on C.CustomerID = O.CustomerID
where O.CustomerID is not null

/*
4. Write an SQL query to find the most popular electronic gadget, which is the one with the highest 
total quantity ordered. Include the product name and the total quantity ordered. 
*/
select OD.Quantity,P.ProductName from OrderDetails as OD
join Products as P on OD.ProductID = P.ProductID
order by OD.Quantity desc
offset 0 rows
fetch next 1 rows only

select productName from Products where ProductID = (
select ProductID from OrderDetails order by Quantity desc
offset 0 rows
fetch next 1 rows only)


/*
5. Write an SQL query to retrieve a list of electronic gadgets along with their corresponding 
categories. 
*/


/*
6. Write an SQL query to calculate the average order value for each customer. Include the 
customer's name and their average order value. 
*/
select C.FirstName,C.LastName, avg(O.TotalAmonut)as Avg_Val from Customers as C
join Orders as O on C.CustomerID = O.CustomerID
group by C.FirstName,C.LastName


/*
7. Write an SQL query to find the order with the highest total revenue. Include the order ID, 
customer information, and the total revenue. 
*/
select O.OrderID,C.FirstName,C.LastName,C.Email,O.TotalAmonut from Orders as O 
join Customers as C on O.CustomerID = C.CustomerID
order by O.TotalAmonut desc
offset 0 rows
fetch next 1 rows only


/*
8. Write an SQL query to list electronic gadgets and the number of times each product has been 
ordered. 
*/
select P.ProductName, count(OD.ProductID) from Products as P
left join OrderDetails as OD on P.ProductID = OD.ProductID
group by P.ProductName

/*
9. Write an SQL query to find customers who have purchased a specific electronic gadget product. 
Allow users to input the product name as a parameter. 
*/
declare @prod varchar(20)= 'laptop'

select C.* from Customers as C 
join Orders as O on C.CustomerID = O.CustomerID
join OrderDetails as OD on OD.OrderID = O.OrderID
join Products as P on P.ProductID = OD.ProductID
where P.ProductName = @prod

/*
10. Write an SQL query to calculate the total revenue generated by all orders placed within a 
specific time period. Allow users to input the start and end dates as parameters.
*/
declare @start date = '2024-04-06'
declare @end date = '2024-04-11'

select sum([TotalAmonut]) from Orders
where OrderDate between @start and @end 

--TASK 4
--1. Write an SQL query to find out which customers have not placed any orders. 
select * from Customers 
where CustomerID not in (select CustomerID from Orders)

--2. Write an SQL query to find the total number of products available for sale.  
select count(ProductID) from Products 
where productID in (
select ProductID from Inventory where QuantityInStock >1)

--3. Write an SQL query to calculate the total revenue generated by TechShop. 
select sum([TotalAmonut]) from Orders


--4. Write an SQL query to calculate the average quantity ordered for products in a specific category. Allow users to input the category name as a parameter.


--5. Write an SQL query to calculate the total revenue generated by a specific customer. Allow users to input the customer ID as a parameter.
declare @custID int = 3

select sum(TotalAmonut) from Orders where CustomerID = @custID
. 
--6. Write an SQL query to find the customers who have placed the most orders. List their names and the number of orders they've placed. 
SELECT C.FirstName, C.LastName, OrderCount
FROM Customers AS C
JOIN (
    SELECT top 1 CustomerID, COUNT(OrderID) AS OrderCount
    FROM Orders
    GROUP BY CustomerID
    ORDER BY OrderCount DESC
) AS MaxOrders ON C.CustomerID = MaxOrders.CustomerID;



--7. Write an SQL query to find the most popular product category, which is the one with the highest total quantity ordered across all orders. 
select ProductName from Products where productID in
(select top 1 ProductID from OrderDetails
order by Quantity desc)

--8. Write an SQL query to find the customer who has spent the most money (highest total revenue) 
select * from Customers where CustomerID in (
select top 1 CustomerID from Orders 
order by TotalAmonut desc)


/*
9. Write an SQL query to calculate the average order value (total revenue divided by the number of 
orders) for all customers. */
select C.*,avgval from Customers as C join (
select CustomerID,(sum(TotalAmonut) / count(OrderID)) as avgval from Orders
group by CustomerID) as avgordval on C.CustomerID = avgordval.CustomerID