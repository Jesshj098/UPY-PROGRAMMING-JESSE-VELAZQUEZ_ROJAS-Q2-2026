import random
import stddraw

from color import Color


def bubble_sort(numbers):
    # INPUT: numbers - a list of numeric values to be sorted, in any order
    # PROCESS: repeatedly step through the list, compare each pair of
    #          adjacent elements, and swap them if they are in the wrong
    #          order; each full sweep pushes the next-largest value into
    #          its final position at the end of the list
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
    # OUTPUT: numbers - the same list, mutated in place so its values are
    #         now in ascending order


def insertion_sort(numbers):
    # INPUT: numbers - a list of numeric values to be sorted, in any order
    # PROCESS: build the sorted list one element at a time by taking the
    #          next unsorted value and shifting it left past any larger
    #          values already in the sorted portion until it lands in its
    #          correct position
    n = len(numbers)
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            j -= 1
    # OUTPUT: numbers - the same list, mutated in place so its values are
    #         now in ascending order


def selection_sort(numbers):
    # INPUT: numbers - a list of numeric values to be sorted, in any order
    # PROCESS: for each position, scan the remaining unsorted portion of
    #          the list to find the smallest value, then swap it into that
    #          position, growing the sorted portion by one each pass
    n = len(numbers)
    for sweep in range(n):
        min_idx = sweep
        for pair in range(sweep + 1, n):
            if numbers[pair] < numbers[min_idx]:
                min_idx = pair
        if min_idx != sweep:
            numbers[sweep], numbers[min_idx] = numbers[min_idx], numbers[sweep]
    # OUTPUT: numbers - the same list, mutated in place so its values are
    #         now in ascending order


def draw_bars(numbers, selected=()):
    # INPUT: numbers - the current state of the list to draw as bars;
    #        selected - a tuple of indices (0, 1, or 2 values) whose bars
    #        should be highlighted in a different color for this frame
    # PROCESS: clear the canvas, then draw one bar per value, coloring the
    #          bars listed in "selected" red and all others blue, sized so
    #          the bars evenly fill the drawing width
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n

    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    # OUTPUT: no return value; renders a single animation frame to the
    #         stddraw canvas showing the bars for this step
    stddraw.show(500)


# ANIMATED
def bubble_sort_animated(numbers):
    # INPUT: numbers - a list of numeric values to be sorted and animated
    # PROCESS: set up the drawing canvas, then run bubble sort, drawing a
    #          highlighted frame before comparing each adjacent pair and
    #          another highlighted frame immediately after any swap, so
    #          the viewer can watch each comparison/swap step by step
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            # DRAW the rectangles before the swap
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                # DRAW the rectangles after the swap
                draw_bars(numbers, selected=(pair, pair + 1))

    draw_bars(numbers)
    # OUTPUT: numbers - the same list, mutated in place into ascending
    #         order; a full animation of the sorting process is rendered
    #         to the canvas as a side effect
    stddraw.show()


def insertion_sort_animated(numbers):
    # INPUT: numbers - a list of numeric values to be sorted and animated
    # PROCESS: set up the drawing canvas, then run insertion sort, drawing
    #          a highlighted frame before each comparison and another
    #          right after any swap as a value is shifted into place,
    #          stopping the inward shift once the correct spot is found
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    for i in range(1, n):
        j = i
        while j > 0:
            # DRAW the rectangles before the swap
            draw_bars(numbers, selected=(j - 1, j))
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
                # DRAW the rectangles after the swap
                draw_bars(numbers, selected=(j - 1, j))
                j -= 1
            else:
                break

    draw_bars(numbers)
    # OUTPUT: numbers - the same list, mutated in place into ascending
    #         order; a full animation of the sorting process is rendered
    #         to the canvas as a side effect
    stddraw.show()


def selection_sort_animated(numbers):
    # INPUT: numbers - a list of numeric values to be sorted and animated
    # PROCESS: set up the drawing canvas, then run selection sort, drawing
    #          a frame before each comparison, another whenever a new
    #          minimum is found, and a before/after pair of frames around
    #          the swap that places the found minimum into position
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    for sweep in range(n):
        min_idx = sweep
        for pair in range(sweep + 1, n):
            # DRAW the rectangles before checking
            draw_bars(numbers, selected=(pair, min_idx))
            if numbers[pair] < numbers[min_idx]:
                min_idx = pair
                # DRAW the rectangles after a new minimum is found
                draw_bars(numbers, selected=(pair, min_idx))

        if min_idx != sweep:
            # DRAW the rectangles before the swap
            draw_bars(numbers, selected=(sweep, min_idx))
            numbers[sweep], numbers[min_idx] = numbers[min_idx], numbers[sweep]
            # DRAW the rectangles after the swap
            draw_bars(numbers, selected=(sweep, min_idx))

    draw_bars(numbers)
    # OUTPUT: numbers - the same list, mutated in place into ascending
    #         order; a full animation of the sorting process is rendered
    #         to the canvas as a side effect
    stddraw.show()


# INPUT: a randomly generated list of 10 integers between 0 and 100
numbers = [random.randint(0, 100) for x in range(10)]
print(f"Before: {numbers}")
# bubble_sort(numbers)
# insertion_sort(numbers)
# selection_sort(numbers)
# bubble_sort_animated(numbers)
# insertion_sort_animated(numbers)
selection_sort_animated(numbers)
# OUTPUT: the sorted list printed to the console, plus the rendered
#         animation shown on the stddraw canvas
print(f"After: {numbers}")
