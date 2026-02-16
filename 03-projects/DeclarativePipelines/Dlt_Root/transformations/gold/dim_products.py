import dlt 


# We need to creat AUTO CDC dflow 
# Create empty Streaming table 

dlt.create_streaming_table(
    name = "dim_products"
)



# Auto CDC flow 

dlt.create_auto_cdc_flow(
        target = "dim_products",
        source = "products_enr_view",
        keys = ["product_id"],
        sequence_by = "last_updated",
        column_list= None,
        ignore_null_updates= False,
        apply_as_deletes = None,
        apply_as_truncates = None,
        except_column_list = None,
        stored_as_scd_type = 1,
        # Important to set this to true 
        track_history_column_list = None,
        track_history_except_column_list = None

)


