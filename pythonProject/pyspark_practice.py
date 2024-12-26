from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import  Window
spark = SparkSession.builder.appName("pyspark_practice").getOrCreate()

cols = ["col_1", "col_2", "col_3"]

data = [("x", "y", "z", "a", "b"), (6,7,8,9,10), (11,12,13,14,25)]

df = spark.createDataFrame(data=data, schema=cols)

window_sum = Window.partitionBy("col_1").orderBy("col_3")

df.withColumn("sum_col_3", sum(col("col_3")).over(window_sum))
df.withColumn("row_number", row_number().over(window_sum))
df.withColumn("rank", rank().over(window_sum))
df.withColumn("dense_rank", dense_rank().over(window_sum))
df.withColumn("lag", lag("col_1").over(window_sum))
df.withColumn("lead", lead("col_1").over(window_sum))

csv_data = spark.read.csv("some_file.csv", inferSchema=True, header=True)

csv_data.withColumn("abc", coalesce(col("abc"), 0))
csv_data.asDict()
df.groupBy("col_1").mean().show()

df.na.drop(how="any")
df.na.drop(how="all")
df.dropna(how="any")



df.show()



lst = [1,2,3,4,5,6,7]

rdd = spark.sparkContext.parallelize(lst)

squared = rdd.map(lambda x : x*x)
flat_map = rdd.flatMap(lambda x : x.split())
squared.collect()

rdd_sum = rdd.reduce(lambda x,y : x+y)

new_window = Window.partitionBy("col_1").orderBy("col_3")
df = df.groupBy("col_1").agg(collect_list("col_3").alias("list_values"))


from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, count, collect_list

# Initialize SparkSession
spark = SparkSession.builder.master("local").appName("AggregationExamples").getOrCreate()

# Example data
data = [
    (1, "Alice", 5000),
    (2, "Bob", 4000),
    (3, "Alice", 3000),
    (4, "Bob", 7000),
    (5, "Alice", 8000),
    (6, "Charlie", 10000)
]
columns = ["id", "name", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)


df.sort(desc("id"))
# Example 1: Group by 'name' and calculate total and average salary
result1 = df.groupBy("name").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("average_salary"),
    count("salary").alias("count"),
    collect_list("salary").alias("salaries")
)
result1.show()

# Example 2: Group by a computed column (e.g., salary range)
from pyspark.sql.functions import when
df = df.withColumn("salary_range", when(df.salary < 5000, "Low").otherwise("High"))
result2 = df.groupBy("salary_range").agg(
    count("id").alias("count"),
    max("salary").alias("max_salary")
)
result2.show()



from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.textFile("/apps/sparkbyexamples/src/pyspark-examples/data.txt")

for element in rdd.collect():
    print(element)

#Flatmap
rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)
#map
rdd3=rdd2.map(lambda x: (x,1))
for element in rdd3.collect():
    print(element)
#reduceByKey
rdd4=rdd3.reduceByKey(lambda a,b: a+b)
for element in rdd4.collect():
    print(element)
#map
rdd5 = rdd4.map(lambda x: (x[1],x[0])).sortByKey()
for element in rdd5.collect():
    print(element)
#filter
rdd6 = rdd5.filter(lambda x : 'a' in x[1])
for element in rdd6.collect():
    print(element)









