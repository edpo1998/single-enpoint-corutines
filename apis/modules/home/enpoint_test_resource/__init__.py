from flask_restx import Namespace, fields
api = Namespace(f"ENPOINT - Test")

from .enpoint_test_resource import EnpointResource