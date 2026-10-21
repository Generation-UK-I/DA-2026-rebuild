SELECT p.ProductName, SUM(o.Total) AS TotalRevenue
FROM Orders o
JOIN Products p
ON o.ProductID = p.ProductID
GROUP BY p.ProductName;