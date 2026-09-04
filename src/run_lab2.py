import os 
import json 
import pandas as pd 
import matplotlib.pyplot as plt

from spatial import PointSet 

# ----------------------------- 
# Paths 
# ----------------------------- 
DATA_PATH = "data/points.csv" 
OUTPUT_DIR = "output" 
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "lab2_report.json") 
PLOT_PATH = os.path.join(OUTPUT_DIR, "lab2_preview.png") 
# ----------------------------- 
# A. Read the CSV file 
# ----------------------------- 
try: 
    pointset = PointSet.from_csv("data/points.csv") 
except FileNotFoundError: 
    print(f"Error: Cannot find file at '{DATA_PATH}'.") 
    print("Make sure you have: data/points.csv") 
    raise 

num_rows, num_cols = pointset.shape
 

print("\nBounding Box") 
print("------------") 

if pointset.bbox() is None:
    print("No valid coordinate rows found. Bounding box cannot be computed.") 
else: 
    print(pointset.bbox())  # Print the bounding box of valid coordinates

# ----------------------------- 
# E. Save outputs 
# ----------------------------- 
# Create output folder if it doesn't exist 
os.makedirs(OUTPUT_DIR, exist_ok=True) 

# Build summary dictionary 
summary = { 
    "total_point_count": int(pointset.count()),
    "bbox": pointset.bbox(),   
    "counts_per_tag": {"poi": pointset.filter_by_tag("poi").count(), 
                       "school": pointset.filter_by_tag("school").count(), 
                       "gate": pointset.filter_by_tag("gate").count(), 
                       "building": pointset.filter_by_tag("building").count(),
                       "landmark": pointset.filter_by_tag("landmark").count(),
                       "road": pointset.filter_by_tag("road").count()}

} 


# Write summary.json
with open(SUMMARY_PATH, "w", encoding="utf-8") as f: 
    json.dump(summary, f, indent=2) 

print(f"\nSaved summary to: {SUMMARY_PATH}") 

# Save scatter plot (valid coords only) 
plt.figure() 
if pointset.count() == 0: 
    # Create an empty plot with message in title 
    plt.title("Preview Plot (No valid coordinates to plot)") 
else: 
    plt.scatter(
    [p.lon for p in pointset.points],
    [p.lat for p in pointset.points]
) 
    plt.title("UP Diliman Landmarks (lon vs lat)") 
    plt.xlabel("Longitude") 
    plt.ylabel("Latitude") 

plt.savefig(PLOT_PATH, dpi=150, bbox_inches="tight") 
plt.close() 

print(f"Saved scatter plot to: {PLOT_PATH}") 
print("\n=== END OF REPORT ===")