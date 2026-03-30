# Write your MySQL query statement below
SELECT employee.name AS Employee
FROM Employee employee
JOIN Employee manager
    ON employee.managerID = manager.id and employee.salary >= manager.salary
