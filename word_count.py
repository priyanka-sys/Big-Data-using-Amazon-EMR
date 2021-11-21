from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('WordCountApp').getOrCreate()


df = spark.read.text('s3://kpl3-s3/shakespeare_data.txt').co


#df = spark.read.text('shakespeare_data.txt')

#df.show()

df.withColumnRenamed('value', 'word').createTempView("data")

# Count the number of words
df.count()

# First three values in text file
df.show(3, True)

# 10 longest words and their length
spark.sql('SELECT DISTINCT(word), length(word) AS len FROM data ORDER BY len DESC').show(10)


# 10 highest occurred words and count of occurrence
spark.sql(
    "SELECT word, count(word) AS word_count FROM data GROUP BY word ORDER BY word_count DESC").show(10)

© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
