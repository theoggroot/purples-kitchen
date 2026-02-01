import os
from pathlib import Path

# 1. IDENTIFY WHERE WE ARE
current_file = Path(__file__)
root_dir = current_file.parent
images_dir = root_dir / "assets" / "images"

print("-" * 50)
print(f" DIAGNOSTIC REPORT")
print("-" * 50)
print(f"1. Script location:   {current_file}")
print(f"2. Detected Root:     {root_dir}")
print(f"3. Target Image Folder: {images_dir}")
print("-" * 50)

# 2. CHECK IF FOLDER EXISTS
if not images_dir.exists():
    print("❌ ERROR: The folder 'assets/images' does NOT exist.")
    print("   Please check your spelling or folder structure.")
else:
    print("✅ SUCCESS: Image folder found!")
    
    # 3. LIST ALL FILES INSIDE (To check exact names)
    print("\n   FILES FOUND IN FOLDER:")
    files = list(images_dir.glob("*"))
    if not files:
        print("   ⚠️  The folder is empty!")
    else:
        for f in files:
            print(f"   📄 {f.name}")

print("-" * 50)