

# a while loop to loop through each item in the list
i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1

# Use * to repeat lists
[1]*3

# check if something is inside a list

1 in [1, 2, 3]

# Unpack a sequence into different variables

x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x


# a convenient way for string formatting

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'
print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


# an example where we are grouping the cars by number of cylinder, and fnding the average cty mpg for each group
CtyMpgByCyl = []
for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

# Dates and Times in python
import datetime as dt
import time as tm

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

today = dt.date.today()
delta = dt.timedelta(days = 100) # create a timedelta of 100 days
today - delta # the date 100 days ago

# an example of a class in python
class Person:
    department = 'School of Information' #a class variable

    def set_name(self, new_name): #a method
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# How to map the <min> function between two lists
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)

for item in cheapest:
    print(item)

# Several interesting python functions

np.ones((3,2)); np.ones((3,2),int)
np.zeros((2,3))
np.eye(3)
np.diag([4,5,6])


# vstack and hstack

p = np.ones([2, 3], int)

#out: array([[1, 1, 1],
#            [1, 1, 1]])
   
p.shape

#out: (2, 3)

np.vstack([p, 2*p])

#out: array([[1, 1, 1],
#            [1, 1, 1],
#            [2, 2, 2],
#            [2, 2, 2]])

np.hstack([p, 2*p])

#out: array([[1, 1, 1, 2, 2, 2],
#            [1, 1, 1, 2, 2, 2]])


a.argmax()
a.argmin()


# ***************************

r = np.arange(36)
r.resize((6, 6))

# be careful with copying and modifying arrays in NumPy!

r_copy = r.copy()


############ < Pandas > ############

animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

# 0    Tiger
# 1     Bear
# 2    Moose
# dtype: object   

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)

# Archery           Bhutan
# Golf            Scotland
# Sumo               Japan
# Taekwondo    South Korea
# dtype: object

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])

# India      Tiger
# America     Bear
# Canada     Moose
# dtype: object

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)

# Archery           Bhutan
# Golf            Scotland
# Sumo               Japan
# Taekwondo    South Korea
# dtype: object

s.iloc[3]
#'South Korea'

s.loc['Golf']
#'Scotland'

s[3]
#'South Korea'

s['Golf']
#'Scotland'

%%timeit -n 100
summary = np.sum(s)
#100 loops, best of 3: 1.15 ms per loop

%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
s+=2

########## Pandas DataFrame ##########

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


df = pd.DataFrame({'Name': ['Chris', 'Kevyn', 'Vinod'],
                   'Item Purchased': ['Dog Food', 'Kitty Litter', 'Bird Seed'],
                   'Cost': [22.50, 2.5, 5.00]}, index= ['Store 1', 'Store 1', 'Store 2'])

# access DataFrame
df.loc['Store 2'] # loc is only for indexes; output series

# Cost                      5
# Item Purchased    Bird Seed
# Name                  Vinod
# Name: Store 2, dtype: object

df.loc['Store 1', 'Cost'] # loc is only for indexes; output series
df.loc['Store 1']['Cost']

# Store 1    22.5
# Store 1     2.5
# Name: Cost, dtype: float64

df['Cost'] # this is for accessing columns; output series

# WITH loc, we can also output DataFrame
df.loc[:,['Name', 'Cost']]

df.drop('Store 1') # this drop rows containing "Store 1", and output DataFrame


# Load csv file 
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)

# DataFrame rename column names
df.rename(columns={'old_name': 'new_name'}, inplace=True)


# Create a boolean mask 
df['Gold'] > 0

# np.where function in DataFrame; Replace values where the condition is False
df.where(df['Gold'] > 0)

# select/crop out a subset from a DataFrame based on condition
set_01 = df[df['Gold'] > 0]
set_02 = df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]







