import inference
model = inference.get_model("connect4-lxv2j/2", "fxXBp7IHZMUOlxGJbueP")
results = model.infer(image="/content/WIN_20240909_18_06_29_Pro.jpg")

###
results[0].predictions

###
for result in results[0].predictions:
  print(f"{result.x}, {result.y}, {result.class_name}")

###
from PIL import Image

image = Image.open("/content/WIN_20240909_18_06_29_Pro.jpg")

###
from PIL import Image

image = Image.open("/content/WIN_20240909_18_06_29_Pro.jpg")

###

def package(results):
  formattedList = []
  for result in results[0].predictions:
    formattedList.append([result.x, result.y, result.class_name])
  return formattedList