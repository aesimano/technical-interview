"""
Quick Sort

Pivot - usually the last element in the array is chosen as the first pivot

Efficiency - complicated
    worst case: already sorted O(n^2), or close to being sorted (bad use of quick sort)
    average and best: O(nlogn)
    space complexity is O(1) because it is in-place
"""
import abc

sorted
class BaseQuickSort(object):
    __metaclass__ = abc.ABCMeta

    def quick_sort(self, array):
        if not isinstance(array, list):
            raise TypeError('Must be of type "list", instead {} was passed'.format(type(array)))

        if len(array) > 1:
            self._qsort(array, 0, len(array) - 1)

        return array

    @abc.abstractmethod
    def _qsort(self, array, lo, hi):
        pass

    @abc.abstractmethod
    def _partition(self, array, lo, hi):
        pass

    def _swap(self, array, index_a, index_b):
        if index_a != index_b:
            temp = array[index_a]
            array[index_a] = array[index_b]
            array[index_b] = temp


class HoareQuickSort(BaseQuickSort):
    def _qsort(self, array, lo, hi):
        if lo < hi:
            pivot = self._partition(array, lo, hi)
            self._qsort(array, lo, pivot)
            self._qsort(array, pivot + 1, hi)

    def _partition(self, array, lo, hi):
        pivot = array[lo]
        i = lo - 1
        j = hi + 1

        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1

            if i >= j:
                return j

            self._swap(array, i, j)


class LumotoQuickSort(BaseQuickSort):
    def _qsort(self, array, lo, hi):
        if lo < hi:
            pivot = self._partition(array, lo, hi)
            self._qsort(array, lo, pivot - 1)
            self._qsort(array, pivot + 1, hi)

    def _partition(self, array, lo, hi):
        pivot = array[hi]
        i = lo

        for j in range(lo, hi):
            if array[j] <= pivot:
                self._swap(array, i, j)
                i += 1
        self._swap(array, i, hi)

        return i


class QuickSortType(object):
    HOARE = 'hoare'
    LUMOTO = 'lumoto'


def quick_sort_factory(qs_type):
    qs = None

    if qs_type == QuickSortType.HOARE:
        qs = HoareQuickSort()
    elif qs_type == QuickSortType.LUMOTO:
        qs = LumotoQuickSort()

    return qs.quick_sort


if __name__ == '__main__':
    import time

    quick_sort = quick_sort_factory(QuickSortType.LUMOTO)
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 0, 55, 10, 17, 29, 0]
    start_time = time.time()
    print quick_sort(test)
    print 'elapsed time: {}'.format(time.time() - start_time)

    quick_sort = quick_sort_factory(QuickSortType.HOARE)
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 0, 55, 10, 17, 29, 0]
    start_time = time.time()
    print quick_sort(test)
    print 'elapsed time: {}'.format(time.time() - start_time)
