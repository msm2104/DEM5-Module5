import pandas as pd
from helper_fun import *
import DataFrameDataCleaner as dc


LIBARTY_BORROW_RECORD = "data/03_Library Systembook.csv"        # Customer ID, Customer Name
CUSTOMER_FILENAME = "data/03_Library SystemCustomers.csv"        # Id, Books, Book checkout, Book Returned, Days allowed to borrow, Customer ID
    
CLEAN_CUSTOMER_LIST = "Library Systembook_SystemCustomers.csv"
CLEAN_BORROW_RECORD = "Library_Systembook_Clean.csv"
DIRTY_BORROW_RECORD = "Library_Systembook_Dirty.csv"


def clean_library_record_files():
    Record_Cleaning_Summary = {
        "Original_Rows" : 0,
        "Duplicates" : 0,
        "Empty Rows" : 0,
        "Dirty Rows" : 0,
        "Clean Rows" : 0  
    }
    lib_rec_data = pd.read_csv(LIBARTY_BORROW_RECORD)
    lib_rec_data_clean =  lib_rec_data.copy();

    

    Record_Cleaning_Summary["Original_Rows"] = len(lib_rec_data)
    
    # remove duplicates 
    old_len = len(lib_rec_data)
    lib_rec_data_clean =   lib_rec_data_clean.drop_duplicates()
    Record_Cleaning_Summary["Duplicates"] = old_len - len(lib_rec_data)
    
    
    # remove null values 
    old_len = len(lib_rec_data_clean)
    lib_rec_data_clean = lib_rec_data_clean.dropna(subset=["Id"])
    Record_Cleaning_Summary["Empty Rows"] =  old_len -  len(cus_data_clean)

    # output into clean csv file.
    lib_rec_data_clean.to_csv(CLEAN_CUSTOMER_LIST, index=False)


def clean_customer_library_files():
    Customer_File_Cleaning_Summary = {
        "Original_Rows" : 0,
        "Duplicates" : 0,
        "Empty Rows" : 0,
        "Clean Rows" : 0  
    }
    cus_data = pd.read_csv(CUSTOMER_FILENAME)
    cus_data_clean = cus_data.copy();

    Customer_File_Cleaning_Summary["Original_Rows"] = len(cus_data)
    
    # remove duplicates 
    old_len = len(cus_data)
    cus_data_clean = cus_data_clean.drop_duplicates()
    Customer_File_Cleaning_Summary["Duplicates"] = old_len - len(cus_data_clean)
    
    
    # remove null values 
    old_len = len(cus_data_clean)
    cus_data_clean = cus_data_clean.dropna(subset=["Customer ID", "Customer Name"])
    Customer_File_Cleaning_Summary["Empty Rows"] =  old_len -  len(cus_data_clean)

    # output into clean csv file.
    cus_data_clean.to_csv(CLEAN_CUSTOMER_LIST, index=False)

if __name__ == "__main__":
    clean_customer_library_files()