import json
import os

import yaml
from configparser import ConfigParser


# class defined as FileConverter
class FileConverter:
    # defined constructor method with file_name as argument
    # it takes file name and stores into self.file_name so it can be accessible in any method
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None
        self.error = None

    # this method checks the file format, based on that appropriate method will be called
    # to convert file data into flat dictionary
    def convert(self):
        # checking file formate is .yml or .yaml then calling yml_to_dict method and
        # assigning that result in self.data
        if ".yml" in self.file_name.lower() or "yaml" in self.file_name.lower():
            self.data = self.__yml_to_dict()
        # checking file formate is .yfg or .config then calling config_to_dict method and
        # assigning that result in self.data
        elif ".cfg" in self.file_name.lower() or ".config" in self.file_name.lower() or ".conf" in self.file_name.lower():
            self.data = self.__config_to_dict()
        else:
            self.error = "Please give valid file_path with extention ex: .yml,.cfg or .conf"
            print(self.error)

    # This is private method it can't able to access out side of the class
    # reads the YML file and return dict as a result
    def __yml_to_dict(self):
        # using file handling to open a file and using yaml package to
        # read and convert data into dictionary
        with open(self.file_name) as f:
            data = yaml.safe_load(f)
            # returning final output dict
            return data

    # This is private method it can't able to access out side of the class
    # This method uses the configparser package then reads the input file then creates dictionary
    def __config_to_dict(self):
        # object creation
        config = ConfigParser()
        # reading input file
        config.read(self.file_name)
        dictionary = {}
        # looping config and creating a dictionary with config data
        for section in config.sections():
            # value assignment to existing dict with empty dict
            dictionary[section] = {}
            for option in config.options(section):
                # value assignment to existing dict with some data
                dictionary[section][option] = config.get(section, option)
        # returning final output dict
        return dictionary

    # This method takes 1 argument file_path (it contains the output file formate like .env or .json
    # based on file extension data will be written to given file and stored into same file path
    def get_configuration(self, file_path):
        # Checking file path is valid or not if its not valid printing error message
        # and returning value as None
        if ".env" not in file_path and ".json" not in file_path:
            self.error = "Please give valid file_path with extension ex: .env,.json"
            print(self.error)
            return None
        # Checking file extension is .env then using filehandling to create file 
        # and writing data to that file
        if ".env" in file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                for val in self.data:
                    file.write(f"{val}={self.data.get(val)}\n")
                print(f"file generated: {file_path}")
        # else considering the file extension as json and creating file and dumping data
        else:
            with open(file_path, "w") as file:
                json.dump(self.data, file)
                print(f"file generated: {file_path}")

    # This method gets the self.data as value then iterate each element then it will add environment variables
    def set_configuration(self):
        # doing iteration using for loop
        for value in self.data:
            # using exception handling to avoid the exceptions (iteration will not break until it's done
            try:
                os.environ[value] = str(self.data.get(value))
                print(f"environment variable name: {value} is exported")
            except Exception as e:
                print(f"ERROR: while exporting env {value}: {self.data.get(value)} to the system", e)
