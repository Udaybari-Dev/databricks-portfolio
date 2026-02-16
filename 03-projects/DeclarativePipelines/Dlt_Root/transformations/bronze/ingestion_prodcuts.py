import dlt 

#Product rules 
product_rules = {
    "rule_1" : "product_id IS NOT NULL",
    "rule_2" : "price >= 0"

 }

# Ingesting Produts 
@dlt.table(
    name = "products_stg"
)
@dlt.expect_all_or_drop(product_rules)

def products_stg():
    df = spark.readStream.table("ud_cata.dlt_schema.products")
    return df