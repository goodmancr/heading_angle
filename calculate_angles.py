import numpy as np
import pandas as pd
from tqdm import tqdm


# get vector between two points
def vector_between_points(point1, point2): return np.array(point2) - np.array(point1)


# get angle between two vectors
def angle_between(v1, v2):
    
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    radians_angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    
    return np.degrees(radians_angle)


# get the unit vector
def unit_vector(vector): return vector / np.linalg.norm(vector)


# iterating through df and calculating head angles
def calculating_angles(df):
    update_count = 0
    for idx, row in tqdm(df.iterrows(), 
                                     total=len(df), 
                                     desc="Calculating heading angles", 
                                     bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
                    
        if row['Spider_Light'] > 0.97:
            
            # get the points to calculate vectors
            head = row['headcenter x'], row['headcenter y']
            schnozz = row['nose x'], row['nose y']
            spider = row['light x'], row['light y']

            # calculate the vectors
            head_to_schnozz = vector_between_points(head, schnozz)
            head_to_spider = vector_between_points(head, spider)

            # calculate the angle
            df.at[idx, 'heading_angle'] = angle_between(head_to_schnozz, head_to_spider)
            update_count += 1
        else:
            df.at[idx, 'heading_angle'] = 0.0
    print("Updated", update_count, "rows...\n")
    return df
