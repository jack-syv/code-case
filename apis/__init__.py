from flask_restx import Api
from .property import api as property_ns

api = Api(version="0.1",
          title="Hjemla Code-case",
          description="Basic Rest API")

api.add_namespace(property_ns, path='/property')