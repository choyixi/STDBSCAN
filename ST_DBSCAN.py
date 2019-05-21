from vincenty import vincenty
import numpy as np

class stdbscan:
    def __int__(self, hour, lat, lng, value=None, hourdelta=3, spatialdelta=5, minpts=10, threshold=4):
        """
        Python st-dbscan hourly trend implementation.
        :param hour: hour column name;
        :param lat: Latitude column name;
        :param lng: Longitude column name;
        :param value: non-spatial and non-temporal value column name;
        
        :param hourdelta: Maximum non-spatial distance value (hour);
        :param spatialdelta: Maximum geographical coordinate (spatial) distance value (km);

        :param minpts: Minimum number of points within Eps1 and Eps2
             distance;
        :param threshold: threshold value to be included in a cluster
        """

        
        self.hour = hour
        self.lat = lat
        self.lng = lng
        self.value = value
        self.hourdelta = hourdelta
        self.spatialdelta = spatialdelta
        self.minpts = minpts
        self.threshold = threshold
    
    # return the list of index values contained that are the neighbours of the starting object 
    def find_neighbours(self, index, matrix):
        
        starting_obj = matrix[index,:]  
        # filter by hour
        if starting_obj[0]-self.hourdelta<0:
            min_hour = 24-self.hourdelta
        else:
            min_hour = starting_obj[0]-self.hourdelta
            
        if starting_obj[0]+self.hourdelta>=24:
            max_hour = starting_obj[0]+self.hourdelta-24
        else:
            max_hour = starting_obj[0]+self.hourdelta
            
        if min_hour<=max_hour:
            matrix = matrix[(matrix[:,0]>= min_hour) & 
                            (matrix[:,0]<=max_hour),:]
        else:
            matrix = matrix[(matrix[:,0]>= min_hour) | 
                            (matrix[:,0]<=max_hour),:]    
        # filter by distance
        def calc_dist(i):
            return vincenty(i[1:3],starting_obj[1:3])
        temp = np.apply_along_axis(calc_dist, axis=1, arr=matrix)
        #get the IDs of the neighbour objects
        neighbourhood = matrix[temp<=self.spatialdelta,4].tolist()    
        neighbourhood.remove(index)
        return neighbourhood
    
    def run(self,data):
        # set predefined variables
        unmarked = 888
        noise = -1
        stack = []
        cluster_label = 0
        
        #data = pd.read_csv("test.csv")
        
        df = data[[self.hour,self.lat,self.lng]]
        # check if there is a non-spatial, non-temporal value column in the data. 
        # if not, assign it to 0
        if self.value is not None:
            df['Value'] = data['Value']
        else:
            df = df.assign(Value = 0)
        # append the index value to the matrix
        df['index'] = range(df.shape[0])
        # initialize all objects as unmarked cluster
        df = df.assign(cluster=unmarked)
        matrix = df.values
        df.drop(['index'],inplace=True, axis=1)
        
        for index in range(matrix.shape[0]):
            neighbours = self.find_neighbours(index,matrix)
            if len(neighbours)<self.minpts:
                #if the number of neighbours do not satify the condition forming a cluster
                matrix[index, 5] = noise
            else:
                #found a core object
                cluster_label += 1
                matrix[index, 5] = cluster_label
                
                #assign this cluster label to all of its neighbours
                for neighbour in neighbours:
                    matrix[neighbour, 5] = cluster_label 
                    stack.append(neighbour)
                    
                #find additional neighbours of this clustered neighbourhood
                while len(stack)>0:
                    current_point = stack.pop()
                    new_neighbours = self.find_neighbours(current_point,matrix)
                    cluster = matrix[matrix[:,5]==cluster_label,:]
                    cluster_avg = cluster[:,3].nanmean()
                    if len(new_neighbours)>=self.minpts:
                        for new_neighbour in new_neighbours:
                            if matrix[new_neighbour,5]!=unmarked \
                            and matrix[new_neighbour,5]!=noise \
                            and abs(matrix[new_neighbour,3]-cluster_avg)<=self.threshold:
                                matrix[new_neighbour,5] = cluster_label
                                stack.append(new_neighbour)
        df['cluster']=matrix[:,5]
                        
                        
    
    
    
    
    
    
    