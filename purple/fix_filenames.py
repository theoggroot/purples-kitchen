import os
from pathlib import Path

# Setup paths
root_dir = Path(__file__).parent
images_dir = root_dir / "assets" / "images"

print(f"🔧 Scanning {images_dir} for double extensions...\n")

# List of double extensions we want to fix
bad_suffixes = [".jpg.jpg", ".gif.gif", ".png.png"]

count = 0

for file_path in images_dir.iterdir():
    name = file_path.name
    
    # Check if the file ends with any of our "bad" suffixes
    for bad in bad_suffixes:
        if name.endswith(bad):
            # Calculate new name: "image.jpg.jpg" -> "image.jpg"
            # We slice off the last 4 characters (.jpg)
            clean_name = name[:-4] 
            new_path = images_dir / clean_name
            
            # Rename the file
            try:
                os.rename(file_path, new_path)
                print(f"✅ Fixed: {name}  -->  {clean_name}")
                count += 1
            except FileExistsError:
                print(f"⚠️  Skipped: {clean_name} already exists.")
            except Exception as e:
                print(f"❌ Error renaming {name}: {e}")

if count == 0:
    print("\n🎉 No issues found! Your files look good.")
else:
    print(f"\n🎉 Successfully fixed {count} files.")