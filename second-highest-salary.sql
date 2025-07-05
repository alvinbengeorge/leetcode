SELECT IFNULL( (SELECT salary FROM (
    SELECT DISTINCT salary
    FROM Employee
) as E ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) as SecondHighestSalary;
