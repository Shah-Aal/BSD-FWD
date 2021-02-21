# BSD-FWD
Bike Share Data (https://www.motivateco.com)



In this project, i used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. we can now compare the system usage between three large cities: Chicago, New York City, and Washington, DC.


The Datasets Randomly selected data for the first six months of 2017 are provided for all three cities.
All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53) 
Trip Duration (in seconds - e.g., 776) 
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer) 
The Chicago and New York City files also have the following two columns: Gender Birth Year



Data for the first 10 rides in the new_york_city.csv file The original files are much larger and messier.
Some data wrangling has been performed to condense these files to the above core six columns to make the analysis straightforward. 



 In this project, i wrote a  code to provide the following information:



#1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day

 #2 Popular stations and trip
most common start station 
most common end station 
most common trip from start to end (i.e., most frequent combination of start station and end station)

 #3 Trip duration
total travel time average travel time

 #4 User info
counts of each user type counts of each gender (only available for NYC and Chicago) earliest, most recent, most common year of birth (only available for NYC and Chicago) 
Attached the File To answer these questions using Python.
