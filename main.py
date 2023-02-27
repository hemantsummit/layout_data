import os
import json
from paddleocr import PaddleOCR
os.environ["KMP_DUPLICATE_LIB_OK"]="True"
# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Path to the input images folder
input_folder = './documents/pfs_form'

# Path to the output JSON files folder
output_folder = './new_documents/pfs_form'

# Loop through all the images in the input folder
for image_name in os.listdir(input_folder):
    if image_name.endswith('.jpg') or image_name.endswith('.png'):
        
        # Load the image
        image_path = os.path.join(input_folder, image_name)

        # Perform OCR on the image
        result = ocr.ocr(image_path, cls=True)
        # print(result)
        # Create a dictionary to store the results
        results_dict = []

        # Loop through each detected text and add it to the dictionary
        for text in result[0]:
            top = max(text[0][0][1],text[0][1][1],text[0][2][1],text[0][3][1])
            bottom = min(text[0][0][1],text[0][1][1],text[0][2][1],text[0][3][1])
            left = min(text[0][0][0],text[0][1][0],text[0][2][0],text[0][3][0])
            right = max(text[0][0][0],text[0][1][0],text[0][2][0],text[0][3][0])
            results_dict.append({
                'word':text[1][0],
                'bounding_box':[left, top, right, bottom]
            })

        # Save the dictionary as a JSON file with the same name as the image
        json_path = os.path.join(output_folder, image_name.replace('.jpg', '.json').replace('.png', '.json'))
        with open(json_path, 'w') as f:
            json.dump(results_dict, f)
