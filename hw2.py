import data2

# Write your functions for each part in the space below.

# Part 1
# takes two points and makes sure they are top_left and bottom_right(first point(PointA) is top_left and second point(PointB) is bottom_right
#rectangle returned because top_left and bottom_right make a rectangle; rectangle is made up of 2 points
# the code checks for every scenario and returns the points in a top_left and bottom_right position, returning the same points if already in the correct position
def create_rectangle(PointA:data2.Point, PointB:data2.Point) -> data2.Rectangle:

    Point1 = data2.Point(0, 0)
    Point2 = data2.Point(0, 0)
    if PointA.x < PointB.x:

        if PointA.y < PointB.y:
            Point1.y = PointB.y
            Point1.x = PointA.x
            Point2.y = PointA.y
            Point2.x = PointB.x
        else:
            Point1 = PointA
            Point2 = PointB
    else:
        if PointA.y < PointB.y:
            Point1.y = PointB.y
            Point1.x = PointB.x
            Point2.y = PointA.y
            Point2.x = PointA.x
        else:
            Point1 = PointA
            Point2 = PointB

    rectangle = data2.Rectangle(Point1, Point2)
    return rectangle



# Part 2
# takes two data points of data2. Duration, consisting of (minutes, seconds), returning True if the first point is less than the second point and false if not
#The minutes are turned into seconds by multiplying by 60, putting it in the same units to make combining seconds and minutes easier and accurate
def shorter_duration_than(D1:data2.Duration, D2:data2.Duration) -> bool:
    d1minutes = D1.minutes * 60
    d2minutes = D2.minutes * 60

    if d1minutes + D1.seconds < d2minutes + D2.seconds:

        return True

    else:

        return False

# Part 3
#This function uses a list of songs and returns the songs that have a duration  less than the upperbound limit(3 minutes, 30 seconds in this case)
#The minutes are turned into seconds by multiplying by 60, putting it in the same units to make combining seconds and minutes easier and accurate
def song_shorter_than(Songs:list[data2.Song], uppbound:data2.Duration) -> list[data2.Song]:
    up = uppbound.minutes * 60 + uppbound.seconds
    out = []
    for song in Songs:
        dur = song.duration.minutes * 60 + song.duration.seconds

        if dur < up:
            out.append(song)
            #print(song)
    return out


# Part 4
#This function uses a playlist to add up the time of the songs from a list based on the order that the songs are in the playlist
#If the seconds  goes over 60, it will add 1 to the minute and be reduced from the seconds
def running_time(TheSongs:list[data2.Song], playlist:list[int]) -> data2.Duration:
    sum = 0
    sum1 = 0
    k = len(playlist)
    for j in range(0, (k)):
        l = playlist[j]
        song = TheSongs[l]
        sum += song.duration.minutes
        sum1 += song.duration.seconds
        if sum1 > 60:
            sum += 1
            sum1 -= 60
    return [sum, sum1]



# Part 5
#This function returns true if the citylink is true(in order based on route) based on the order of the city names
def validate_route(citylinks:list[list[str]], cityname:list[str]) -> bool:

    k = len(cityname)
    c = 0
    for i in range(0, k-1):
        if (cityname[i] == citylinks[i][0] or cityname[i] == citylinks[i][1]) and (cityname[i+1] == citylinks[i][0] or cityname[i+1] == citylinks[i][1]):
            c +=1
    if c == k-1:
        return True
    else:
        return False



# Part 6
#uses index, count and maxStreak to find index with the longest streak(returns first index of longest streak)

def longest_repetition(list1:list[int]) -> int:
    index = -1
    count = 0
    maxStreak = 0
    indexAtMaxStreak = 0
    for i in range(0,len(list1)-1):
        # if there is a repetition update count
        if list1[i] == list1[i+1]:
            count += 1
            # update max if the count is greater
            if index == -1:
                index = i
            if count > maxStreak:
                maxStreak = count
                indexAtMaxStreak = index
        else:
            # if there isn't a repetition, we will reset count
            index = -1
            count = 0
    return indexAtMaxStreak
