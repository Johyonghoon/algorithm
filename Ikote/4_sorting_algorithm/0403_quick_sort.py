from utils import my_menu


class QuickSort:

    def __init__(self):
        global array
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort_og(self, array, start, end):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while(left <= right):
            while(left <= end and array[left] <= array[pivot]):
                left += 1
            while(right > start and array[right] >= array[pivot]):
                right -= 1
            if(left > right):
                array[right], array[pivot] = array[pivot], array[right]
            else:
                array[left], array[right] = array[right], array[left]
        self.quick_sort_og(array, start, right - 1)
        self.quick_sort_og(array, right + 1, end)

    def solution_og(self):
        self.quick_sort_og(array, 0, len(array) - 1)
        print(array)

    def quick_sort_pythonic(self, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        tail = array[1:]

        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]

        return self.quick_sort_pythonic(left_side) + [pivot] + self.quick_sort_pythonic(right_side)

    def solution_pythonic(self):
        print(self.quick_sort_pythonic(array))


MENUS = ["종료",  # 0
         "퀵정렬 기본",  # 1
         "퀵정렬 파이써닉",  # 2
         ]

menu_options = {"1": lambda x: x.solution_og(),
                "2": lambda x: x.solution_pythonic(),
                }

if __name__ == '__main__':
    qs = QuickSort()
    while True:
        menu = my_menu(MENUS)
        if menu == "0":
            print("종료")
            break
        else:
            menu_options[menu](qs)
