# library import
from statistics import mean, stdev
import pandas
import matplotlib.pyplot as plt


# market designation
kc = 'markets/kc.csv'
snp = 'markets/snp.csv'
zw = 'markets/zw.csv'
unavailable = 'markets/mi'

# market selection
a = 'kc'

if a == 'kc':
    a = kc
elif a == 'snp':
    a = snp
elif a == 'zw':
    a = zw
else:
    a = unavailable

# market tag
if a == kc:
    b = 'Coffee Future (KC)'
elif a == snp:
    b = 'S&P500 Future'
elif a == zw:
    b = 'Wheat Future (ZW)'
else:
    b = 'UNAVAILABLE'

# csv reading
z = ['date', 'price', 'open_morning', 'high', 'low', 'volume', 'change']
data = pandas.read_csv(a, names=z)

date = data.date.tolist()
price = data.price.tolist()
open_morning = data.open_morning.tolist()
high = data.high.tolist()
low = data.low.tolist()
volume = data.volume.tolist()
change = data.change.tolist()


# list conversion from str to float
def delete_prct(list_input):
    list_c = []
    for i in list_input[1:]:
        f = i[:-1]
        list_c.append(f)
    return list_c


change_no_percentage = delete_prct(change)


def conv_stf(list_input):
    # note : creation de la variable que l'on souhaite retourner
    list_c = []
    for i in list_input[1:]:
        f = float(i)
        list_c.append(f)
    return list_c


change_float = conv_stf(change_no_percentage)

# mean
m = mean(change_float)
print('Mean: ' + str(m))

# standard deviation
sd = stdev(change_float)
print('Standard Deviation: ' + str(sd))


# print SD
def print_sd(mean_distribution, sd_distribution, rank):
    x = mean_distribution + rank*sd_distribution
    y = mean_distribution - rank*sd_distribution
    print('+ '+str(rank)+' SD: ' + str(x))
    print('- '+str(rank)+' SD: ' + str(y))


def value_sd(mean_distribution, sd_distribution, rank):
    x = mean_distribution + rank*sd_distribution
    y = mean_distribution - rank*sd_distribution
    return x, y


# mean +/- 1 SD
print_sd(m, sd, 1)
sd_1 = value_sd(m, sd, 1)

# mean +/- 2 SD
print_sd(m, sd, 2)
sd_2 = value_sd(m, sd, 2)

# mean +/- 3 SD
print_sd(m, sd, 3)
sd_3 = value_sd(m, sd, 3)

# mean +/- 4 SD
print_sd(m, sd, 4)
sd_4 = value_sd(m, sd, 4)

# mean +/- 5 SD
print_sd(m, sd, 5)
sd_5 = value_sd(m, sd, 5)


# value counting
def nb_value(list_a):
    return len(list_a)


def delta_h(list_a, value):
    return len([i for i in list_a if i >= value])


def delta_l(list_a, value):
    return len([i for i in list_a if i <= value])


# 1SD
sd_1_nbv = nb_value(change_float)
sd_1h_nbv = delta_h(change_float, sd_1[0])
sd_1l_nbv = delta_l(change_float, sd_1[1])


print(str(sd_1_nbv) + ' Values')
# print(sd_1h_nbv)
# print(sd_1l_nbv)

# TEST KC NORMAL DISTRIBUTION
# csv reading
j = ['kc_norm']
data_02 = pandas.read_csv('markets/KCnorm.csv', names=j)

kc_norm = data_02.kc_norm.tolist()

kc_norm_float = conv_stf(kc_norm)


# data visualisation
dist = change_float

bins = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.hist(dist, bins, histtype='bar', rwidth=0.8, color='blue')
plt.hist(kc_norm_float, bins, histtype='bar', rwidth=0.8, color='orange')

plt.xlabel('Change %')
plt.ylabel('')
plt.title('Price Distribution'+'\n'+str(b)+' - Daily')
plt.text(-20, 550, str(b)+'\n'+'Mean: '+str(m)[:5]+'\n'+'Standard Deviation: '+str(sd)[:5], color='blue')
plt.text(-20, 475, 'Random Normal Distribution'+'\n'+'(same parameters)', color='orange')
plt.grid(False)
plt.show()


