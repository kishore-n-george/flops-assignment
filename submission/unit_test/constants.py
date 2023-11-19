# You can create more variables according to your project. The following are the basic variables that have been provided to you
#UNIT_TEST_DB_PATH = '/Users/kishoregeorge/Development/MLDS/repos/mlops-assignment/Assignment/01_data_pipeline/unit_test/' 
DB_PATH = '/Users/kishoregeorge/Development/MLDS/repos/mlops-assignment/Assignment/01_data_pipeline/unit_test/' 
DB_FILE_NAME = 'utils_output.db'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = DB_PATH
INTERACTION_MAPPING = DB_PATH+'interaction_mapping.csv'
INDEX_COLUMNS_TRAINING = ['created_date', 'first_platform_c',
       'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier',
       'referred_lead', 'app_complete_flag']
INDEX_COLUMNS_INFERENCE = ['created_date', 'first_platform_c',
       'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier',
       'referred_lead']
NOT_FEATURES = ['created_date', 'assistance_interaction', 'career_interaction',
                'payment_interaction', 'social_interaction', 'syllabus_interaction']




