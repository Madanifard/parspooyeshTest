import pandas as pd
from .connection import MongoConnection

def fined_register_user(start_date, end_date):
    '''
    connected to mongo 
    set filter 
    search in people collection
    '''
    try:
        connection = MongoConnection()
        conditions = {
            "signup": {
                "$gt": start_date,
                "$lt": end_date,
            }
        }
        
        output = {
            'error': False,
            'message': 'search OK',
            'data': connection.find('peoples', conditions)
        }
    except Exception as ex:
        output = {
            'error': True,
            'message': ex,
        }
    finally:
        return output 



def report_register_people_pandas(items):
    '''
    get data that find 
    then convert to DataFrame Pandas
    and export to CSV file in reports directory
    '''
    try:
        df =  pd.DataFrame(items)
        df.to_csv('reports/output_report.csv')
        output = {
            'error': False,
            'message': 'Ready csv file'
        }
    except Exception as ex:
        output = {
            'error': True,
            'message': ex
        }
    finally:
        return output
