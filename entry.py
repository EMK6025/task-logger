from datetime import date, time, timedelta
from sqlalchemy import Interval, MetaData, Table, text, insert
from engine import create_engine

# sql shortcut to log new entry
def log(name:str, date:date, 
        start_time: time, duration:timedelta, 
        description:str = '', sub_tasks:int = 1):
    
    engine = create_engine()
    metadata = MetaData()

    table = Table("logs", metadata, autoload_with=engine)
    
    stmt = insert(table).values(name=name, date=date,
                                start_time=start_time, duration=duration,
                                description=description, sub_tasks=sub_tasks)
    
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
    return

# function for grabbing a single field
def grab_input(field_name):
    while True:
        val = input("\nEnter the activity's {field_name}: ")
        while True:
            check = input(f'Is "{val}" correct? y/n: ').lower()
            if check in ("y", "n"):
                break
            print("Invalid input. Try again.")
        
        if check == "y":
            break
    return val

if __name__ == '__main__':
    # entry()
    # log("Scrolling", date(2025, 7, 30), time(hour=7, minute=0), duration=timedelta(hours=2))
    engine = create_engine()
    from engine import connect
    df = connect(engine)
    print(df.head())
    
'''
CREATE TABLE logs (
    id                  SERIAL PRIMARY KEY,
    name                TEXT NOT NULL,
    date                DATE NOT NULL,
    start_time          TIME NOT NULL,
    duration            INTERVAL NOT NULL,
    description         TEXT,
    sub_tasks           INTEGER DEFAULT 1 CHECK (sub_tasks >= 1)
);
'''