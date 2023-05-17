from curses.ascii import isdigit


class RangeString:

    def solution(self, input_data):
        ls = list(input_data)
        range_characters = ""
        sum = 0
        for i in ls:
            if isdigit(i):
                sum += int(i)
            elif isdigit(i) is False:
                range_characters += i
        print("".join(sorted(range_characters)) + str(sum))

    def teacher_solution(self, input_data):
        result = []
        value = 0

        for x in input_data:
            if x.isalpha():
                result.append(x)
            else:
                value += int(x)
        result.sort()

        if value != 0:
            result.append(str(value))
        print("".join(result))


if __name__ == '__main__':
    input_data = input("문자열을 입력하세요 : ")
    # RangeString().solution(input_data)
    RangeString().teacher_solution(input_data)
