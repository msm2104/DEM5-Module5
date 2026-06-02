import re 
from datetime import datetime

def parse_date(date_str): 
    # 1. remove string quotation of exists 
    # 2. check if you can parse date
    # 3. format date in standard mm/dd/yyyy format 
    date_str = date_str.replace("\"","")
    formats = [
        "%d/%m/%Y",  # 01/06/2026 or 1/6/2026
        "%d/%m/%y",  # 01/06/26 or 1/6/26
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass

    raise ValueError(f"Invalid date format: {date_str}")   
     

def extract_no_of_weeks(val):
    no_of_weeks_str = re.sub("week", "", val, flags=re.IGNORECASE)
    no_of_weeks_str = re.sub("weeks", "", no_of_weeks_str, flags=re.IGNORECASE)
    if is_int(no_of_weeks_str):
        return float(no_of_weeks_str)
    return None

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def calculate_book_hold_days(checkout_date,return_date):
    days = (return_date - checkout_date).days
    return days

    