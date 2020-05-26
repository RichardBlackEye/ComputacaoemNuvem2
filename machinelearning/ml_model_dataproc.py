from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.getOrCreate()


data= spark.read.format("bigquery").option("table", "germany_regression.germany").load()





# create features vector
feature_columns =['NY_ADJ_NNTY_KD_ZG','NY_ADJ_NNTY_KD','NY_ADJ_NNTY_CD','NY_ADJ_NNTY_PC_KD_ZG','NY_ADJ_NNTY_PC_KD','NY_ADJ_NNTY_PC_CD','NY_ADJ_SVNX_GN_ZS','NY_ADJ_SVNX_CD','NY_ADJ_SVNG_GN_ZS'] # here we omit the final column


data2 = clean_data.rdd.map(feature_colums).toDF(["label","features"])

data2.cache()

algo = RandomForestClassifier(featuresCol='features', labelCol='Crise')
model = algo.fit(data_2) 
predictions = model.transform(data_2) 

predictions.select(['Crise','prediction', 'probability']).show() 