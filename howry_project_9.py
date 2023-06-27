"""
Creating a Clickable Map

This program reads a file containing CO elevations 
and creates a gray-scale map according to the elevation level.
When clicked, the elevation is printed at the bottom-left.

File Name: howry_project_9.py
Author: Ken Howry
Date: 22.11.18
Course: COMP 1351
Assignment: Project IV
Collaborators: N/A
Internet Source: N/A
"""

#creating a list
elevations = []

#reading the elevations file and making a matrix
with open("CO_elevations_feet.txt", "r") as a_file:
    for line in a_file:
        elevations.insert(0, line.strip().split(" "))

#function to find the max value in the matrix
def max_elevation(a: list) -> int:
    """
    Description of function: Iterates through a 2D list and prints the largest integer
    Parameters: 
        a: 2D list
    Return: int
    """
    max_value = 0

    for i in range(len(a)):
        for j in range (len(a[i])):
            a[i][j] = int(a[i][j])
        for element in a[i]:
            if element > max_value:
                max_value = element
    return max_value

#printing the max_value to the terminal
print(max_elevation(elevations))

#variable storing the max value
max = max_elevation(elevations)

#creating canvas
import dudraw
dudraw.set_canvas_size(760, 560)
dudraw.set_x_scale(0,760)
dudraw.set_y_scale(0,560)
dudraw.clear(dudraw.BLACK)

#function to draw the map using the elevations
def map() -> None:
    """
    Description of Function: Draws a gray-scale map
    Parameters: None
    Return: None
    """
    #variables
    x_Coor = 0
    y_Coor = 0
    #map creation
    for i in range(len(elevations)):
        for j in range(len(elevations[i])):
            #changing the color based off elevation
            color=int(255*(elevations[i][j])/max)
            dudraw.set_pen_color_rgb(color, color, color)
            #drawing each square in the row
            dudraw.filled_square(x_Coor, y_Coor, 1)
            x_Coor += 1
        #moving up a row and resetting x_Coor
        y_Coor += 1
        x_Coor = 0

#variables
key = " "
run_Once = False

while key == " ":
    #drawing the map once
    if run_Once == False:
        map()
        run_Once = True

    #if mouse pressed, print the elevation in the bottom left
    if dudraw.mouse_pressed():
        x_position = int(dudraw.mouse_x())
        y_position = int(dudraw.mouse_y())
        
        #finding the elevation in the matrix
        clicked_elevation = elevations[y_position][x_position]

        #printing the elevation
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.filled_rectangle(50,15,50,15)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(50,10,(f"Elevation: {clicked_elevation}"))

    #closing the program if any key is pressed
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    dudraw.show(30)