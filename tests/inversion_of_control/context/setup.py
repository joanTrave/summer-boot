import os

from summer.inversion_of_control.service_locator import discover_services

executable_parent_path = os.path.dirname(os.path.abspath(__file__))


def setup():
    discover_services(executable_parent_path)
