""""
1) second highets salary - select max(salary) from employee where salary not in (max(salary) from employee)


2) Rising Temp:

select w1.id as id from Weather as w1, Weather as w2
where datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature


3)Average time of process per macine
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
Output:
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+

select a1.machine_id, ROUND(AVG(a2.timestamp-a1.timestamp), 3) as processing_time from Activity a1 join activity a2
on a1.process_id = a2.process_id
and a1.machine_id  = a2.machine_id
and a1.timestamp < a2.timestamp
group by a1.machine_id


"""