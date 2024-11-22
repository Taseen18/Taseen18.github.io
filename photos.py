import os
import json

# Directories
photos_directory = "photos"
compressed_directory = "compressed"
output_file = "photos.json"

# Supported image file extensions
image_extensions = {".jpg", ".jpeg", ".png", ".gif"}

def generate_photos_json(original_dir, compressed_dir, output):
    photos = []

    # Get a list of compressed files
    compressed_files = {os.path.basename(f): os.path.join(compressed_dir, f).replace("\\", "/")
                        for f in os.listdir(compressed_dir) if os.path.splitext(f)[1].lower() in image_extensions}

    # Walk through the original directory to find full-resolution files
    for root, _, files in os.walk(original_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                # Full-resolution image path
                full_path = os.path.join(root, file).replace("\\", "/")
                
                # Look for corresponding compressed image
                compressed_path = compressed_files.get(file)

                if compressed_path:
                    photos.append({
                        "full": full_path,
                        "compressed": compressed_path
                    })
                else:
                    print(f"Warning: No compressed version found for {file}")

    # Write the list of photos to a JSON file
    with open(output, "w") as json_file:
        json.dump(photos, json_file, indent=4)
    print(f"Generated {output} with {len(photos)} photos.")

# Ensure the compressed directory exists
if not os.path.exists(compressed_directory):
    print(f"Error: Compressed directory '{compressed_directory}' does not exist.")
else:
    # Run the script
    generate_photos_json(photos_directory, compressed_directory, output_file)
