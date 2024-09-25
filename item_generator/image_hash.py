import os
import imagehash
from PIL import Image
from collections import defaultdict
from itertools import combinations
from multiprocessing import Pool, cpu_count

# Step 1: Compute perceptual hashes for all images
def compute_hash(image_path):
    try:
        with Image.open(image_path) as img:
            # You can choose different hash functions: average_hash, phash, dhash, whash
            hash_value = imagehash.phash(img)
            return (image_path, hash_value)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return (image_path, None)


# Step 2: Build the hash list
def build_hash_list(image_folder):
    image_paths = list()
    # Collect all image file paths
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_paths.append(os.path.join(root, file))
    print(f"Total images found: {len(image_paths)}")

    # Use multiprocessing to speed up hash computation
    pool = Pool(processes=cpu_count())
    hash_list = pool.map(compute_hash, image_paths)
    pool.close()
    pool.join()

    # Filter out any images that couldn't be processed
    hash_list = [item for item in hash_list if item[1] is not None]
    return hash_list

# Step 3: Group images by hash similarity
def group_similar_images(hash_list, threshold=5):
    # Build a dictionary to hold groups
    groups = defaultdict(list)

    # Create buckets based on hash values
    hash_buckets = defaultdict(list)
    for image_path, hash_value in hash_list:
        hash_buckets[str(hash_value)].append(image_path)

    # Extract the unique hash keys
    hash_keys = list(hash_buckets.keys())
    total_keys = len(hash_keys)
    print(f"Total unique hash buckets: {total_keys}")

    # Keep track of processed keys
    processed_keys = set()

    # Iterate over the hash keys
    for i in range(total_keys):
        key1 = hash_keys[i]
        if key1 in processed_keys:
            continue  # Skip if already processed
        images1 = hash_buckets[key1]
        hash1 = imagehash.hex_to_hash(key1)

        # Use the first image path as the group identifier
        group_id = images1[0]

        # Initialize the group
        if group_id not in groups:
            groups[group_id].extend(images1)

        # Compare with subsequent hashes
        for j in range(i + 1, total_keys):
            key2 = hash_keys[j]
            if key2 in processed_keys:
                continue  # Skip if already processed
            hash2 = imagehash.hex_to_hash(key2)
            distance = hash1 - hash2
            if distance <= threshold:
                images2 = hash_buckets[key2]
                # Add images to the group
                groups[group_id].extend(images2)
                # Mark key2 as processed
                processed_keys.add(key2)
        # Mark key1 as processed
        processed_keys.add(key1)

    print(f"Total groups formed: {len(groups)}")
    return groups


# Main execution
if __name__ == "__main__":
    image_folder = 'item_inventory_images'  # Folder where images are stored
    print("Building hash list...")
    hash_list = build_hash_list(image_folder)

    print("Grouping similar images...")
    groups = group_similar_images(hash_list, threshold=1)

    # Output the groups
    for group_id, image_paths in groups.items():
        print(f"\nGroup {group_id}:")
        for image_path in image_paths:
            print(f"  {image_path}")
