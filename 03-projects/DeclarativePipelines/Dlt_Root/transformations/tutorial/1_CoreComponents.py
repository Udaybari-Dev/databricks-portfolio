# #creating streaming table 
# # streeaming view 
# import dlt 

# @dlt.table(
#     name = "first_stream_table"
# )
# def first_stream_table():
#     df = spark.readStream.table("ud_cata.ud_schema.orders")
#     return df


# ## meterlized view ( batch processing )

# @dlt.table(
#     name = "first_mat_view"
# )

# def first_mat_view():
#     df = spark.read.table("ud_cata.ud_schema.orders")
#     return df




# # create view , only for view , which hold the query  only not stored  any where 
# # 2 type Btach view and stream view ok 

# # Btach view  ( dlt.view is used not table )
# @dlt.view(
#     name = "first_batch_view"
# )
# def first_batch_view():
#     df = spark.read.table("ud_cata.ud_schema.orders")
#     return df

# # Cretating straming view 
# @dlt.view(
#     name = "first_stream_view"
# )

# def first_stream_view():
#     df = spark.readStream.table("ud_cata.ud_schema.orders")
#     return df 


