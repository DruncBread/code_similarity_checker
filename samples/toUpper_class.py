class StringConverter:
  def __init__(self, string):
    self.string = string

  def to_upper(self):
    return self.string.upper()

converter = StringConverter("hello world")
print(converter.to_upper())
