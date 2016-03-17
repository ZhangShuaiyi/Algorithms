from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0,
                            'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5,
                                'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5,
                                'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0,
                            'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0,
                             'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0,
                             'Superman Returns': 5.0,
                             'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
                    'Superman Returns': 4.0}
           }


# 返回一个有关person1和person2的基于欧氏距离的相似度评价
def sim_euclidean_distance(prefs, person1, person2):
    si = [item for item in prefs[person1] if item in prefs[person2]]
    # 如果没有相同之处，则返回0
    if len(si) == 0:
        return 0

    # 计算所有差值的平方和
    sum_of_squares = sum(pow(prefs[person1][item] - prefs[person2][item],
                             2) for item in si)
    return 1 / (1 + sqrt(sum_of_squares))


def sim_distance2(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],
                              2) for item in prefs[person1] if item in
                          prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))


# 皮尔森相关系数
# 结果的取值区间为[-1，1]，-1表示完全的负相关(这个变量下降，那个就会上升)，+1表示完全的正相关，0表示没有线性相关
def sim_pearson_correlation_score(prefs, p1, p2):
    si = [item for item in prefs[p1] if item in prefs[p2]]
    n = len(si)
    
    # 如果没有共同之处返回0
    if n == 0:
        return 0

    # 对所有偏好求和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 求平方和
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # 求乘积之和
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 计算皮尔逊相关系数
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0

    r = num / den
    return r


if __name__ == '__main__':
    ret = sim_euclidean_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print("Euclidean Distance: %.20f" % (ret))
    ret = sim_pearson_correlation_score(critics, 'Lisa Rose', 'Gene Seymour')
    print("Pearson Correlation Score: %.20f" % (ret))
