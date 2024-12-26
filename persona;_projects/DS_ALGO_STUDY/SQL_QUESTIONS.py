"""
get emp_id where name starts with A


SELECT
CASE
 WHEN A<0 THEN "Negative"
 WHEN A>0 THEN "Positive"
 WHEN A=0 THEN "Zero"
 ELSE "Invalid"
END AS A
FROM(
SELECT (A+B+C) AS A
FROM NUMBERS) AS tab;


"""

"""
SELECT COUNT(ID) as A from WORKERS group by DailyWage*DaysWorked Desc limit 1; 

count total number of workers getting highest salary 

"""

"""
select a.Id as "Id" from Books as a JOIN BoughtsBooks as b on a.Id = b.BooksId group by b2.BooksId having count(b2.id) >=3;

SELECT BooksId as Id from BoughtBooks group by BooksId having count(BooksId) >=3;

get the books id for the famous books. famous books are those whose has bought by more than three cust.

"""