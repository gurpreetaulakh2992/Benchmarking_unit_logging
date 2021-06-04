#import Train class from TrainClass module
from Train.TrainClass import Train
# inherit properties from Train class i.e parent class
class routes(Train):
      # find all possible paths
      def find_all_paths(self, graph, start, end, path=[]):
        try:
            path = path + [start]
            if start == end:
                return [path]
            if start not in self.graph:
                return []
            paths = []
            for node in graph[start]:
                if node not in path:
                    newpaths = self.find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths
        except:
            print("Exception Occured")
