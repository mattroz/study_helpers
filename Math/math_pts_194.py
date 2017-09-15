#	Calculate sample mean (x_b), standart deviation (sigma), variance (var)
#	theoretical frequencies

X = [10.01, 10.03, 10.05, 10.06, 10.09]		# random variate intervals
m = [9.0, 16.0, 47.0, 21.0, 7.0]						# empirical frequencies for each interval
#phi = [0.0478, 0.242, 0.397, 0.323, 0.0303]	# values from the table according to t[i]
phi = [0.3925, 0.3973, 0.3989, 0.3983, 0.3910]
t = []
theor_freq = []

h = X[1] - X[0]	# interval length
n = sum(m)		# sample size
x_b = 0.0			# sample mean
sigma = 0.0		# standart deviation
var	= 0.0			# variance


def calculate_sample_mean(rv, freq):
	_x_b = 0
	for i in range(0, len(m)):
		_x_b += X[i] * m[i]
	_x_b /= n
	print("sample mean = {}".format(_x_b))
	return _x_b


def calculate_standart_deviation(rv, freq, x_b):
	x_b_squared = 0.0
	_sigma = 0.0
	for i in range(0, len(m)):
		x_b_squared += (X[i]**2) * m[i]
	x_b_squared	/= n
	print("x_b = {}\nx_b_s = {}".format(x_b**2, x_b_squared))
	_sigma = (1.0101010101*(x_b_squared - (x_b**2)))**0.5
	print("standart deviation = {}".format(_sigma));
	return _sigma


def calculate_theoretical_frequencies(sigma, x_b):	# gives correct answer only if (in this case) sigma = 0.020802 instead of 0.01846
	_theor_freq = []
	for i in range(0,5):
		t.append((X[i] - x_b) / sigma)
		_theor_freq.append(h * n * phi[i] / sigma)
		print(_theor_freq[i])
	print('sum = {}'.format(sum(_theor_freq)))
	return _theor_freq

# Run
x_b = calculate_sample_mean(X, m)
sigma = calculate_standart_deviation(X, m, x_b);
#sigma = 0.20746276287518509
print('--------------------')
theor_freq = calculate_theoretical_frequencies(sigma, x_b)
print('--------------------')
