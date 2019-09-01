def querytime(self, query, open_hours):
        if len(open_hours) == 0:
            return 0.0
        res = 0.0
        avahour = query[1] - query[0]
        for oph in open_hours:
            if min(oph[1], query[1]) - max(oph[0], query[0]) > 0:
                res += (min(oph[1], query[1]) - max(oph[0], query[0])) / avahour

        return res
