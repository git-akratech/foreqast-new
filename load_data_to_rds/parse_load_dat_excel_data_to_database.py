# pandas for read excel
import pandas as pd
# import ORM / DB related packages
from sqlalchemy import create_engine, Table, MetaData, select, insert, update, delete, and_, or_, func

# database configuration
# ENV variables here
DATABASE_USERNAME = "admin"
DATABASE_PASSWORD = "%Monday123%"
DATABASE_HOSTNAME = "database-1.c8uq1bsrptts.ap-south-1.rds.amazonaws.com"
DATABASE_NAME = "akra_scraper"

# Database conection
db_engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME, echo = False, pool_size = 50, max_overflow = 16, pool_recycle = 300)

# data verification and insert script generation
def convert_excel_into_insert_script():
    # read the excel
    excel_file_name = "scraping_data/load/ERCO.xlsx"
    df = pd.read_excel(str(excel_file_name), sheet_name="Sheet1", engine='openpyxl')
    
    # remove the duplicate records
    duplicate = df[df.duplicated(subset=['timestamp'])]
    
    # remove not required columns
    df = df.drop(columns = ['Unnamed: 0'])

    # insert into the database
    df.to_sql('foreqast_load_data', db_engine, if_exists='append', index=False)

# invoke system execution
if __name__ == "__main__":
    convert_excel_into_insert_script()
