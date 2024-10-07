# This script generates a grid of representative images from the BioVid dataset.
# It counts the number of images for each participant and displays them in a grid,
# along with their participant ID and image count. The final grid is saved as a PNG file.

import os
import matplotlib.pyplot as plt
from PIL import Image

# Path to the directory containing your images
image_directory = "Biovid Training Sets/1000 pain frames"

# Uncomment to use neutral frames instead.
# image_directory = "Biovid Training Sets/1000 neutral frames"

# Dictionary to store counts for each person
person_counts = {}


# Each image's name includes a unique ID that identifies the participant. 
# This section counts the number of images for each participant based on their unique ID.
for filename in os.listdir(image_directory): # Iterate through each image in the directory
    parts = filename.split('_')

    if len(parts) >= 2 and parts[0].isdigit():
        # Extract the person identifier 
        person_identifier = parts[0]

        # Increment the count for this person
        person_counts[person_identifier] = person_counts.get(person_identifier, 0) + 1


persons = list(person_counts.keys())
counts = list(person_counts.values())

# Set up a 6x15 grid
#fig, axes = plt.subplots(6, 15, figsize=(25, 15))
fig, axes = plt.subplots(6, 10, figsize=(25, 20))
fig.suptitle(f'Representative Images and Counts for Each Person in Pain dataset ({len(persons)} participants)', fontsize=25)

# Display images in the grid
for i, ax in enumerate(axes.flatten()):
    if i < len(persons):
        person_id = persons[i]
        image_filename = next((f for f in os.listdir(image_directory) if f.startswith(f"{person_id}_")), None)

        if image_filename:
            img_path = os.path.join(image_directory, image_filename)
            img = Image.open(img_path)
            ax.imshow(img)
            ax.set_title(f"ID: {person_id}\nCount: {counts[i]}",fontsize=17)
            ax.axis('off')
    else:
        ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.95])


# Save the resulting image as a PNG file in the current directory
plt.savefig("pain_participants.png")

#plt.show()