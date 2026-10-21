SELECT p.ProductName,
SUM(o.Quantity) AS TotalQuantity
FROM Orders o Join Products p
ON p.ProductID = o.ProductID
GROUP BY o.ProductID
LIMIT 1;