# sneaky lil feature ;D
onion = ["🧅", "onlon"]

def get_response(message: str) -> str:
  p_message = message.lower()
  for m in onion:
    if p_message == m:
      return "**CULT!**"
  return