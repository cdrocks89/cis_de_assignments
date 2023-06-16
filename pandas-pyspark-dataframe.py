"""
     Name  Age
0   Scott   50
1    Jeff   45
2  Thomas   54
3     Ann   34
root
 |-- Name: string (nullable = true)
 |-- Age: long (nullable = true)

+------+---+
|  Name|Age|
+------+---+
| Scott| 50|
|  Jeff| 45|
|Thomas| 54|
|   Ann| 34|
+------+---+

root
 |-- First Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 
 """

# -*- coding: utf-8 -*-
"""
author SparkByExamples.com
"""

import pandas as pd    
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
  
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()

#sparkDF=spark.createDataFrame(pandasDF.astype(str)) 
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
mySchema = StructType([ StructField("First Name", StringType(), True)\
                       ,StructField("Age", IntegerType(), True)])

sparkDF2 = spark.createDataFrame(pandasDF,schema=mySchema)
sparkDF2.printSchema()
sparkDF2.show()


spark.conf.set("spark.sql.execution.arrow.enabled","true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled","true")

pandasDF2=sparkDF2.select("*").toPandas
print(pandasDF2)


test=spark.conf.get("spark.sql.execution.arrow.enabled")
print(test)

test123=spark.conf.get("spark.sql.execution.arrow.pyspark.fallback.enabled")
print(test123)
