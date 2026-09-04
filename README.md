# Project Title 
# Simple Spatial Objects in Python 

# How to Design a Spatial Object
# 1. Create a class shell
# 2. Add identity and coordinates
# 3. Enforce Spatial Validity
# 4. Add Optional Meaning
# 5. Add a Simple Instance Method
# 6. Add Spatial Interaction
# 7. Add a Static Method for Spatial Math
# 8. Add a Class Method
# 9. Add Semantic Behavior


# Run Instructions
# Load your csv file to /data folder
# Run the runner script run_lab2.py in the terminal [python src/run_lab2.py]
# Once finished in running the runner script, you can find the resulting output files in /output folder

# Reflections

# 1. Object vs Geometry
# How did modeling points as objects change the way you thought about the data compared to treating them as rows in a table?
# Modeling points made me see them as entities that represents something in the real world with their own properties, rather than just rows in a table. 

# 2. Responsibility 
# Which behaviors belonged in Point, which belonged in PointSet, and which belonged in the runner script? Give one concrete example. 
# Point handles behaviors specific to a single point while PointSet handles behaviors involving multiple points. The runner script handles the overall workflow for the project. 
# Examples:
# Point - definition of distance to another point
# PointSet - definition of bounding box
# Runner Script - data inspection, printing of summary

# 3. Modeling Insight 
# How did separating geometry, meaning, and behavior make the spatial logic easier (or harder) to understand?
# Separating geometry, meaning, and behavior made the spatial logic easier to understand because each of these components were assigned a specific role or responsibility. This helps us not mix up these roles which makes the analysis and troubleshooting easier.