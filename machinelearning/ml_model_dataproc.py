from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.getOrCreate()


data= spark.read.format("bigquery").option("table", "germany_regression.germany").load()





# create features vector
feature_columns =['Value'] # here we omit the final column


data2 = clean_data.rdd.map(feature_colums).toDF(["label","features"])

data2.cache()

algo = RandomForestClassifier(featuresCol='features', labelCol='Crisis')
model = algo.fit(data_2) 
