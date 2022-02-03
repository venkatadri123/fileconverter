# Constant variables
CFG_FILE_PATH = "tests/fixtures/test.cfg"

YML_FILE_PATH = "tests/fixtures/test.yml"

NE_FILE_PATH = "tests/fixtures/test.txt"

DATA_FOR_CFG = {'ABC': {'ch0': '"C:/Users/utility/ABC-ch0.txt"', 'ch1': '"C:/Users/utility/ABC-ch1.txt"'},
                'settings': {'script': '"C:/Users/OneDrive/utility/xxxx.exe"',
                             'settings': '"C:/Users/OneDrive/xxxxxxConfig.xml"'}}

DATA_FOR_YML = {'name': 'SkySlopeV2', 'description': 'SkySlope V2 Ingestion Source', 'fields': [
    {'slug': 'TypeOfSale', 'name': 'objectType', 'type': 'list', 'allowed': ['Sale', 'Listing'], 'trigger_field': True,
     'dynamic_field': True}]}

new_name = "new_file.json"

new_name_env = "new_file.env"

err = "Please give valid file_path with extention ex: .yml,.cfg or .conf"

error1 = "Please give valid file_path with extention ex: .env,.json"

neg_new_name_env = "new_file.txt"
