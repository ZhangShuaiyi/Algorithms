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
    # return 1 / (1 + sum_of_squares)
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


def topMatches(prefs, person, n=5, similarity=sim_pearson_correlation_score):
    """
    从反应偏好的字典中返回最为匹配者
    返回结果的个数和相似度函数为可选参数
    """
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    # 对列表进行排序，评价高者排在最前面
    scores.sort(reverse=True)
    return scores[:n]


def getRecommendations(prefs, person,
                       similarity=sim_pearson_correlation_score):
    """
    根据用户相似度计算和影片评分，预测用户还未看过的电影的评分，进行影片推荐
    """
    totals = {}
    simSums = {}
    for other in prefs:
        # 不比较自己
        if other == person:
            continue
        # 计算相关性
        sim = similarity(prefs, person, other)

        # 忽略相关性小于等于0的用户
        if sim <= 0:
            continue

        for item in prefs[other]:
            # 只对自己还未看过的影片进行评价
            if item not in prefs[person] or prefs[person][item] == 0:
                # 评分*相似度之和
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # 相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # 建立一个归一化列表
    rankings = [(total / simSums[item], item)
                for item, total in totals.items()]
    rankings.sort(reverse=True)
    return rankings


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # 将人员和物品对调
            result[item][person] = prefs[person][item]
    return result


def calculateSimilarItems(prefs, n=10):
    # 建立字典，列出物品最为接近的其它物品及相似度
    result = {}

    itemPrefs = transformPrefs(prefs)
    for item in itemPrefs:
        # 列出最接近的n个物品
        scores = topMatches(
            itemPrefs, item, n=n, similarity=sim_euclidean_distance)
        result[item] = scores
    return result


def getRecommendedItems(prefs, itemMatch, user):
    # 用户已经评过分的商品
    userRatings = prefs[user]
    scores = {}
    totalSim = {}

    # 遍历用户已评分商品
    for (item, rating) in userRatings.items():

        # 遍历当前商品向近的商品
        for (similarity, item2) in itemMatch[item]:
            # 如果用户已对商品做过评价，则忽略
            if item2 in userRatings:
                continue

            # 评分与相似度的加权和
            scores.setdefault(item2, 0)
            scores[item2] += rating * similarity

            # 相似度之和
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity

    # 将加权和除以相似度之和得到平均值
    rankings = [(score / totalSim[item], item)
                for item, score in scores.items()]

    rankings.sort(reverse=True)
    return rankings


if __name__ == '__main__':
    ret = sim_euclidean_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print("Euclidean Distance: %.20f" % (ret))
    ret = sim_pearson_correlation_score(critics, 'Lisa Rose', 'Gene Seymour')
    print("Pearson Correlation Score: %.20f" % (ret))
    print("match Toby top 3:")
    print(topMatches(critics, 'Toby', n=3))
    rankings = getRecommendations(critics, 'Toby')
    print("getRecommendations for Toby:")
    print(rankings)
    rankings = getRecommendations(critics, 'Toby', sim_euclidean_distance)
    print("getRecommendations by sim_euclidean_distance for Toby:")
    print(rankings)

    movies = transformPrefs(critics)
    movie = 'Superman Returns'
    ret = topMatches(movies, movie)
    print("match " + movie + " top:")
    print(ret)

    movie = 'Just My Luck'
    ret = getRecommendations(movies, movie)
    print('getRecommendations for ' + movie + ':')
    print(ret)

    itemsim = calculateSimilarItems(critics)
    # print(itemsim)
    user = 'Toby'
    ret = getRecommendedItems(critics, itemsim, user)
    print('getRecommendedItems for ' + user + ':')
    print(ret)
