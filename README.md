# Mouse Heading Angle in Arena

In the study of animal behavior, heading angle can be an important feature when trying to understand ethograms (a list of species-specific behaviors).

In attack-flee studies, there is a prey (mouse) and a predator (spider). 2D videos are recorded as the mouse interacts with the spider in an arena. To better understand mice behavior with respect to the spider, heading angle is calculated to understand the relationship between various behaviors and the locations/positions of the predator and prey. 

## Methods
1. Record videos of mice and spider in arena.
2. Train a pose estimation model using computer vision techniques (DeepLabCut) to accurately estimate body parts of the mice and spider throughout the duration of the video.
3. Evaluate the model and analyze each video using this model.
4. Once each video is analyzed, determine the behavior bouts of interest (when the mouse and spider are interacting with one another).
5. For each frame of a single bout (30 frames per second), two vectors are calculated:
    - HeadCenter --> Nose
    - HeadCenter --> SpiderCenter
7. Once the two vectors are calculated, the heading angle is calculated. (The angle between the two calculated vectors)
8. For each frame where the spider and mouse are interacting, the heading angle is updated. Otherwise, the heading angle is set to 0.0.
9. A new csv is saved from the updated dataframe for further analysis of the relationship between heading angle and animal behavior.

## To run your own DeepLabCut files through:
1. Download the Python files to your computer (an example Excel file has been added to the respository for better understanding).
2. In the command line, run 'python spider_heading_angles.py'
   - When the first prompt appears, input the file path to the folder that contains the Excel files from your DLC output.
   - The script will load your files, update the heading angles, and output a file titled '{file_name}_angles.csv' (ensures you have your original data and also the angle data)
