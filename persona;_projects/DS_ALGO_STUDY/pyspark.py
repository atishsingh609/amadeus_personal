import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName('sparkdf').getOrCreate()

# list  of college data with  dictionary
# with three  dictionaries
data = [{'student_id': 12, 'name': 'sravan', 'address': 'kakumanu'},
        {'student_id': 14, 'name': 'jyothika', 'address': 'tenali'},
        {'student_id': 11, 'name': 'deepika', 'address': 'repalle'}]

# creating a dataframe
dataframe = spark.createDataFrame(data)

# show data frame
dataframe.show()