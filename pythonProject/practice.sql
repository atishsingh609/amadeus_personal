-- Create the employee table
-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     dept_id VARCHAR(50),
--     manager_id INT,
--     salary DECIMAL(10, 2),
--     expertise VARCHAR(20)
-- );
--
-- -- Insert the employee data
-- INSERT INTO employees (employee_id, first_name, last_name, dept_id, manager_id, salary, expertise) VALUES
-- (100, 'John', 'White', 'IT', 103, 120000, 'Senior'),
-- (101, 'Mary', 'Danner', 'Account', 109, 80000, 'Junior'),
-- (102, 'Ann', 'Lynn', 'Sales', 107, 140000, 'Semisenior'),
-- (103, 'Peter', 'O''connor', 'IT', 110, 130000, 'Senior'),
-- (106, 'Sue', 'Sanchez', 'Sales', 107, 110000, 'Junior'),
-- (107, 'Marta', 'Doe', 'Sales', 110, 180000, 'Senior'),
-- (109, 'Ann', 'Danner', 'Account', 110, 90000, 'Senior'),
-- (110, 'Simon', 'Yang', 'CEO', NULL, 250000, 'Senior'),
-- (111, 'Juan', 'Graue', 'Sales', 102, 37000, 'Junior');


-- select * from employees;


-- select employees.first_name, employees.last_name, employees.dept_id, employees.manager_id, employees.salary,
--        employees.expertise, rank() over (partition by employees.dept_id order by employees.salary desc) as ranking from employees;

-- to get second highest salary in each dept.




select first_name, last_name, dept_id, manager_id, salary from (
    select employees.first_name, employees.last_name, employees.dept_id, employees.manager_id, employees.salary,
       employees.expertise, dense_rank()  over (partition by employees.dept_id order by employees.salary desc) as ranking from employees )
where ranking =2;


WITH temp_table as (
    select employees.first_name, employees.last_name, employees.dept_id, employees.manager_id, employees.salary,
       employees.expertise, ntile(4) over ( order by employees.salary desc) as ntile from employees
)
select first_name, last_name, dept_id, manager_id, salary, ntile from temp_table;

select employees.first_name, employees.dept_id, employees.salary from employees
where salary > (
select avg(employees.salary) over (partition by employees.dept_id) as avg_salary
from employees);


select * from employees where employees.first_name like "[A-Z]%";

select employees.dept_id, employees.salary,
       sum(employees.salary) over (partition by employees.dept_id order by employees.salary rows between unbounded preceding and current row ) as commu_sum
from employees;

