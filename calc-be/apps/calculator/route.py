from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData  # Make sure this is defined correctly
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    # Decode the base64 image data
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    
    # Convert byte data to image
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)

    # Analyze the image (make sure this function exists in utils)
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    
    # Prepare the response data
    response_data = []
    for response in responses:
        response_data.append(response)

    # Log the response for debugging
    print('Responses:', response_data)

    return {
        "message": "Image processed",
        "data": response_data,  # Corrected to use response_data
        "status": "success"
    }
