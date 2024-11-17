import os
from PIL import Image
import imagehash
from collections import defaultdict


def find_duplicate_images(directory):
    def get_image_metadata(file_path):
        try:
            with Image.open(file_path) as img:
                return img.info
        except Exception as e:
            print(f"Error reading metadata for {file_path}: {e}")
            return None

    def calculate_image_hash(file_path):
        try:
            with Image.open(file_path) as img:
                return str(imagehash.average_hash(img))
        except Exception as e:
            print(f"Error hashing {file_path}: {e}")
            return None

    duplicates = defaultdict(list)
    hashes = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
                metadata = get_image_metadata(file_path)
                image_hash = calculate_image_hash(file_path)

                if metadata and image_hash:
                    match_found = False
                    for hash_key, metadata_files in hashes.items():
                        if hash_key == image_hash or hash_key - imagehash.hex_to_hash(image_hash) < 5:
                            if any(metadata == get_image_metadata(other_file) for other_file in metadata_files):
                                duplicates[hash_key].append(file_path)
                                match_found = True
                                break

                    if not match_found:
                        hashes[image_hash] = [file_path]

    return {hash_key: files for hash_key, files in duplicates.items() if len(files) > 1}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="A program hasonló képeket keres metaadat és maga a kép alapján")
    parser.add_argument("directory", help="A könyvtár elérési útja, ahol a képek vannak.")
    args = parser.parse_args()

    duplicate_images = find_duplicate_images(args.directory)

    if duplicate_images:
        print("Duplikált képek:")
        for hash_key, files in duplicate_images.items():
            print(f"\nHash: {hash_key}")
            for file in files:
                print(f"  {file}")
    else:
        print("Nincs duplikált kép")
