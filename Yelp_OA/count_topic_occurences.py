def count_topic_occurences(s, map):
    finans = collections.defaultdict(int)
    for ele in s:
        a = ele.lower()
        single_res = helper(map, a)
        print('single_res',single_res)
        for key in single_res.keys():
            finans[key] = finans.get(key, 0) + single_res[key]
    finans = sorted(finans.items(), key=lambda x: x[1], reverse = True)
    return dict(finans)

def helper(map, a):
    res = collections.defaultdict(int)
    for vallist in map.values():
        for val in vallist:
            if val in a:
                for key, value in map.items():
                        if val in value:
                            res[key] += 1
                        if res[key] >= 1:
                            res[key] = 1
    return res
