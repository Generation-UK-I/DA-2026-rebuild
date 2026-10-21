SELECT c.CustomerName, SUM(o.Total) as TotalSales
FROM Customers c
JOIN Orders o ON o.CustomerID = c.CustomerID
GROUP BY o.CustomerID
ORDER BY TotalSales DESC
LIMIT 3;