import os
from unittest import TestCase

from tests.fixtures import constants
from filesconverter import converter


class TestConverter(TestCase):
    object = None

    # Runs once at the start of every run
    def setup_class(self):
        self.object = converter.FileConverter(constants.CFG_FILE_PATH)

    def test_positive_cfg_data_items(self):
        print("== test_positive_cfg_data_items starting")
        self.object.convert()
        assert self.object.data == constants.DATA_FOR_CFG

    def test_positive_yml_data_items(self):
        self.object = converter.FileConverter(constants.YML_FILE_PATH)
        print("== test_positive_cfg_data_items starting")
        self.object.convert()
        assert self.object.data == constants.DATA_FOR_YML

    def test_get_configuration(self):
        self.object.get_configuration(constants.new_name)
        assert os.path.exists(constants.new_name) is True

    def test_get_configuration_env(self):
        self.object.get_configuration(constants.new_name)
        assert os.path.exists(constants.new_name_env) is True


class TestConverterNegetive(TestCase):
    api_object = None

    # Runs once at the start of every run
    # Runs once at the start of every run
    def setup_class(self):
        self.object = converter.FileConverter(constants.NE_FILE_PATH)

    def test_negetive_filename(self):
        # Give invalid key 'log_names' has a type - the correct key is 'log_name'
        self.object.convert()
        assert self.object.data is None
        assert self.object.error == constants.error1

    def test_negetive_getconfiguration(self):
        # Give invalid key 'log_names' has a type - the correct key is 'log_name'
        self.object.get_configuration(constants.neg_new_name_env)
        assert self.object.error == constants.error1
        # Must have an error field
        assert self.object.data is None
        assert os.path.exists(constants.neg_new_name_env) is False
