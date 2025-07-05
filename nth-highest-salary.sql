CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT IFNULL( (SELECT salary FROM (
            SELECT DISTINCT salary
            FROM Employee
        ) as E ORDER BY salary DESC LIMIT 1 OFFSET N), NULL) as NthHighestSalary
    );
END
