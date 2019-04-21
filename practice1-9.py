# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:34:31 2019

@author: YJH
"""
from collections import Counter

x = [
    {"name": "电影1", "director": "导演1", "actor": ["演员1", "演员2", "演员3", "演员4"]},
    {"name": "电影2", "director": "导演2", "actor": ["演员3", "演员2", "演员4", "演员5"]},
    {"name": "电影3", "director": "导演3", "actor": ["演员1", "演员5", "演员3", "演员6"]},
    {"name": "电影4", "director": "导演1", "actor": ["演员1", "演员4", "演员3", "演员7"]},
    {"name": "电影5", "director": "导演2", "actor": ["演员1", "演员2", "演员3", "演员8"]},
    {"name": "电影6", "director": "导演3", "actor": ["演员5", "演员7", "演员3", "演员9"]},
    {"name": "电影7", "director": "导演4", "actor": ["演员1", "演员4", "演员6", "演员7"]},
    {"name": "电影8", "director": "导演1", "actor": ["演员1", "演员4", "演员3", "演员8"]},
    {"name": "电影9", "director": "导演2", "actor": ["演员5", "演员4", "演员3", "演员9"]},
    {"name": "电影10", "director": "导演3", "actor": ["演员1", "演员4", "演员5", "演员10"]},
    {"name": "电影11", "director": "导演1", "actor": ["演员1", "演员4", "演员3", "演员11"]},
    {"name": "电影12", "director": "导演2", "actor": ["演员7", "演员4", "演员9", "演员12"]},
    {"name": "电影13", "director": "导演3", "actor": ["演员1", "演员7", "演员3", "演员13"]},
    {"name": "电影14", "director": "导演4", "actor": ["演员10", "演员4", "演员9", "演员14"]},
    {"name": "电影15", "director": "导演5", "actor": ["演员1", "演员8", "演员11", "演员15"]},
    {"name": "电影16", "director": "导演6", "actor": ["演员14", "演员4", "演员13", "演员16"]}
]


#处理演员数据
def deal_data(actors):
    z = []
    for i in actors:
        z.extend(i["actor"])
    k = []
    for item in set(z):
        tmp = []
        tmp.append(item)
        _t = []
        for i in actors:
            if item in i["actor"]:
                _t.append(i["name"])
        tmp.append(set(_t))
        k.append(tuple(tmp))

    return k

#两个演员共同参演的电影
def getActorPair(actors):
    result = []

    for index, actor1 in enumerate(actors[:-1]):
        for _, actor2 in enumerate(actors[index + 1:]):
            actorPair = (actor1[0], actor2[0])
            films = actor1[1] & actor2[1]
            result.append((actorPair, films))

    return result

#参演的作品最多演员
def part2(actors):
    director_list = []
    for i in actors:
        director_list.extend(i["actor"])

    z = Counter(director_list)

    print("2", z.most_common(1))


#创作的电影最多导演
def part1(actors):
    director_list = []
    for i in actors:
        director_list.append(i["director"])

    z = Counter(director_list)

    print("1", z.most_common(1))


if __name__ == "__main__":
    part1(x)
    part2(x)

    actors = deal_data(x)
    actorPairs = getActorPair(actors)
    closestPair = max(actorPairs, key=lambda item: len(item[1]))

    print("3", closestPair)

