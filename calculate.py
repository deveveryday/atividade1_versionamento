def calculate_percentage(values):
  for value in values:
    print(f"${value[0] * (value[1] / 100)}")


def add_percentage(values):
  for value in values:
    print(f"${value[0] + (value[0] * (value[1] / 100))}")


def reduce_percentage(values):
  for value in values:
    print(f"${value[0] - (value[0] * (value[1] / 100))}")