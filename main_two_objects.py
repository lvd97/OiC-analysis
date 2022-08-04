import pandas as pd
from exploration_estimation_two_objects import aggregated_info, get_info

p =0.4    #Set here the p-cutoff
offset = 5
fps = 12.5
inter = 300 #The table with results will also specify the total exploration time up until this frame number

results = pd.DataFrame(
    columns=['animal', 'object1', 'object2', 'inter_object1', 'inter_object2', 'l_average'])

animal_list= [417271, 417272] #Fill in the animal numbers (video titles without '.mp4') of the videos that should be analysed 

for animal in animal_list:
    animal = str(animal)
    df = pd.read_csv('directory' +
                     animal+'DLC_resnet50_extra2Jun22shuffle1_1000000.csv', skiprows=2)
    coords_object1 = pd.read_csv(       #Specify were the coordinates of the objects can be found, name them e.g. 'animalnumber_object1.csv'
        '/Users/lindevandongen/Documents/Object-in-Context/Coordinates_objects_testing_pilot/'+animal+'_bulb.csv')
    coords_object2 = pd.read_csv(                   
        '/Users/lindevandongen/Documents/Object-in-Context/Coordinates_objects_testing_pilot/'+animal+'_jar.csv')                               
    video = '/Volumes/Samsung_T5/DLC/short_videos_pilot_testing/'+animal+'.mp4' #Specify where the behavioural videos can be found
    outpath_video = '/Users/lindevandongen/Downloads/' #Specify the directory where the DLC videos are saved

    df = get_info(animal, p, offset, df, fps, coords_object1,
                  coords_object2, video, outpath_video) #Also specify 'make_video=False' if you do not want the videos to be created 
    results = aggregated_info(df, fps, results, animal, inter)

results.to_csv(
    '/Users/lindevandongen/Downloads/hoi.csv', index=False) #Specify the directory where the results are saved 
