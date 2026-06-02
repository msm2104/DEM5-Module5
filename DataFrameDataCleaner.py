class DataFrameDataCleaner:
    def __init__(self, df):
        self.DataFrame = df
        

    def DropNullRows(self,subset=None):
        return self.DataFrame.dropna(subset=subset)
    
    def DropDuplicates(self,subset=None):
        return self.DataFrame.drop_duplicates(subset=subset)