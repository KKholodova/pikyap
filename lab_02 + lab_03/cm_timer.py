# Необходимо написать контекстные менеджеры cm_timer_1 и cm_timer_2, которые считают время работы блока кода и выводят его на экран. Пример:

# with cm_timer_1():
#     sleep(5.5)

# После завершения блока кода в консоль должно вывестись time: 5.5 (реальное время может несколько отличаться)
# cm_timer_1 и cm_timer_2 реализуют одинаковую функциональность, 
# но должны быть реализованы двумя различными способами (на основе класса и с использованием библиотеки contextlib)

import time

# with Context Manager 1

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time}")

# with Context Manager 2

from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"time: {elapsed_time}")

with cm_timer_1():
    time.sleep(5.5)

with cm_timer_2():
    time.sleep(5.5)