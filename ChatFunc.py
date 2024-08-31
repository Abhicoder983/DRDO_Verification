from openai import OpenAI
import json
import os
import base64

os.environ['OPENAI_API_KEY'] = '<Insert Key Here>'


client = OpenAI()


def load_json_schema(schema_file: str) -> dict:
    with open(schema_file, 'r') as file:
        return json.load(file)

# Load the JSON schema
invoice_schema = load_json_schema('docstruct.json')

# Open the local image file in binary mode
def img(image_path):
    with open(image_path, 'rb') as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        return image_base64


#THIS Is Main, You Just have to use It
def jsonData(image_path):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "provide JSON file that represents this document. Use this JSON Schema: " +
                        json.dumps(invoice_schema)},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img(image_path)}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500,
    )

    json_data = json.loads(response.choices[0].message.content)
    return json_data
