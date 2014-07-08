import collections


movie_genreinfo={}
def read_genreFile(): 
    with open('genre.data') as genredetails:
        
        for line in genredetails:
            line=line.rstrip('\n')
            temp=line.split('|')
            movie_genreinfo[temp[0]]=temp[1]
            
read_genreFile()

def read_movieDataFile():
        file_object = open('movie.data', 'r')
        movie_data = {}
        for line in file_object:
            movie_temp = {}
            #genreList =[]
            words = line.split("|")
            movie_temp={"movieId":words[0],
                       "movieName":words[1],
                       "releaseYear":words[2],
                       "url":words[4],
                       "rating":''
                       }
            movie_data[words[0]]=movie_temp
        file_object.close()
        return movie_data
   
                
                  
            
        
  
def read_movieRating():
    userlist=[]
    movielist=[]
    with open('ratings.data') as ratingdetails:
        for line in ratingdetails:
            
            line=line.rstrip('\n')
            line=line.replace('\t', ' ')
            temp=line.split(' ')
            userlist.append(temp[0])
            movielist.append(temp[1])
          
        movie_data1=read_movieDataFile()
        max=collections.Counter(userlist).most_common()[0]
        print 'most active user' ,max[0] 
        maxratedmovie=collections.Counter(movielist).most_common()[0]
        maxratedmovie1=maxratedmovie[0]
        print 'most rated movie'
        print movie_data1.get(maxratedmovie1).get('movieName')
        
                          
read_movieRating();     
    
    

        
        
          
        
       
        
        
        