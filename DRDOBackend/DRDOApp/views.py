from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .ocr import extract_text_from_image
from rest_framework import status
from decouple import config
class OCRView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # Extract the image from the request
        image = request.FILES.get('image')
        image1=request.FILES.get('image1')

        if not image:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Perform OCR on the image
        extracted_text = extract_text_from_image(image)
        extracted_text1 = extract_text_from_image(image1)

        # Save the data (optional)
      

        # Return the extracted text as a response
        return Response({"extracted_text": extracted_text,
                         "extracted_text1": extracted_text1}, status=status.HTTP_200_OK)

    def get(request, *args, **kwargs):
        name=config("NAME")
        return Response({"name":name},status=status.HTTP_200_OK)
        
    

