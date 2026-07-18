import random
import stddraw
from color import Color

def draw_bars(numbers, selected = ()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n

    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color  = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)

#--------------------------
#   ANIMATED
#--------------------------

def bubble_sort_animated(numbers):

    #CONFIG canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            #draw rectangles before swap
            draw_bars(numbers, selected=(j, j + 1))
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1] , numbers[j]
                #draw rectangles after the swap
                draw_bars(numbers, selected=(j, j + 1))

    draw_bars(numbers, selected=())
    stddraw.show()


def selecttion_sort_animated(numbers):

    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(i, j))
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
    draw_bars(numbers, selected=())
    stddraw.show()


def insertion_sort_animated(numbers):

    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    n = len(numbers)

    for i in range(n):
        draw_bars(numbers, selected = (i - 1, i))
        while i > 0:
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
            draw_bars(numbers, selected = (i - 1, i))
            i -= 1
    
    draw_bars(numbers, selected = ())
    stddraw.show()
 


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for x in range(10)]
    check = input("Select sort(BS, SS. IS): ")
    print(f"Unsorted: {numbers}")
    if check == "BS":
        bubble_sort_animated(numbers)
    elif check == "SS":
        selecttion_sort_animated(numbers)
    elif check == "IS":
        insertion_sort_animated(numbers)
    print(f"Sorted: {numbers}")