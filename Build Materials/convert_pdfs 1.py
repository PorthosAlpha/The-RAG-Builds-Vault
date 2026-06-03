import pymupdf4llm
import os
from pathlib import Path

# We use Path.home() to automatically find your /Users/dr.richardmoncriffe folder
home_dir = str(Path.home())
input_dir = os.path.join(home_dir, "target research folder")
output_dir = os.path.join(home_dir, "4-25-26 Converted PDFs")

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the target folder
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(input_dir, filename)
        md_filename = filename[:-4] + ".md"
        md_path = os.path.join(output_dir, md_filename)
        
        print(f"Converting: {filename}...")
        
        try:
            # This is where the magic happens
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_text)
            print(f"  -> Successfully saved {md_filename}")
        except Exception as e:
            print(f"  -> Error converting {filename}: {e}")

print("\nAll conversions finished!")
