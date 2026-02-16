# import dlt
# from pyspark.sql.functions import *

# # Creating End-To-End Basic Pipeline

# # ---------------- STAGING ----------------
# @dlt.table(name='staging_orders')
# def staging_orders():
#     df = spark.readStream.table("ud_cata.ud_schema.orders")
#     return df


# # ---------------- TRANSFORMED ----------------
# @dlt.view(name="transformed_orders")
# def transformed_orders():
#     df = dlt.read_stream("staging_orders")
#     df = df.withColumn("order_status", lower(col("order_status")))
#     return df

# #Creating Aggregated orders 

# @dlt.table( name= 'aggregated_orders')

# def aggregated_orders():
#     df = dlt.read_stream("transformed_orders")
#     df = df.groupBy("order_status").count() 

#     return df





