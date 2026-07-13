"""
AI DATASET INSPECTOR

Author: Aanshi Jain
Version: 3.0

Description:
A command-line Python tool that scans image datasets,
validates user-selected file extensions, and generates category-wise
and extension-wise reports.
"""


from pathlib import Path
# Check if the dataset folder exists
dataset = Path("dataset")

if not dataset.exists():
    print("Dataset folder not found")
    print("Please place your dataset inside the 'dataset' folder.")
    exit()
# Initialize counters and data structures
folder_count = 0
file_count = 0
invalid_count = 0
extension_count = {}
category_count = {}
invalid_extensions = {}

# Get allowed file extensions from the user
enter_extension = input("Enter Extensions: ")
extension_list = enter_extension.split()
if extension_list == []:
   ext = input("Please enter at least one extension (e.g., .jpg png): ")
   if ext == "":
    print("No extension entered. Exiting Program👋")
    exit()
   else:
      extension_list.append(ext)
revised_extension_list = []

# Normalize extensions
# (convert to lowercase and ensure each starts with '.')
for extension in extension_list:
   extension = extension.lower()
   if extension[0] == ".":
       revised_extension_list.append(extension)
   else:
       extension = "." + extension
       revised_extension_list.append(extension)
# Remove duplicate extensions for faster lookup
revised_list_set = set(revised_extension_list)

# initial counter of every extention = 0
for extension in revised_list_set:
    extension_count[extension] = 0

# Scan every category folder in the dataset
for folder in dataset.iterdir():
   if folder.is_dir():
      folder_count += 1
      categoryfiles_count = 0
      for file in folder.iterdir():
         category_count[folder.name] = categoryfiles_count
         file_count += 1
         categoryfiles_count += 1
         # Validate each file and update extension statistics
         if file.suffix in revised_list_set:
            if file.suffix in extension_count:
                extension_count[file.suffix] += 1
            else:
                extension_count[file.suffix] = 1
         else:
            invalid_count += 1
            if file.suffix in invalid_extensions:
                invalid_extensions[file.suffix] += 1  
            else:
                invalid_extensions[file.suffix] = 1

# Display the final inspection report
print ("📂 DATASET SUMMARY")
print("------------------------")
print("Total Categories: ", folder_count)
print("Total files: ",file_count)
for key, value in extension_count.items():
   print(f"Total {key} files : {value}") 
print("Total invalid files: ", invalid_count)
print("------------------------")
print("📂 CATEGORY REPORT")
print("------------------------")
for key, value in category_count.items():
   print(key, ":", value)
print("------------------------")
print("⚠ INVALID EXTENSIONS ")
print("------------------------")
for key, value in invalid_extensions.items():
      print(key, ":", value)
print("=====================================================")
print("Inspection Completed Successfully ✅")
print("=====================================================")