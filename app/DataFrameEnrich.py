import pandas as pd
import helper_fun as h
from dataclasses import dataclass

@dataclass
class DataFrameEnrich:
    df : pd.DataFrame
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        
    def add_duration(self,datetimeFrom_col,datetimeTo_col,newcolumn_name):

        self.df[datetimeFrom_col] = pd.to_datetime(
            self.df[datetimeFrom_col],
            dayfirst=True,
            errors="coerce"
        )

        self.df[datetimeTo_col] = pd.to_datetime(
            self.df[datetimeTo_col],
            dayfirst=True,
            errors="coerce"
        )
        
        
        self.df[newcolumn_name] = (
            self.df[datetimeTo_col] - self.df[datetimeFrom_col]
        ).dt.days
        return self.df

    def calculate_date(self,datetime_from,duration_col,newcolumn_name):

        self.df[datetime_from] = pd.to_datetime(
            self.df[datetime_from],
            dayfirst=True,
            errors="coerce"
        )
        
        weeks = self.extract_no_of_weeks(self.df[duration_col])

        self.df[newcolumn_name] = (
            self.df[datetime_from]
            + pd.to_timedelta(weeks, unit="W")
        )
        
        return self.df
    
    def extract_no_of_weeks(self,series: pd.Series) -> pd.Series:
        return (
            series.astype(str)
            .str.lower()
            .str.extract(r"(\d+)", expand=False)
            .astype(float)
            .fillna(0)
        )

    
    