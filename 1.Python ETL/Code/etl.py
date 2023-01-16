from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import pymysql

# Create a SparkSession
spark = SparkSession.builder.appName("MySQL_ETL").config("spark.logConf", "true").config("spark.logLevel", "ERROR").getOrCreate()

# Read the CSV file into a Spark DataFrame
df = spark.read.csv("DEM_Challenge_Section1_DATASET.csv", header=True, inferSchema=True)

# Perform some transformations on the DataFrame
df = df.withColumnRenamed("id", "ID")
df = df.withColumn("Full_Name", F.concat(F.col("first_name"), F.lit(" "), F.col("last_name")))

#df.show()

# do some transformations using Spark DataFrames
df = df.withColumnRenamed("first_name", "FirstName").withColumnRenamed("last_name", "LastName")
df = df.withColumn("gender", F.when(df["gender"] == "Genderfluid", "Other").otherwise(df["gender"]))

df = df.withColumnRenamed("gender", "Gender")

df.show()

# Write the DataFrame to a MySQL table
df.write.format("jdbc").options(
    url="jdbc:mysql://pythonetldbinstance-us-west-1.c42itdm7bfae.us-west-1.rds.amazonaws.com:3306/mydb",
    driver="com.mysql.jdbc.Driver",
    dbtable="transformed_table",
    user="myuser",
    password="mypassword"
).mode("append").save()

# Close the SparkSession
spark.stop()

