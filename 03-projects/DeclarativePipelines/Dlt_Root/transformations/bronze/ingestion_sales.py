import dlt

#Sales Expectations 
sales_rules = {
    "rule_1" : "sales_id IS NOT NULL"
}

# Empty Streaming Table 
dlt.create_streaming_table(
    name = "sales_stg", 
    expect_all_or_drop= sales_rules
    ) 


# Creating East sales flow 
@dlt.append_flow(target="sales_stg")
def east_sales():

    df = spark.readStream.table("ud_cata.dlt_schema.sales_east")
    return df


#Creating west sales flow 
@dlt.append_flow(target="sales_stg")
def west_sales():

    df = spark.readStream.table("ud_cata.dlt_schema.sales_west")
    return df


 



