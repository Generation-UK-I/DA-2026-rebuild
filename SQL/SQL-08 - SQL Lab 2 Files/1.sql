SELECT c.CustomerName, SUM(o.Total) AS TotalSales
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY o.CustomerID, c.CustomerName;