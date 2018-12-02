
import pandas as pd 


cities = pd.read_csv('cities.csv')

output_points = pd.read_csv('points.csv')

output_points['City'] = ''

for i in range(0, len(output_points)):
    for j in range(0, len(cities)):
        if(output_points['X'][i] in range (cities['TopLeft_X'][j],cities['BottomRight_X'][j]+1) and output_points['Y'][i] in range (cities['TopLeft_Y'][j],cities['BottomRight_Y'][j]+1)) :
            output_points['City'][i] = cities['Name'][j]
            break
        else :
            output_points['City'][i] = 'None' 


output_points.to_csv('output_points.csv',index = False)
