import os

from summer.inversion_of_control.service_locator import discover_services

executable_parent_path = os.getcwd()


def setup():
    discover_services(executable_parent_path)
