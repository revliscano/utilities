from timeit import timeit


def measure_time(func, *args, number=100, modules=None, **kwargs):
	globals_ = {'func': func, 'args': args, 'kwargs': kwargs}
	if modules:
		globals_.update({module.__name__: module for module in modules})
	return timeit(f'func(*args, **kwargs)',
		      number=number,
		      globals=globals_)
