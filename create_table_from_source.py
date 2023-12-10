import docx
import pandas as pd

def create_table_from_source(source_path: str, 
                             worksheet=None,
                             sep=',',
                             header=True) -> docx.Document:
    
    # check for file type
        
    if source_path.endswith(".xlsx"):
        df = pd.read_excel(source_path, worksheet=worksheet)
    elif source_path.endswith(".csv"):
        df = pd.read_csv(source_path, sep=sep, header=0)
    elif source_path.endswith(".parquet"):
        df = pd.read_parquet()
    elif source_path.endswith(".json"):
        df = pd.read_json()
    else:
        print("Invalid file type.")
        return None
    
    
    
    
        
    
    
    
        
        
    
    
