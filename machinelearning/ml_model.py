from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.getOrCreate()

data = spark.read.csv('./indicators3.csv', header=True, inferSchema=True)



# create features vector
feature_columns =['Value'] # here we omit the final column


assembler = VectorAssembler(inputCols=feature_columns,outputCol="features")

data_2 = assembler.transform(data)




algo = RandomForestClassifier(featuresCol='features', labelCol='Crisis')
model = algo.fit(data_2) 
