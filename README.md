# Mouse Heading Angle in Arena

In the study of animal behavior, heading angle can be an important feature when trying to understand ethograms (a list of species-specific behaviors).

In attack-flee studies, there is a prey (mouse) and a predator (spider). 2D videos are recorded as the mouse interacts with the spider in an arena. To better understand mice behavior with respect to the spider, heading angle is calculated to understand the relationship between various behaviors and the locations/positions of the predator and prey. 

## Methods
1. Record videos of mice and spider in arena.
2. Train a pose estimation model using computer vision techniques (DeepLabCut) to accurately estimate body parts of the mice and spider throughout the duration of the video.
3. Evaluate the model and analyze each video using this model.
4. Once each video is analyzed, determine the behavior bouts of interest (when the mouse and spider are interacting with one another).
5. For each frame of the bout (30 frames per second), two vectors are calculated: (1) HeadCenter --> Nose (2) HeadCenter --> SpiderCenter
6. Once the two vectors are calculated, the heading angle is calculated. (The angle between the two calculated vectors)
7. For each frame where the spider and mouse are interacting, the heading angle is updated. Otherwise, the heading angle is set to 0.0.
