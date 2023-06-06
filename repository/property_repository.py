repo = {}

def delete_property(property_id):
  try:
    del repo[property_id]
    return True
  except KeyError:
    return False

def get_property(property_id):
  try:
    return repo[property_id]
  except KeyError:
    return None

def update_property(property_id, data):
  repo[property_id] = data
  return True

def create_property(property_id, data):
  repo[property_id] = data
  return True