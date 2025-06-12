import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def process_image(image_file, x=None, y=None, width=None, height=None):
    """
    Processa a imagem: aplica crop se coordenadas forem fornecidas e converte para JPEG.
    Retorna (file_name, ContentFile) pronto para salvar.
    """
    image = Image.open(image_file)

    # Aplica crop se todos os parâmetros estiverem presentes
    if None not in (x, y, width, height):
        x, y, width, height = map(int, (x, y, width, height))
        if x + width > image.width or y + height > image.height:
            raise ValueError("Dimensões de crop inválidas.")
        image = image.crop((x, y, x + width, y + height))

    # Converte imagem para RGB (removendo alpha se existir)
    if image.mode == 'RGBA':
        background = Image.new('RGB', image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])  # canal alpha
        image = background
    elif image.mode != 'RGB':
        image = image.convert('RGB')

    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)

    file_name = os.path.splitext(os.path.basename(image_file.name))[0] + '.jpg'
    return file_name, ContentFile(buffer.read())
