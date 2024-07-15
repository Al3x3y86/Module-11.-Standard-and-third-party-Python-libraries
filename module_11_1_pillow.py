from PIL import Image, ImageFilter

# Pillow предоставляет широкие возможности для работы с изображениями, включая их открытие,
# изменение размера, применение эффектов (например, размытие),
# конвертацию в другие форматы и сохранение результатов обработки.

# 1. Открытие и обработка изображения
image = Image.open('images.jpeg')
image.show()

# 2. Изменение размера изображения
resized_image = image.resize((200, 200))
resized_image.show()

# 3. Применение эффекта размытия (Blur) к изображению
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# 4. Сохранение изображения в другом формате
image.save('output.png')
