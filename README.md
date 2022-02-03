# Converter-python-client
it is used to convert .cfg, .config, .yml and .yaml files to dictionary then we can generate new json, .env files from this library

## Versions
''python 3.5'' and above

## Building
''python setup.py bdist_wheel''

## Installing
''pip install dist/file_converter-0.6.0-py3-none-any.whl''

# Usage
To call an library you must create a object.

''conver_object = FileConverter(file_path)''

# Example
if you want to convert a yml file to json you need to import the library and create an object 

from file_converter.converter import FileConverter

<!-- Invoking the FileConverter class by passing file_path -->
''conver_object = FileConverter("file_name.yml")''

<!--  this will convert given file to dict and stored into self.data -->
''conver_object.convert()''

<!--  printing the converted value -->
''print(conver_object.data)''

<!--  generating new file from converted dictionary it will be stored into given path -->
''conver_object.get_configuration("new_file.json")''

<!--  exporting env variables to current system from generated dictionary -->
''conver_object.set_configuration()''
