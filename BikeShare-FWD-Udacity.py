import time
import pandas as pd
import numpy as np
import datetime

City_Data = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months_Data ={"all":0,"january":1,"febrary":2,"march":3,"april":4,"may":5,"june":6}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in City_Data.keys():
       print("Please enter the name of the city:")
       city = input().lower().strip()

       if (city not in City_Data.keys()):
        print("This is a wrong city not included within bikeshare sheet.")
        print("Please enter one of those cities: Chicago, New York, Washington.")

    print("You Selected: "+city+" City")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in Months_Data.keys():
        print("Please note that you can enter a valid month from January till June or All")
        month = input().lower().strip()
        if (month not in Months_Data.keys()):
            print("This is not a valid month")

    print("You Selected: "+month)

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Days_Data={"all":"all","saturday":"sat.","sunday":"sun.","monday":"mon.","tuesday":"tues.","wednesday":"wed.","thursday":"thu.","friday":"fri."}

    day= ""
    while day not in Days_Data.keys():
        print("Please enter a valid day as Saturday, Sunday,...etc or All")
        day=input().lower().strip()
        if (day not in Days_Data.keys()):
            print("This is not a valid day name")
    print ("You Selected: "+day)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
  """

    #load data file into data frame
    df= pd.read_csv(City_Data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = Months_Data[month]
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["Common Trip"]= df["Start Station"]+" to "+ df["End Station"]

    common_trip = df["Common Trip"].mode()[0]

    print("Most common trip is: ", common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=df['Trip Duration'].sum()
    #print('The total travel time of all trips: ', str(datetime.timedelta(seconds=total_trip_duration)))

    minutes, sec = divmod(total_trip_duration,60)
    hours, minutes = divmod(minutes,60)
    print('The total travel time of all trips: ',hours,'hrs and ',minutes,'mins.')

    # TO DO: display mean travel time
    average_trip_duration=df['Trip Duration'].mean()
    print('The average of the trip duration is: ',str(datetime.timedelta(seconds=average_trip_duration)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    total_user_type=df['User Type'].value_counts()
    print(f"The total user types are:\n{total_user_type}")

    # TO DO: Display counts of gender
    if (city != 'washington'):
        total_gender=df['Gender'].value_counts()
        print(f'\n\nThe total number of gender as follows:\n{total_gender}')
        # TO DO: Display earliest, most recent, and most common year of birth
        common_year=int(df['Birth Year'].mode()[0])
        print("\n\nThe most common year is: ",common_year)
        earliest_year=int(df['Birth Year'].min())
        print('The earliest year is: ',earliest_year)
        recent_year=int(df['Birth Year'].max())
        print('The recent year is: ',recent_year)
    else:
        print('This data is not available for Washington City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """display the option of viewing 5 rows of raw data"""


    answers=["yes","no"]
    result=""
    counter=0

    while result not in answers:
        print("Do you want to view 5 rows of the raw data?\nPlease type yes or no")
        result=input().lower().strip()

        if result=="yes":
            print(df.head())
        elif result not in answers:
            print("Please choose one of the answers yes or no")

    while result == 'yes':
        print("Do you want to view 5 more rows of raw data?\nPlease type yes or no.")
        result=input().lower().strip()

        if result =="yes":
            counter+=5
            print(df[counter:counter+5])

        elif result=="no":
            break
        else:
            print("Incorrect input please type yes or no")
            result="yes"



def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
