import pandas as pd
from helper_fun import *
from DataFrameDataCleaner import DataFrameDataCleaner

LIBARTY_BORROW_RECORD = "data/03_Library Systembook.csv"        # Customer ID, Customer Name
CUSTOMER_FILENAME = "data/03_Library SystemCustomers.csv"        # Id, Books, Book checkout, Book Returned, Days allowed to borrow, Customer ID
    
CLEAN_CUSTOMER_LIST_OUT = f"/data/Library_SystemCustomers_Clean.csv"
CLEAN_BORROW_RECORD_OUT = f"/data/Library_Systembook_Clean.csv"
DIRTY_BORROW_RECORD_OUT = f"/data/Library_Systembook_Dirty.csv" 


def clean_library_record_files():
    record_cleaning_summary = {
        "Original_Rows" : 0,
        "Duplicates" : 0,
        "Empty_Rows" : 0,
        "Dirty_Rows" : 0,
        "Clean_Rows" : 0  
    }
    lib_rec_data = pd.read_csv(LIBARTY_BORROW_RECORD)
    lib_rec_data_clean = DataFrameDataCleaner(lib_rec_data.copy())

    lib_rec_data_clean.df, 
    record_cleaning_summary["Original_Rows"], 
    record_cleaning_summary["Duplicates"], 
    record_cleaning_summary["Empty_Rows"] = lib_rec_data_clean.clean_null_and_duplicates(nullSubset=["Id"],duplicateSubSet=None)

    
    # output into clean csv file.
    lib_rec_data_clean.df.to_csv(CLEAN_BORROW_RECORD_OUT, index=False)


def clean_customer_library_files():
    customer_file_cleaning_summary = {
        "Original_Rows" : 0,
        "Duplicates" : 0,
        "Empty_Rows" : 0,
        "Clean_Rows" : 0  
    }
    cus_data = pd.read_csv(CUSTOMER_FILENAME)
    cus_data_clean = DataFrameDataCleaner(cus_data.copy())

    cus_data_clean.df, 
    customer_file_cleaning_summary["Original_Rows"], 
    customer_file_cleaning_summary["Duplicates"], 
    customer_file_cleaning_summary["Empty_Rows"] = cus_data_clean.clean_null_and_duplicates(nullSubset=["Customer ID", "Customer Name"],duplicateSubSet=None)
    
    customer_file_cleaning_summary["Clean_Rows"] = len(cus_data_clean.df)
    # output into clean csv file.
    cus_data_clean.df.to_csv(CLEAN_CUSTOMER_LIST_OUT, index=False)

if __name__ == "__main__":
    clean_customer_library_files()