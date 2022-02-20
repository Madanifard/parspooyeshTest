import pymongo
import pandas as pd

def fined_register_user(start_date, end_date):
    '''
    connected to mongo 
    set filter 
    search in people collection
    '''
    try:
        database_name = 'parspooyeshDB'
        collection_name = 'peoples'
        my_client = pymongo.MongoClient("mongodb://localhost:27017")
        my_db = my_client[database_name]
        my_collections = my_db[collection_name]

        conditions = {
            "signup": {
                "$gt": start_date,
                "$lt": end_date,
            }
        }
        output = {
            'error': False,
            'message': 'search OK',
            'data': my_collections.find(conditions)
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
