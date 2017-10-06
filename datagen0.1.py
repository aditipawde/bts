# import packages
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import style

# input N
N = 1000

# Parameters -- to be read from config file
ns = 10
industry_sectors = np.arange(ns)
industry_sector_names = ['Computer s/w', 'Hotels and resorts', 'Cloth manufatcuring', 'Construction', 'Electronics component manufacturing',
'Chemical manufacturing', 'Insurance agency', 'Jewelers','Medical and nursing services','Pharmaceuticals'
]
p_industry_sector = [0.2, 0.1, 0.05, 0.1, 0.05, 0.05, 0.05, 0.1, 0.1, 0.2]
#industry categorization
bulk = [3, 5]
semi_bulk = [2, 4, 6]
retail = [0, 1, 7, 8, 9]
locations = ['INDIA', 'OFFSHORE']
p_locations = [0.99, 0.01]
is_tax_haven = ['YES', 'NO']
p_tax_haven = [0.99, 0.01]
num_owners = [1, 2, 3, 4, 5]
p_owners = [0.45, 0.3, 0.2, 0.025, 0.025]
is_private = ['YES', 'NO']
p_is_private = [0.5, 0.5]
employee_base = ['VERY SMALL', 'SMALL', 'MEDIUM', 'LARGE', 'VERY LARGE']
p_emp_base = [0.2, 0.26, 0.26, 0.18, 0.1]
rev_per_emp_month_size = ['VERY LOW', 'LOW', 'MEDIUM', 'HIGH', 'VERY HIGH']
rev_categorization = [[8], [2, 4 ,5], [6, 9], [1, 3, 7], [0]]


# Generate lists based on probability distribution of parameters
c_id = np.arange(N)
c_sector = np.random.choice(industry_sectors, N, p=p_industry_sector)
c_loc = np.random.choice(locations, N, p=p_locations)
c_n_owners = np.random.choice(num_owners, N, p=p_owners)
c_is_private = np.random.choice(is_private, N, p=p_is_private)
c_emp_base = np.random.choice(employee_base, N, p=p_emp_base)


# zip each item in the list to form tuples
c_list = list(zip(c_id, c_sector, c_loc, c_n_owners, c_is_private, c_emp_base))

# Form dataframe out of list
c_dataframe = pd.DataFrame(data = c_list, columns=['comp_id', 'industry_sector', 'location', 'num_owners', 'is_private', 'emp_base'])

# Generate calculated columns

# Insert columns in dataframe for is_tax_haven, num_employees, industry_category, annual_revenue, net_revenue
c_dataframe.insert(loc=3, column='is_tax_haven', value='')
c_dataframe.insert(loc=7, column='num_employees', value = np.zeros([N, 1], dtype=int))
c_dataframe.insert(loc=8, column='industry_category', value = np.zeros([N, 1], dtype=int))
c_dataframe.insert(loc=9, column='rev_per_emp_month_size', value = '')
c_dataframe.insert(loc=10, column='annual_revenue', value = np.zeros([N, 1], dtype=float))
c_dataframe.insert(loc=11, column='net_revenue', value = np.zeros([N, 1], dtype=float))

# Generation of number of employees
e_mu1, e_sigma1 = 25, 5
e_mu2, e_sigma2 = 200, 50
e_mu3, e_sigma3 = 2500, 500
e_mu4, e_sigma4 = 50000, 10000
e_mu5, e_sigma5 = 300000, 50000

e_x_vsmall = np.random.normal(e_mu1, e_sigma1, N)
e_x_small = np.random.normal(e_mu2, e_sigma2, N)
e_x_med = np.random.normal(e_mu3, e_sigma3, N)
e_x_large = np.random.normal(e_mu4, e_sigma4, N)
e_x_vlarge = np.random.normal(e_mu5, e_sigma5, N)

e_y_vsmall = np.random.normal(0.1 * e_x_vsmall, 0.01 * e_x_vsmall, N)
e_y_small = np.random.normal(0.1 * e_x_small, 0.01 * e_x_small, N)
e_y_med = np.random.normal(0.1 * e_x_med, 0.01 * e_x_med, N)
e_y_large = np.random.normal(0.1 * e_x_large, 0.01 * e_x_large, N)
e_y_vlarge = np.random.normal(0.1 * e_x_vlarge, 0.01 * e_x_vlarge, N)

e_z_vlow = np.random.normal(e_x_vsmall, e_y_vsmall)
e_z_low = np.random.normal(e_x_small,  e_y_small)
e_z_med = np.random.normal(e_x_med, e_y_med)
e_z_high = np.random.normal(e_x_large, e_y_large)
e_z_vhigh = np.random.normal(e_x_vlarge, e_y_vlarge)

# Dictionary for generating number of employees
def get_num_emp (x):
    return {
        'VERY SMALL': int(np.random.choice(e_z_vlow)),
        'SMALL': int(np.random.choice(e_z_low)),
        'MEDIUM': int(np.random.choice(e_z_med)),
        'LARGE': int(np.random.choice(e_z_high)),
        'VERY LARGE': int(np.random.choice(e_z_vhigh))
    }[x]

# Normal distributions for annual_revenue

mu1, sigma1 = 65000, 6500
mu2, sigma2 = 250000, 25000
mu3, sigma3 = 550000, 55000
mu4, sigma4 = 1050000, 105000
mu5, sigma5 = 1950000, 195000

x_very_low = np.random.normal(mu1, sigma1, N)
x_low = np.random.normal(mu2, sigma2, N)
x_medium = np.random.normal(mu3, sigma3, N)
x_high = np.random.normal(mu4, sigma4, N)
x_very_high = np.random.normal(mu5, sigma5, N)

y_very_low = np.random.normal(0.1 * x_very_low, 0.01 * x_very_low, N)
y_low = np.random.normal(0.1 * x_low, 0.01 * x_low, N)
y_medium = np.random.normal(0.1 * x_medium, 0.01 * x_medium, N)
y_high = np.random.normal(0.1 * x_high, 0.01 * x_high, N)
y_very_high = np.random.normal(0.1 * x_very_high, 0.01 * x_very_high, N)

z_very_low = np.random.normal(x_very_low, y_very_low)
z_low = np.random.normal(x_low, y_low)
z_medium = np.random.normal(x_medium, y_medium)
z_high = np.random.normal(x_high, y_high)
z_very_high = np.random.normal(x_very_high, y_very_high)

def get_annual_rev (x):
    return{
        'VERY LOW': np.round(random.choice(z_very_low), 2),
        'LOW': np.round(random.choice(z_low), 2),
        'MEDIUM': np.round(random.choice(z_medium), 2),
        'HIGH': np.round(random.choice(z_high), 2),
        'VERY HIGH': np.round(random.choice(z_very_high), 2)
    }[x]

# industry categorization
def get_industry_cat (x):
    return{
        0: 'r',
        1: 'r',
        2: 's',
        3: 'b',
        4: 's',
        5: 'b',
        6: 's',
        7: 'r',
        8: 'r',
        9: 'r'
    } [x]

# Function for getting revenue per employee per month categorization
def find_rev_size(sector_id):
    for i, val in enumerate(rev_categorization):
        if sector_id in rev_categorization[i]:
            return rev_per_emp_month_size[i]


# Distribution of for profit and loss
percent_pl = np.random.normal(4, 3, 1000)

c_dataframe.set_index('comp_id')

# Calculated columns
for comp_id in range(N):
    if(c_dataframe.loc[comp_id, 'location'] == 'INDIA'):
        c_dataframe.loc[comp_id, 'is_tax_haven'] = 'NO'
    else:
        c_dataframe.loc[comp_id, 'is_tax_haven'] = np.random.choice(is_tax_haven, p=p_tax_haven)

    c_dataframe.loc[comp_id, 'num_employees'] = get_num_emp(c_dataframe.loc[comp_id, 'emp_base']) # Uniform probability for number of employees
    c_dataframe.loc[comp_id, 'industry_category'] = get_industry_cat(c_dataframe.loc[comp_id, 'industry_sector']) # Assign industry category based on industry sector
    c_dataframe.loc[comp_id, 'rev_per_emp_month_size'] = find_rev_size(c_dataframe.loc[comp_id, 'industry_sector'])
    c_dataframe.loc[comp_id, 'annual_revenue'] = np.round(12 * c_dataframe.loc[comp_id, 'num_employees'] * get_annual_rev(c_dataframe.loc[comp_id, 'rev_per_emp_month_size']), 2) # annual_revenue = 12 * num_employees * revenue per employee per month
    c_dataframe.loc[comp_id, 'net_revenue'] = np.round(percent_pl[comp_id] * c_dataframe.loc[comp_id, 'annual_revenue'] / 100, 2)


c_dataframe.to_csv('data.csv', ',')
print(c_dataframe)


size = 'SMALL'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']
print(series)
style.use('ggplot')

plt.hist(series, bins=10, normed=True, align = 'mid')


plt.show()