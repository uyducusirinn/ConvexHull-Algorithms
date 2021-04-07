# coding=utf-8
import random
import matplotlib.pyplot as plt
import time

# Starting time function
start_time = time.time()


# Firstly, I defined point class
class point:
    def __init__(self, x, y):  # initializer method
        self.x = x
        self.y = y

    def get_points(self):
        return self.x, self.y


class line_vector:
    def __init__(self, p1, p2):  # initializer method, p1 and p2 are our attributes
        self.p1 = p1
        self.p2 = p2

    def point_on_where(self, px):  # important method b
        # this method will identify whether the point x (px) is
        # on the left, right of the line or colinear.

        x, y = px.get_points()
        x1, y1 = self.p1.get_points()
        x2, y2 = self.p2.get_points()

        rate = (x1 - x2) * (y - y2) - (y1 - y2) * (x - x2)

        if rate > 0:
            return 1
        elif rate < 0:
            return -1
        else:
            return 0


# Firstly, I define function for random points
def random_points(n):
    point_list = []
    for _ in range(n):
        x, y = random.randint(0, 100), random.randint(0, 100)  # points defined at 0 -100
        point_list.append(point(x, y))
    return point_list


def leftmost_point(set_of_points):  # ı tried to identifies the lest most point in the
    # given set of points.
    pointleft = set_of_points[0]
    xLeft, yLeft = 200, 200

    for p in set_of_points:
        x, y = p.get_points()
        if x < xLeft:
            xLeft, yLeft = pointleft.x, pointleft.y
            pointleft = p

    return pointleft


def display_points(set_of_points):
    # ı defined displays the points this function show points in figure
    xcor = [p.x for p in set_of_points]
    ycor = [p.y for p in set_of_points]
    plt.scatter(xcor, ycor)
    plt.show()


def distance_between_two_points(p1, p2):
    # This function returns
    # the distance between two points
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** (1 / 2)
    # Obviously, I used this link to create this formula.
    # https://stackoverflow.com/questions/21369449/how-to-calculate-the-distance-between-two-points-using-return-methods-in-python


def jarvis_march(set_of_points):
    # This function identifies the
    # convex hull on the given set of points. Returns border_points.

    convex_hull = []

    convexpoint = leftmost_point(set_of_points)
    i = 0
    while True:
        convex_hull.append(convexpoint)
        end_point = set_of_points[0]
        for j in range(len(set_of_points)):
            l = line_vector(convex_hull[i], end_point)
            if (end_point == convexpoint) or (l.point_on_where(set_of_points[j]) < 0):
                end_point = set_of_points[j]
        i += 1
        convexpoint = end_point
        if end_point.get_points() == convex_hull[0].get_points():
            break

    convex_hull.append(leftmost_point(set_of_points))

    return convex_hull


def display_envelope(border_points, set_of_points):
    Set_x = [p.x for p in set_of_points]
    Set_y = [p.y for p in set_of_points]
    Border_x = [p.x for p in border_points]
    Border_y = [p.y for p in border_points]

    plt.scatter(Set_x, Set_y)
    plt.plot(Border_x, Border_y, "g")
    plt.show()


point_list = random_points(50)
display_points(point_list)
convex_hull = jarvis_march(point_list)
display_envelope(convex_hull, point_list)


#I used this part to find out how long my code worked and output it.
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
end_time = time.time()
print("seconds=", end_time - start_time)
