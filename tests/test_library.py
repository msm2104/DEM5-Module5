import pandas as pd 
import unittest
from app.DataFrameDataCleaner import DataFrameDataCleaner
from pandas.testing import assert_frame_equal


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Customer ID": [1, 2, 2, 3, 4, 5, 5, 6],
            "Customer Name": ["Alice", "Bob", "Bob", None, "David", "Eve", "Eve", "Frank"],
            "Email": ["alice@test.com", "bob@test.com", "bob@test.com", "charlie@test.com", None, "eve@test.com", "eve@test.com", "frank@test.com"],
            "Age": [25, 30, 30, 22, 40, None, None, 28],
            "City": ["London", "Paris", "Paris", "Berlin", "Madrid", "Rome", "Rome", None]
            })
        self.df_cleaner = DataFrameDataCleaner(self.df)


    def test_dataframe_cleaner(self) :
        original_rows = len(self.df)

        self.df = self.df.drop_duplicates()
        duplicate_rows_removed = original_rows - len(self.df)    
            
        self.df = self.df.dropna(subset=["Customer Name","Email"])
        null_rows_removed = duplicate_rows_removed - len(self.df)
        
        self.df_cleaner.clean_empty_rows()
        self.df_cleaner.find_duplicates()
        
        
        self.assertEqual(original_rows,self.df_cleaner.stats["original_rows"], "no of original rows in data cleaning doesn't match")
        self.assertEqual(duplicate_rows_removed,self.df_cleaner.stats["duplicate_rows_removed"], "no of duplicate rows removed in data cleaning doesn't match")
        self.assertEqual(null_rows_removed,self.df_cleaner.stats["null_rows_removed"], "no of null rows removed in data cleaning doesn't match")
        assert_frame_equal(self.df,self.df_cleaner.df,"Clean DataFrame does not match")


if __name__ == "__main__":
    unittest.main()