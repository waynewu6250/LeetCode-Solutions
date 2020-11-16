CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare a INT;
  set a = N-1;
  RETURN (
      # Write your MySQL query statement below.
     
      SELECT Distinct Salary
      FROM Employee 
      Order by salary
      desc
      limit a,1
  );
END