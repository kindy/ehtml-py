#coding: utf-8

class TplHelper:
    getaid_c = 0

    def getaid(self, prefix='autogenid_'):
        self.getaid_c += 1
        return prefix + str(self.getaid_c)

    def group_(self, iterable, num):
        return map(None, *[iter(iterable)] * num)

    def group(self, iterable, num, predicate=None):
        """Group an iterable into an n-tuples iterable. Incomplete tuples
        are discarded e.g.
        
        >>> list(group(range(10), 3))
        [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, None, None)]
        """
        if predicate is None:
            for item in self.group_(iterable, num):
                yield item
        else:
            buf = []
            for item in iterable:
                flush = predicate and not predicate(item)
                if buf and flush:
                    buf += [None] * (num - len(buf))
                    yield tuple(buf)
                    del buf[:]
                buf.append(item)
                if flush or len(buf) == num:
                    yield tuple(buf)
                    del buf[:]
            if buf:
                buf += [None] * (num - len(buf))
                yield tuple(buf)
    

class DomHelper:
    
    def classes(self, *args, **kwargs):
        classes = list(filter(None, args)) + [k for k, v in kwargs.items() if v]
        if not classes:
            return None
        return u' '.join(classes)
