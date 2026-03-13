import json
import os
import config
import sys

if len(sys.argv) == 2:
    exam_code = sys.argv[1]
else:
    exam_code = config.exam_name_str
# Construct the file path
file_path = os.path.join("JSON", f"{exam_code}_jp_exam.json")
print(file_path)

# Check if the file exists
if not os.path.exists(file_path):
    print("Error: File does not exist")
else:
    # Open the file
    file = open(file_path, "r", encoding="utf-8")
    data = json.load(file)
    print(data)

    new_file_path = os.path.join("JSON", f"{exam_code}_jp_exam.json")
    new_file = open(new_file_path, "w", encoding="utf-8")
                
    json.dump(data, new_file, ensure_ascii = False, separators=(',',':'))

           


