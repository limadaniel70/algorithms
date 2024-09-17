def my_range(stop: int, start: int = 0, step: int = 1):
    iterator = start
    while iterator < stop:
        yield iterator
        iterator += step
if __name__ == "__main__":
    for i in my_range(10):
        print(i)
