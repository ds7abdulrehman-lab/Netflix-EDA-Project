Create database sql_practice;
use sql_practice;
create table if not exists employees(
id int primary key,
name varchar (50),
department varchar(50),
salary varchar(50),
hire_date date);

insert into employees(
id, name, department, salary, hire_date)
VALUES
(1, 'Alice', 'HR', 5000, '2020-01-10'),
(2, 'Bob', 'IT', 6500, '2019-03-02'),
(3, 'Carol', 'IT', 7000, '2021-07-15'),
(4, 'David', 'Finance', 5500, '2018-11-23'),
(5, 'Emma', 'HR', 5200, '2022-04-01'),
(6, 'Frank', 'IT', 7200, '2020-06-11'),
(7, 'Grace', 'Marketing', 4800, '2019-10-19'),
(8, 'Henry', 'Finance', 6100, '2021-01-05'),
(9, 'Irene', 'HR', 5300, '2022-09-09'),
(10, 'Jack', 'IT', 6800, '2017-02-14'),
(11, 'Karen', 'Marketing', 4900, '2020-12-12'),
(12, 'Leo', 'Finance', 6300, '2023-02-01'),
(13, 'Mia', 'IT', 7100, '2019-05-25'),
(14, 'Noah', 'HR', 5400, '2021-11-30'),
(15, 'Olivia', 'Marketing', 5100, '2018-08-27'),
(16, 'Paul', 'IT', 6900, '2022-03-03'),
(17, 'Quinn', 'Finance', 6000, '2017-12-15'),
(18, 'Rosa', 'HR', 5600, '2020-09-21'),
(19, 'Sam', 'IT', 7300, '2023-06-18'),
(20, 'Tina', 'Marketing', 5200, '2019-04-10');

select * from employees;

select id, name, salary
from employees;

select * from employees
where department = "IT";

select * from employees
where salary > 6000;

select * from employees
where hire_date > '2020-12-30';

select * from employees
where department = "HR" and salary > 5200;

select * from employees
where department  <> "IT";

select * from employees
where salary >=5000 and salary <= 6000;

select * from employees
where name like('A%') or name like ('B%');

select * from employees
where hire_date between '2020-01-01' and '2021-12-31';

select * from employees
order by salary desc;

select * from employees
order by hire_date desc;

select * from employees
order by salary desc
limit 5;

select * from employees
order by department ASC, salary desc;

select count(id)
from employees;

select max(salary) as comp_highest
from employees;

select min(salary) as comp_minimum
from employees;

select avg(salary) as average_salary
from employees;

select sum(salary) as total_monthly
from employees;

select department, count(department)
from employees
group by department;

select department, avg(salary) as department_average
from employees
group by department;

select department, sum(salary) as department_expense
from employees
group by department;

select department, max(salary) as max_department
from employees
group by department;

select department, avg(salary) 
from employees
group by department 
having avg(salary) > 6000;


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    manager VARCHAR(50)
);


INSERT INTO departments (department_id, department_name, manager) VALUES
(1, 'HR', 'Sophia'),
(2, 'IT', 'Michael'),
(3, 'Finance', 'James'),
(4, 'Marketing', 'Olivia'),
(5, 'Sales', 'Daniel'),
(6, 'Operations', 'Emma'),
(7, 'Customer Support', 'Liam'),
(8, 'Legal', 'Charlotte'),
(9, 'R&D', 'Noah'),
(10, 'Logistics', 'Ava');

select avg(salary)
from employees;

select id, name as employee_name, salary
from employees
where salary > (select avg(salary)
from employees);

select department, avg(salary)
from employees
group by department;

select e.id, e.name as employee_name, e.salary
from employees e 
inner join( select department, avg(salary) as average
from employees
group by department) average_salary
on average_salary.department = e.department and average_salary.average < e.salary;

select department 
from employees
where name = "Alice";

select name as employee, id, salary
from employees
where department in (select department 
from employees
where name = "Alice");

select max(salary)
from employees;

select id, name, salary
from employees
where salary =(
select max(salary)
from employees
where salary < (select max(salary)
from employees)
);
use sql_practice;

select name, salary,
dense_rank () over(order by salary desc) as ranking
from employees;

select name, salary
from (
select name, salary,
dense_rank () over(order by salary desc) as ranking
from employees
) rnk
where ranking =2;

select id,name, salary,
row_number() over (order by salary desc) as ranking
from employees
limit 3;

select id, name, salary, ranking
from (select id,name, salary,
row_number() over (order by salary desc) as ranking
from employees) rnk
limit 3;



select id, name, salary, ranking
from (select id, name, salary,
rank () over(order by salary desc) as ranking
 from employees) rnk
 where ranking between 1 and 3;
 
 

 
 select id, name, salary,
 case 
 when salary < 5500 then 'Low'
 when salary between 5500 and 7000 then 'Medium'
 else 'High'
 end as salary_level
 from employees;
 
 select id, name, department,
 case
	when hire_date >2021-12-31 then 'Junior'
    when hire_date between '2019-01-01' and '2021-12-31' then 'Mid'
    else 'Senior'
    end as Tenure
    from employees;
    
select department, Tenure, count(Tenure)
    from (
		select id, name, department,
			case
				when hire_date >'2021-12-31' then 'Junior'
				when hire_date between '2019-01-01' and '2021-12-31' then 'Mid'
				else 'Senior'
			end as Tenure
		from employees) ten
    group by department, Tenure;
    
    
    select id, name, department,
			case
				when hire_date >'2021-12-31' then 'Junior'
				when hire_date between '2019-01-01' and '2021-12-31' then 'Mid'
				else 'Senior'
			end as Tenure
		from employees;
        
select id, name, salary, department, Tenure,
	dense_rank() over(partition by department order by salary desc) as dept_salary
from ( select id, name, department,salary,
			case
				when hire_date >'2021-12-31' then 'Junior'
				when hire_date between '2019-01-01' and '2021-12-31' then 'Mid'
				else 'Senior'
			end as Tenure
		from employees ) rnk;
	
    
select department, count(*) as top_employees_count
from( select id, name, salary, department, Tenure,
	dense_rank() over(partition by department order by salary desc) as dept_salary
from ( select id, name, department,salary,
			case
				when hire_date >'2021-12-31' then 'Junior'
				when hire_date between '2019-01-01' and '2021-12-31' then 'Mid'
				else 'Senior'
			end as Tenure
		from employees ) rnk
        )ranked 
where dept_salary <=2
group by department, Tenure;        

select id, name, department, salary,
case 
when salary < 5500 then 'Low'
when salary between 5500 and 7000 then 'Medium'
else 'High'
end as salary_cat
from employees;

select department, salary_level, count(*) as employee_count
from (
	select id, name, department, salary,
		case 
			when salary < 5500 then 'Low'
			when salary between 5500 and 7000 then 'Medium'
			else 'High'
		end as salary_level
	from employees
    ) rnk
group by department, salary_level
order by department, salary_;

select id, name, department, salary,
row_number() over(partition by department order by salary desc) as salary_dept
from (
select id, name, department, salary,
		case 
			when salary < 5500 then 'Low'
			when salary between 5500 and 7000 then 'Medium'
			else 'High'
		end as salary_cat
	from employees
    ) rnk;
