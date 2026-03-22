class Point:
    """
    A class representing a point on a plane.

    Attributes:
        x (int/float): The x-coordinate of the point.
        y (int/float): The y-coordinate of the point.
    """
    
    def __init__(self, coordinates=(0, 0)):
        """
        Initialize a new Point object.

        Args:
            coordinates (tuple, optional): A tuple (x, y) containing the coordinates.
        """
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def get_x(self):
        """Return the x-coordinate of the point."""
        return self.x
    
    def get_y(self):
        """Return the y-coordinate of the point."""
        return self.y
    
    def distance(self, other):
        """
        Calculate the Euclidean distance between this point and another point.
        
        Args:
            other (Point): Another Point object to calculate distance to.
        
        Returns:
            float: The Euclidean distance between the two points.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx**2 + dy**2) ** 0.5
        return distance
    
    def sum(self, other):
        """
        Create a new point that is the sum of this point and another point.
        
        Args:
            other (Point): Another Point object to add to this point.
        
        Returns:
            Point: A new Point object with coordinates equal to the sum.
        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point((new_x, new_y))
    
    def __str__(self):
        """Return a string representation of the Point object."""
        return "({}; {})".format(self.x, self.y)
    
    def __repr__(self):
        """Return a string representation for debugging."""
        return "({}; {})".format(self.x, self.y)


class Segment:
    """
    A class representing a line segment on a plane.

    Attributes:
        point1 (Point): The first endpoint of the segment.
        point2 (Point): The second endpoint of the segment.
        one_intersection (bool): Indicates if the segment intersects exactly one axis.
    """
    
    def __init__(self, point1, point2):
        """
        Initialize a new Segment object.
       
        Args:
            point1 (Point): The first endpoint of the segment.
            point2 (Point): The second endpoint of the segment.
        """
        self.point1 = point1
        self.point2 = point2
       
        self.one_intersection = self._check_one_intersection()
    
    def _check_one_intersection(self):
        """
        Check if the segment intersects exactly one coordinate axis.
      
        Returns:
            bool: True if the segment intersects exactly one axis, False otherwise.
        """
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        
        intersects_x = False
        if y1 != y2:
            t = (0 - y1) / (y2 - y1)
            if 0 <= t <= 1:
                intersects_x = True
        
        intersects_y = False
        if x1 != x2:
            t = (0 - x1) / (x2 - x1)
            if 0 <= t <= 1:
                intersects_y = True
        
        return intersects_x != intersects_y  
    
    def __str__(self):
        """
        Return a string representation of the Segment object.
        
        Returns:
            str: A string in the format ((x1; y1), (x2; y2))
        """
        return "({}, {})".format(self.point1, self.point2)


class CoordinateSystem:
    """
    A class representing a coordinate system (plane).

    Attributes:
        segments (list): List of Segment objects on the plane.
    """
    
    def __init__(self):
        """Initialize a new CoordinateSystem object."""
        self.segments = []
    
    def add_segment(self, segment):
        """
        Add a segment to the coordinate system.
        
        Args:
            segment (Segment): The Segment object to add.
        """
        self.segments.append(segment)
    
    def axis_intersection(self):
        """
        Count the number of segments that intersect exactly one coordinate axis.
        
        Returns:
            int: The number of segments intersecting exactly one axis.
        """
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count
    
    def __str__(self):
        """
        Return a string representation of all segments.
        
        Returns:
            str: A string containing all segments in a list format.
        """
        return str(self.segments)

def main():
    """The main function of the program."""
    p1 = Point((-2, 7))
    print(p1)
    p2 = Point((3, 4))
    
    s1 = Segment(p1, p2)
    print(s1)
    print(s1.one_intersection)
    
    xy = CoordinateSystem()
    xy.add_segment(s1)
    
    p3 = Point((2, -8))
    p4 = Point((4, 16))
    s2 = Segment(p3, p4)
    xy.add_segment(s2)
    
    xy.add_segment(Segment(p4, p2))
    xy.add_segment(Segment(Point((-5, 3)), Point((-13, -6))))
    
    print(xy.segments)
    print(xy)
    print(xy.axis_intersection())


if __name__ == "__main__":
    main()
