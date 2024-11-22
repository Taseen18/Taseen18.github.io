import os
import json

# Directory containing your photos
photos_directory = "photos"
output_file = "photos.json"

# Supported image file extensions
image_extensions = {".jpg", ".jpeg", ".png", ".gif"}

def generate_photos_json(directory, output):
    photos = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has a valid image extension
            if os.path.splitext(file)[1].lower() in image_extensions:
                # Get the relative path of the file
                relative_path = os.path.join(root, file).replace("\\", "/")
                photos.append(relative_path)

    # Write the list of photos to a JSON file
    with open(output, "w") as json_file:
        json.dump(photos, json_file, indent=4)
    print(f"Generated {output} with {len(photos)} photos.")

# Run the script
generate_photos_json(photos_directory, output_file)
