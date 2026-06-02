import pandas as pd
from dataclasses import dataclass

@dataclass
class DataFrameDataCleaner:
    df : pd.DataFrame

    def clean_null_and_duplicates(self,nullSubset = None,duplicateSubSet = None) :
            original_rows = len(self.df)
            
            self.df = self.df.drop_duplicates(subset=duplicateSubSet)
            duplicate_rows_removed = original_rows - len(self.df)
            
            
            self.df = self.df.dropna(subset=nullSubset)
            null_rows_removed = duplicate_rows_removed - len(self.df)
        

            return self.df, original_rows, null_rows_removed, duplicate_rows_removed


if __name__ == "__main__":
    unittest.main()