from fixture import get_testcase
import heapq


class MediansCalculator:
    """ Class for calculating the running median of a list using heaps
    """

    def __init__(self):
        self.lower_heap = []
        self.higher_heap = []

    def __push(self, num):
        if (not self.lower_heap) or (-num > self.lower_heap[0]):
            heapq.heappush(self.lower_heap, -num)
        else:
            heapq.heappush(self.higher_heap, num)

    def __get_biggest_and_smallest_heap(self):
        return (self.lower_heap, self.higher_heap) if (len(self.lower_heap) > len(self.higher_heap)) else (self.higher_heap, self.lower_heap)

    def __rebalance(self):
        """Check the two heaps, one must not be more than 2 elements bigger
            than the other. Take out from one and push it into the other if it is.
        """
        if abs(len(self.lower_heap) - len(self.higher_heap)) >= 2:
            bigger, smaller = self.__get_biggest_and_smallest_heap()
            heapq.heappush(smaller, -heapq.heappop(bigger))

    def __get_median(self):
        bigger, smaller = self.__get_biggest_and_smallest_heap()
        if len(bigger) > len(smaller):
            return abs(bigger[0])
        else:
            return float(abs(bigger[0]) + abs(smaller[0])) / 2

    def get_medians(self, a):
        for num in a:
            self.__push(num)
            self.__rebalance()
            print("{0:0.1f}".format(self.__get_median()))


def main():
    for t in ['00']:
        i, o = get_testcase(t, folder_name='testcases/running_median')
        m = MediansCalculator()
        m.get_medians(list(map(int,i[1:])))


if __name__ == '__main__':
    main()