# Import necessary libraries from Azure and Python
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
import json

# ----------------------------------------
# Step 1: Set up Azure credentials
# ----------------------------------------
# These should be set as environment variables before running the script
subscription_key = os.environ.get("VISION_KEY")
endpoint = os.environ.get("VISION_ENDPOINT")

# Check if credentials are missing
if not subscription_key or not endpoint:
    raise ValueError("Missing Azure credentials. Please set VISION_KEY and VISION_ENDPOINT.")

# Create a client to connect to Azure Computer Vision
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# ----------------------------------------
# Step 2: Load image URLs from JSON file
# ----------------------------------------
# The file 'image.json' should contain a list of image URLs
with open("image.json", "r") as f:
    data = json.load(f)
    image_urls = data.get("images", [])

# Check if the list is empty
if not image_urls:
    raise ValueError("No image URLs found in image.json.")

# ----------------------------------------
# Step 3: Analyze each image using Azure API
# ----------------------------------------
for idx, remote_image_url in enumerate(image_urls):
    # You can skip any image by commenting out its URL in image.json
    print(f"\n🔍 Analyzing image {idx + 1}...")

    try:
        # Send the image to Azure and get tags
        tags_result = computervision_client.tag_image(remote_image_url)

        # Print the tags with confidence scores
        print("📌 Tags found:")
        if not tags_result.tags:
            print("No tags detected.")
        else:
            for tag in tags_result.tags:
                print(f"- {tag.name} ({tag.confidence * 100:.2f}%)")

    except Exception as e:
        # If the image URL is broken or inaccessible, skip it
        print(f"⚠️ Skipping image {idx + 1} due to error: {e}")

# ----------------------------------------
# Step 4: Done!
# ----------------------------------------
print("\n✅ Finished analyzing all images.")
