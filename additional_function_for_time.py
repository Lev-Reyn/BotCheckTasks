"""для того что бы функция приостанавливалась, если шлишком долго раотает"""
import signal
from contextlib import contextmanager


class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds):
    """принимает колличество секунд, которое можем истратить на функцию, если функция работает дольше данного времени,
    то функция перестаёт работать"""

    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

# пример как нужно работать с данной функцией
# try:
#     with time_limit(10):
#         long_function_call()  # функция, которую тестим
# except TimeoutException as e:
#     print("Timed out!")
