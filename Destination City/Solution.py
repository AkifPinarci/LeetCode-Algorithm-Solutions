class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        # Implemented by using the dict structure

        hasht = dict()
        for i in range(len(paths)):
            hasht[paths[i][0]] = paths[i][1]

        start = paths[0][0]
        while start in hasht:
            start = hasht[start]

        return start

        # Implemented by using arrays

        # dests = list()
        # for i in range(len(paths)):
        #     dests.append(paths[i][0])
            
        # for i in range(len(paths)):
        #     if paths[i][1] not in dests:
        #         return paths[i][1]


        # The fastest solution in the internet.

        # cities = {city1: city2 for city1, city2 in paths}
        # s1, s2 = set(cities.keys()), set(cities.values())
        # return list(s2.difference(s1))[0]