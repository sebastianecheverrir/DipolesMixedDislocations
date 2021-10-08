#!/home/sebastian/PythonVEnvs/Atomistic/bin/python

############################################################

#28-04-2021
#Sebastian Echeverri Restrepo
#sebastianecheverrir@gmail.com

############################################################

#Script to calculate the 1 / 2 (111) dislocations on 
#  (110) planes in b.c.c. crystals

import numpy as np
import pandas as pd

#######################################
#Functions to calculate the agle between two vectors
# https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


#######################################
#Some parameters

#burgers vector (we use BCC Fe)
burgers = 2.8553122 * np.sqrt(3)/2

#values of the indices that we want to consider
beginIndex = -3
endIndex = -beginIndex+1

#Slip plane of the dislcoation
y_reference = np.array([-1,0,1])
y_reference_norm =  y_reference/np.linalg.norm(y_reference)

#Dislocation line
z_reference = np.array([1,-1,1])


#######################################
#cycles to form two vectors, z and x. They will take all the values
#    going from beginIndex to endIndex on each of their components
df = pd.DataFrame(columns = ['x', 'y', 'z', 'angle'])

for z_x in range(beginIndex,endIndex):
    for z_y in range(beginIndex,endIndex):
        for z_z in range(beginIndex,endIndex):
            for x_x in range(beginIndex,endIndex):
                for x_y in range(beginIndex,endIndex):
                    for x_z in range(beginIndex,endIndex):
                        #building the vectors
                        z = np.array([z_x, z_y, z_z])
                        x = np.array([x_x, x_y, x_z])
                        #calculating the cross product
                        y = np.cross(z,x)
                        #checking:
                        #  x, y and z are not vectors of zeroes
                        #  x and z are orthogonal 
                        if ( (not np.allclose(x,np.array([0,0,0]))) and \
                             (not np.allclose(y,np.array([0,0,0]))) and \
                             (not np.allclose(z,np.array([0,0,0]))) and \
                             (np.dot(z,x) == 0 )):
                            #normalising vector y
                            y_norm = y/np.linalg.norm(y)
                            #checking that the vector y coincides with the reference y
                            #    done to ensure that the slip plane is y_reference
                            if (np.allclose(y_norm,y_reference_norm)):
                                #calculating the minimum vectors composed of integers
                                x_int = (x/np.gcd.reduce(x)).astype(int)
                                y_int = (y/np.gcd.reduce(y)).astype(int)
                                z_int = (z/np.gcd.reduce(z)).astype(int)
                                #calculating the angle
                                angle = angle_between(z_int,z_reference)#*180/np.pi
                                #putting everything in the dataframe df
                                s = pd.Series(data = [x_int,y_int,z_int,\
                                                      angle, \
                                                      np.linalg.norm(x_int),\
                                                      np.linalg.norm(y_int),\
                                                      np.linalg.norm(z_int),\
                                                      x,y,z] , \
                                              index = ['x', 'y', 'z', \
                                                       'angle', \
                                                       'x_norm', 'y_norm', 'z_norm',
                                                       'x_raw',  'y_raw', 'z_raw'])
                                df = df.append(s, ignore_index=True)

#Roundnig to be able to remove duplicates
df['x_norm'] = df['x_norm'].round(10)
df['y_norm'] = df['y_norm'].round(10)
df['z_norm'] = df['z_norm'].round(10)

#calculating components of the burgers vector
df['b_z'] = (np.abs(burgers*np.cos(df['angle']))).round(10)
df['b_x'] = (np.abs(burgers*np.sin(df['angle']))).round(10)

#converting angle to  degrees
df['angle'] = (df['angle']*180/np.pi).round(10)

#Sorting and removing duplicates and angle > than 90
df.sort_values(by = ['angle'], inplace = True, ignore_index = True)
df.drop_duplicates(inplace=True, subset = ['angle'] )
df = df[df['angle']<91]


print(df[['angle', 'x', 'y', 'z', 'b_x', 'b_z']])



