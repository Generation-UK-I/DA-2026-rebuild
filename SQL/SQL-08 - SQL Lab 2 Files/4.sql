SELECT OrderDate, count(OrderDate)
FROM Orders
GROUP BY OrderDate;