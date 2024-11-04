import os
import shutil
import sys
from datetime import datetime
from PIL import Image, ExifTags


def extract_capture_date(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            date_tags = ['DateTimeOriginal', 'DateTimeDigitized', 'DateTime']
            for date_tag in date_tags:
                for tag, value in exif_data.items():
                    if ExifTags.TAGS.get(tag) == date_tag:
                        date = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                        return date.year, date.month

        print(f"Nincs információ ebben a képben: {image_path}.")
    except Exception as e:
        print(f"Baj történt ezzel a fájllal: {image_path}: {e}")
    return None, None


def organize_photos_by_date(source_folder):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heif')):
                file_path = os.path.join(root, filename)
                year, month = extract_capture_date(file_path)
                if year is None or month is None:
                    print(f"Nincs infó a dátumról ebben a fájlban: {filename}.")
                    continue
                year_folder = os.path.join(source_folder, str(year))
                month_folder = os.path.join(year_folder, f"{month:02}")
                os.makedirs(month_folder, exist_ok=True)
                target_path = os.path.join(month_folder, filename)
                shutil.move(file_path, target_path)
                print(f"{filename} átmozgatva ide: {target_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Használat: imageOrganizer.py <elérési út> (pl.: python imageOrganizer.py C:/képek/)")
        sys.exit(1)
    source_folder = sys.argv[1]
    if not os.path.isdir(source_folder):
        print(f"Hiba: {source_folder} nem egy érvényes elérési út")
        sys.exit(1)

    organize_photos_by_date(source_folder)
