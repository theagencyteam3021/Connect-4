import inference
model = inference.get_model("connect4-lxv2j/2", "fxXBp7IHZMUOlxGJbueP")
results = model.infer(image="/webcam_image.jpg")

###
results[0].predictions

###
for result in results[0].predictions:
  print(f"{result.x}, {result.y}, {result.class_name}")

###
from PIL import Image

image = Image.open("/webcam_image.jpg")

###
from PIL import Image

image = Image.open("/webcam_image.jpg")

###

def package(results):
  formattedList = []
  for result in results[0].predictions:
    formattedList.append([result.x, result.y, result.class_name])
  return formattedList