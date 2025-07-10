# Egg Quality Detection by Detecting Cracks in the Shell
## 1. Background
Eggs are one of the staple foods consumed by the general public in large quantities due to their high nutritional value, including protein, vitamins and minerals.  Quality is an important factor that determines the value of a product and its durability.  However, the quality of eggs can be affected by several factors, one of which is cracks in the eggshell.  Cracks, even slight ones, can act as a barrier for bacteria such as Salmonella, making them unsafe for consumption and can cause serious health problems.
Traditionally, the selection and quality assessment process in many industries still relies heavily on manual methods.  This process involves visual inspection by employees, which not only consumes time and effort, but is also a significant risk factor for human error. As artificial intelligence (AI) technology advances, particularly in the field of computer vision, there are growing opportunities to automate the egg quality selection process. One of the most effective algorithms for real-time object detection is YOLO (You Only Look Once). The latest version, YOLOv8, offers a winning combination of speed and accuracy, making it a perfect candidate for industrial applications.

Implementation Stages of YOLOv8:
1. Data Collection: Collect comprehensive information about egg images.  In this project, the data used was taken from https://universe.roboflow.com/crackedeggs
2. Model Training: The YOLOv8 model was trained using the aforementioned dataset. During this process, the learning model examines patterns, text, and visual elements that distinguish between intact eggshells and cracks.
3. Implementation: Once completed, the resulting model (best.pt) can be integrated into the system. Using the image file, the system will display the egg detection results, and the model will quickly adapt each egg to its shell condition.

## 2. Objective
Implement the YOLOv8 algorithm to detect and classify eggshell conditions into two categories: “Good” and “Cracked”.

## 3. Benefits
1. Improve the efficiency of the egg selection process
2. Contribute to the application of computer vision in agriculture and food.

## 4. Results
