from geo_space.oo_training import Point
# import oo_training as oo

def main():
    'This is the main method'
    a = Point()
    a.point_position()
    a.move(5, 2)
    a.point_position()
    a.reset()
    a.point_position()

if __name__ == '__main__': main()