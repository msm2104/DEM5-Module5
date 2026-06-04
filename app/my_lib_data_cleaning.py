import pandas as pd
from helper_fun import *
from DataFrameDataCleaner import DataFrameDataCleaner
from DataFrameEnrich import DataFrameEnrich

LIBARTY_BORROW_RECORD = f"data/03_Library Systembook.csv"        # Customer ID, Customer Name
CUSTOMER_FILENAME = f"data/03_Library SystemCustomers.csv"        # Id, Books, Book checkout, Book Returned, Days allowed to borrow, Customer ID
    
CLEAN_CUSTOMER_LIST_OUT = f"../clean/Customers_Cleaned.csv"
DIRTY_CUSTOMER_LIST_OUT = f"../clean/Customer_Dirty.csv"
CUSTOMER_CLEANING_STATS_OUT = f"../clean/Customer_Pipeline_Stats.csv"

CLEAN_BORROW_RECORD_OUT = f"../clean/Systembook_Clean.csv"
DIRTY_BORROW_RECORD_OUT = f"../clean/Systembook_Dirty.csv" 
BORROW_RECORD_CLEANING_STATS_OUT = f"../clean/Systembook_Pipeline_Stats.csv"



def clean_customer_library_files():
    
    cus_data = pd.read_csv(CUSTOMER_FILENAME)
    cus_data_clean = DataFrameDataCleaner(cus_data.copy())

    cus_data_clean.clean_empty_rows(null_subset=["Customer ID", "Customer Name"])
    cus_data_clean.clean_duplicate_rows()
    cus_data_clean.stats["clean_rows"] = len(cus_data_clean.df)
    
    # output into clean csv file.
    cus_data_clean.df.to_csv(CLEAN_CUSTOMER_LIST_OUT, index=False)

    # output into dirty csv file.
    cus_data_clean.removed_rows_df.to_csv(DIRTY_CUSTOMER_LIST_OUT, index=False)

    # output summary file.
    pd.DataFrame([cus_data_clean.stats]).to_csv(CUSTOMER_CLEANING_STATS_OUT, index=False)
    



def clean_library_record_files():
    
    lib_rec_data = pd.read_csv(LIBARTY_BORROW_RECORD)
    lib_rec_data_clean = DataFrameDataCleaner(lib_rec_data.copy())

    lib_rec_data_clean.clean_empty_rows(null_subset=["Id", "Books"])
    lib_rec_data_clean.clean_duplicate_rows()
    lib_rec_data_clean.clean_invalid_dates('Book checkout')
    lib_rec_data_clean.clean_invalid_dates('Book Returned')
    lib_rec_data_clean.stats["clean_rows"] = len(lib_rec_data_clean.df)

    lib_rec_data_enrich = DataFrameEnrich(lib_rec_data_clean.df.copy())
    lib_rec_data_enrich.add_duration('Book checkout','Book Returned','actual hold days')
    lib_rec_data_enrich.calculate_date('Book checkout','Days allowed to borrow','expected_return_date')

    
    # output into clean csv file.
    lib_rec_data_enrich.df.to_csv(CLEAN_BORROW_RECORD_OUT, index=False)

    # output into dirty csv file.
    lib_rec_data_clean.removed_rows_df.to_csv(DIRTY_BORROW_RECORD_OUT, index=False)

    # output summary file.
    pd.DataFrame([lib_rec_data_clean.stats]).to_csv(BORROW_RECORD_CLEANING_STATS_OUT, index=False)
    



if __name__ == "__main__":
    clean_customer_library_files()
    clean_library_record_files()
    