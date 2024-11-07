import requests
import os
from PIL import Image
from io import BytesIO

# Set up API key and search parameters
api_key = 'ACCESS_KEY_FROM_UNSPLASH_HERE'
url = "https://api.unsplash.com/search/photos"
query_params = {
    'query': 'avatar',
    'client_id': api_key,
    'per_page': 10
}

# Create a folder to save the images
os.makedirs('avatars', exist_ok=True)

# Make the request to Unsplash API
response = requests.get(url, params=query_params)

if response.status_code == 200:
    data = response.json()
    images = data['results']

    # Download and save images
    for i, image_data in enumerate(images):
        image_url = image_data['urls']['small']
        img_response = requests.get(image_url)
        
        if img_response.status_code == 200:
            img = Image.open(BytesIO(img_response.content))
            img.save(f"../images/avatar_{i + 1}.jpg")
        else:
            print(f"Failed to download image {i + 1}")
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(response.text)