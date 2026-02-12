SELECT Name, Salary
FROM (
    SELECT 
        Name, 
        Salary, 
        DENSE_RANK() OVER (ORDER BY Salary DESC) as Rank
    FROM Employees
) RankedEmployees
WHERE Rank = 1;
