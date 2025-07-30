# Write your MySQL query statement below
SELECT Employee.name as Employee FROM Employee INNER JOIN Employee as e1 ON  Employee.managerId = e1.id WHERE Employee.salary > e1.salary;
