-- Total Sales

SELECT SUM(Sales) AS TotalSales
FROM sales;

-- Total Profit

SELECT SUM(Profit) AS TotalProfit
FROM sales;

-- Sales By Region

SELECT Region,
       SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region;

-- Profit By Category

SELECT Category,
       SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category;

-- Top Products

SELECT Product,
       SUM(Sales) AS TotalSales
FROM sales
GROUP BY Product
ORDER BY TotalSales DESC
LIMIT 10;

-- Monthly Sales

SELECT strftime('%Y-%m', Date) AS Month,
       SUM(Sales) AS TotalSales
FROM sales
GROUP BY Month
ORDER BY Month;