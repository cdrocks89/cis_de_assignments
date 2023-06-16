"""
(39) Spark Jobs
df:pyspark.sql.dataframe.DataFrame = [firstname: string, lastname: string ... 2 more fields]
+---------+--------+------+------+
|firstname|lastname|gender|salary|
+---------+--------+------+------+
|    James|   Smith|     M|  3000|
|     Anna|    Rose|     F|  4100|
|   Robert|Williams|     M|  6200|
+---------+--------+------+------+

aa
+---------+--------+------+------+-------------+
|firstname|lastname|gender|salary|bonus_percent|
+---------+--------+------+------+-------------+
|    James|   Smith|     M|  3000|          0.3|
|     Anna|    Rose|     F|  4100|          0.3|
|   Robert|Williams|     M|  6200|          0.3|
+---------+--------+------+------+-------------+


+---------+--------+------+------+------------+
|firstname|lastname|gender|salary|bonus_amount|
+---------+--------+------+------+------------+
|    James|   Smith|     M|  3000|       900.0|
|     Anna|    Rose|     F|  4100|      1230.0|
|   Robert|Williams|     M|  6200|      1860.0|
+---------+--------+------+------+------------+

+---------+--------+------+------+---------------+
|firstname|lastname|gender|salary|           name|
+---------+--------+------+------+---------------+
|    James|   Smith|     M|  3000|    James,Smith|
|     Anna|    Rose|     F|  4100|      Anna,Rose|
|   Robert|Williams|     M|  6200|Robert,Williams|
+---------+--------+------+------+---------------+

+---------+--------+------+------+------------+
|firstname|lastname|gender|salary|current_date|
+---------+--------+------+------+------------+
|    James|   Smith|     M|  3000|  2023-06-16|
|     Anna|    Rose|     F|  4100|  2023-06-16|
|   Robert|Williams|     M|  6200|  2023-06-16|
+---------+--------+------+------+------------+

+---------+--------+------+------+-----+
|firstname|lastname|gender|salary|grade|
+---------+--------+------+------+-----+
|    James|   Smith|     M|  3000|    A|
|     Anna|    Rose|     F|  4100|    B|
|   Robert|Williams|     M|  6200|    C|
+---------+--------+------+------+-----+

+---------+------+-----+
|firstname|salary|bonus|
+---------+------+-----+
|    James|  3000|  0.3|
|     Anna|  4100|  0.3|
|   Robert|  6200|  0.3|
+---------+------+-----+

+---------+------+------------+
|firstname|salary|bonus_amount|
+---------+------+------------+
|    James|  3000|       900.0|
|     Anna|  4100|      1230.0|
|   Robert|  6200|      1860.0|
+---------+------+------------+

+---------+------+----------+
|firstname|salary|today_date|
+---------+------+----------+
|    James|  3000|2023-06-16|
|     Anna|  4100|2023-06-16|
|   Robert|  6200|2023-06-16|
+---------+------+----------+

+---------+------+-----+
|firstname|salary|bonus|
+---------+------+-----+
|    James|  3000|  0.3|
|     Anna|  4100|  0.3|
|   Robert|  6200|  0.3|
+---------+------+-----+

+---------+------+------------+
|firstname|salary|bonus_amount|
+---------+------+------------+
|    James|  3000|       900.0|
|     Anna|  4100|      1230.0|
|   Robert|  6200|      1860.0|
+---------+------+------------+

+---------+------+----------+
|firstname|salary|today_date|
+---------+------+----------+
|    James|  3000|2023-06-16|
|     Anna|  4100|2023-06-16|
|   Robert|  6200|2023-06-16|
+---------+------+----------+

+---------+------+-----+
|firstname|salary|grade|
+---------+------+-----+
|    James|  3000|    B|
|     Anna|  4100|    B|
|   Robert|  6200|    B|
+---------+------+-----+

"""


from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

data = [('James','Smith','M',3000),
  ('Anna','Rose','F',4100),
  ('Robert','Williams','M',6200), 
]

columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()


if 'salary1' not in df.columns:
    print("aa")
    
# Add new constanct column
from pyspark.sql.functions import lit
df.withColumn("bonus_percent", lit(0.3)) \
  .show()
  
#Add column from existing column
df.withColumn("bonus_amount", df.salary*0.3) \
  .show()

#Add column by concatinating existing columns
from pyspark.sql.functions import concat_ws
df.withColumn("name", concat_ws(",","firstname",'lastname')) \
  .show()

#Add current date
from pyspark.sql.functions import current_date
df.withColumn("current_date", current_date()) \
  .show()


from pyspark.sql.functions import when
df.withColumn("grade", \
   when((df.salary < 4000), lit("A")) \
     .when((df.salary >= 4000) & (df.salary <= 5000), lit("B")) \
     .otherwise(lit("C")) \
  ).show()
    
# Add column using select
df.select("firstname","salary", lit(0.3).alias("bonus")).show()
df.select("firstname","salary", lit(df.salary * 0.3).alias("bonus_amount")).show()
df.select("firstname","salary", current_date().alias("today_date")).show()

#Add columns using SQL
df.createOrReplaceTempView("PER")
spark.sql("select firstname,salary, '0.3' as bonus from PER").show()
spark.sql("select firstname,salary, salary * 0.3 as bonus_amount from PER").show()
spark.sql("select firstname,salary, current_date() as today_date from PER").show()
spark.sql("select firstname,salary, " +
          "case salary when salary < 4000 then 'A' "+
          "else 'B' END as grade from PER").show()


