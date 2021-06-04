# @author Gurpreet Kaur
#import modules
import log
from timeit import timeit
from Train.Routes import routes

graph = {'A': {'B': 5, 'D': 5, 'E': 7},
            'B': {'C': 4},
            'C': {'D': 8, 'E': 2},
            'D': {'C': 8, 'E': 6},
            'E': {'B': 3}}

# Inherit routes class
class Particular(routes):
    # function to find particular path i.e specific route
    def particular_paths(self,start, end, route):
        if not isinstance(route, list):
            error = f"Particular paths needs route as type list: provided {type(route)}"
            log.logging.error(error)
        try:
            paths = self.find_all_paths(graph, start, end)
            if route in paths:
                t = sum(graph[i][j] for i, j in zip(route, route[1::]))
                print('\t\tRoute:', route, "Distance", t)
                return route
            else:
                print("\t\tNo route")
        except:
            print("Exception Occurred")


    # function to find shortest distance
    def min_path(self,start, end):
        if end not in graph:
            warn = 'Invalid end point'
            log.logging.warning(warn)
        try:
            paths = self.find_all_paths(graph, start, end)
            x = []  # append distance
            mpath = []  # compared path stored
            for path in paths:
                t = sum(graph[i][j] for i, j in zip(path, path[1::]))
                x.append(t)
                if t == min(x):  # compare distances
                    mpath = path
            shortestRoute = ' '.join('{}->{}:{}'.format(i, j, graph[i][j]) for i, j in zip(mpath, mpath[1::]))
            if shortestRoute:
                info = f"Shortest Route is {shortestRoute}"
                log.logging.info(info)
            minimumDistance = str(sum(graph[i][j] for i, j in zip(mpath, mpath[1::])))
            print('Shortest Route: ' + shortestRoute + '   Distance: ' + minimumDistance + '\n')
            return shortestRoute
        except:
            print("No shortest route found")

# Main function
if __name__ == "__main__":

    # Test Cases
    print("-------------------------------------------Group A --------------------------------------")
    print("1. Distance from Route A-C")
    timing = timeit(lambda: Particular(1,graph).particular_paths('A', 'C', ['A','B','C']), number=1)
    print(f"timing = {timing:.8f}")
    log_time = f"Time for path ['A','B','C'] is: {timing}"
    log.logging.info(log_time)

    print("2. Distance from Route A-D")
    Particular(2,graph).particular_paths('A','D',['A','D'])

    print("3. Distance from route A-D-C")
    Particular(3,graph).particular_paths('A','C',['A','D','C'])

    print("4. Distance from route A-E-B-C-D")
    timing1 = timeit(lambda: Particular(4,graph).particular_paths('A','D',['A','E','B','C','D']), number = 1)
    print(f"timing = {timing1:.7f}")
    print("5. Distance from route A-E-D")
    Particular(5,graph).particular_paths('A','D',['A','E','D'])

    # shortest route test case
    print("-------------------------------------------Group B--------------------------------------")
    print("The length of the shortest route (in terms of distance to travel) from A to C")
    print(Particular(6, graph).min_path('A', 'D'))
    short_timing = timeit(lambda: Particular(3, graph).min_path('A', 'C'), number=1)
    log_short_time = f"Time for short path is: {short_timing}"
    log.logging.info(log_short_time)


    # Test Cases for log(info, error, warning)
    # Particular(7, graph).particular_paths('A', 'D', ('A', 'D'))
    # Particular(8, graph).min_path('A', 'd')
