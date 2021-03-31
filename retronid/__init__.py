import uuid

def generate():
  uuide = str(uuid.uuid1())
  uuidSpl = uuide.split("-")
  retronid = f"{uuidSpl[0]}{uuide[-2]}"
  return retronid
