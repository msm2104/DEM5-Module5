import pandas as pd
from dataclasses import dataclass

@dataclass
class DataFrameDataCleaner:
    df : pd.DataFrame
    removed_rows_df : pd.DataFrame
    stats : {}

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.removed_rows_df = pd.DataFrame()
        self.stats = {
            "original_rows": len(df),
            "duplicate_rows_removed": 0,
            "null_rows_removed": 0,
            "invalid_date_rows_removed": 0,
            "clean_rows" : 0
        }
        

    def find_duplicates(self, subset=None):
        return self.df[self.df.duplicated(subset=subset, keep="first")].copy()

    def find_null_rows(self, subset=None):
        if subset is None:
            mask = self.df.isna().any(axis=1)
        else:
            mask = self.df[subset].isna().any(axis=1)

        return self.df[mask].copy()
    
    def find_invalid_date(self, date_column):
        temp_dates = pd.to_datetime(
            self.df[date_column],
            dayfirst=True,
            errors="coerce"
        )

        invalid_mask = temp_dates.isna()

        return self.df[invalid_mask].copy(), invalid_mask

    
    def append_removed_rows(self, rows, reason):
        if rows.empty:
            return

        rows = rows.copy()
        rows["removal_reason"] = reason

        self.removed_rows_df = pd.concat(
            [self.removed_rows_df, rows],
            ignore_index=True
        )

    def clean_invalid_dates(
        self,
        date_column
    ):
        
        self.df[date_column] = self.df[date_column].str.replace('"', "", regex=True)

        invalid_date_rows , invalid_mask = self.find_invalid_date(date_column)

        self.stats["invalid_date_rows_removed"] += len(invalid_date_rows)
        self.append_removed_rows(
            invalid_date_rows,
            f"invalid_date :{date_column}"
        )

        self.df = self.df[~invalid_mask].copy()

        return self.df
    
    def clean_empty_rows(
        self,
        null_subset=None,
    ):
        
        # Track duplicates
        null_rows = self.find_null_rows(null_subset)
        
        self.stats["null_rows_removed"] = len(null_rows)

        # Final cleaned dataframe
        self.df = self.df.dropna(
            subset=null_subset
        )

        self.append_removed_rows(
            null_rows,
            "Empty rows"
        )
        
        return self.df
    
    def clean_duplicate_rows(
        self,
        duplicate_subset=None,
    ):
        
        # Track duplicates
        duplicate_rows = self.find_duplicates(duplicate_subset)
        self.stats["duplicate_rows_removed"] = len(duplicate_rows)
        
        self.df = self.df.drop_duplicates(
            subset=duplicate_subset
        )

        self.append_removed_rows(
            duplicate_rows,
            "duplicates"
        )
        
        return self.df 

    