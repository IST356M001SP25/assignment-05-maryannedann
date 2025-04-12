from datetime import datetime

def clean_currency(item: str) -> float:
    """
    Cleans a currency string like "$120,000.00" or "USD 45,500" into a float 120000.0 or 45500.0.
    """
    if not item:
        return None

    allowed_chars = "0123456789."
    result = ""

    for char in item:
        if char in allowed_chars:
            result += char

    try:
        return float(result)
    except:
        return None

def extract_year_mdy(timestamp):
    """
    Extracts the year from a timestamp in MM/DD/YYYY format.
    Returns the year as an integer, or None if the format is invalid.
    """
    try:
        dt = datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S')
        return dt.year
    except ValueError:
        return None

def clean_country_usa(item: str) -> str:
    if not isinstance(item, str):
        return item  # Return as-is if not a string

    country = item.strip().lower()
    if country in ['usa', 'us', 'u.s.', 'united states of america']:
        return 'United States'
    if country == 'united states':
        return 'United States'
    return item.title()              
