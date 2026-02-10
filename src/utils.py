from datetime import datetime

def is_iso_date(datevalue: str) -> bool:
    try:
        if datevalue.endswith("Z"):
            datevalue = datevalue[:-1]
        datetime.fromisoformat(datevalue)
        return True
    except ValueError:
        return False
