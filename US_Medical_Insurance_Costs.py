#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# ## Methodology 
# 
# ### Reviewing This Dataset
# When looking over the insurance.csv dataset, here are the **main observations**
# * There are four columns
#     * Age
#         * containing bionary, int data sets
#     * Sex
#         * containing bionary, sting data sets of 'male' and 'female'
#     * bmi
#         * containing a mix of data sets of int and floats (with no standardized number of decimals)
#     * children
#         * containing a int that are >= 0
#     * smoker
#         * containing bionary, string data sets of 'yes' and 'no'
#     * region
#         * containing one of four datasets, 'southwest', 'southeast', 'northwest', 'northeast'
#     * charges
#         * containing a mix of data sets of int and floats (with no standardized number of decimals)
# 
# 
# ### Scoping This Project
# * Things I'd like to look into
#     1. Find the average age, children, bmi, and charges
#     2. What region the majority of people are from (this is important for finding where to expand insurance for sales/marketing)
#     3. Average cost for 0, 1, 2, 3, 4 children (and what the average cost for adding a single child would cost)
#     4. Ratio of male:female
#         * The average cost per gender
#     5. Ratio of smoker:non-smoker
#         * Broaken down for cost of insurance, age, number of children, sex, bmi, region
# 
# * Useful data points that I'll need to create
#     * Overall averages; age, male:female ration, average bmi, average number of children, smoker:non-smoker ratio, majority region, average cost.
#     * Lists for each category
#     * An all encompasing dictionary made up of dictionaries that are profiles for each patient.
#     * Variables that hold how many patients are in each region
#         * Then rank them 1-4

# In[112]:


import csv 


# In[113]:


# First I need to start creating the lists that I'm going to need for my functions later on for analysis.
# First I'll create all the variables that I need and assign them empty lists that I'll uodate.
ages = []
sexes = []
bmis = []
num_children = []
smokers = []
regions = []
insurance_cost = []

# Append ages to fill it with everyones ages
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        ages.append(row['age'])
# Append sexes to fill it with everyones sexes
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        sexes.append(row['sex'])
# Append bmis to fill it with everyones bmis
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        bmis.append(row['bmi'])
# Append num_children to fill it with everyones number of children
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        num_children.append(row['children'])
# Append smokers to fill it with everyones smoking status
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        smokers.append(row['smoker'])
# Append regions to fill it with everyones region
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        regions.append(row['region'])
# Append insurance_cost to fill it with everyones cost of insurance
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        insurance_cost.append(row['charges'])

# Now I provided these print() functions so that we can test our lists to see what they look like, and make sure that we created them properly
#print(ages)
#print(sexes)
#print(bmis)
#print(num_children)
#print(smokers)
#print(regions)
#print(insurance_cost)

# The first thing that I notice is that all of these lists are lists of strings
# Which is fine for sexes, smokers, and regions; 
# But ages, bmis, num_children, and insurance_cost need to be numbers
# So now I'll create new lists that I can append to change to numbers
ages_updated = []
bmis_updated = []
num_children_updated = []
insurance_cost_updated = []

for item in ages:
    ages_updated.append(int(item))
for item in bmis:
    bmis_updated.append(float(item))
for item in num_children:
    num_children_updated.append(int(item))
for item in insurance_cost:
    insurance_cost_updated.append(float(item))

# Now we're going to print everything again to test it
#print(ages_updated)
#print(bmis_updated)
#print(num_children_updated)
#print(insurance_cost_updated)


# In[184]:


# Now that my lists have all been cleaned up, I need to calculate the over all Averages for bmi, ages, number of children, and insurance costs
# First I'll create the variables and set them to zero, to be updated later
average_ages = 0
average_bmi = 0
average_num_children = 0
average_insurance_cost = 0

# Now i need to create the functions to update these variables
# average_age_function
def average_ages_function(ages_updated):
    total_age = 0
    global average_ages
    for ages in ages_updated:
        total_age += ages
    average_ages = total_age / len(ages_updated)
    return int(average_ages)
        
average_ages = average_ages_function(ages_updated)
#print(average_ages)

# Average bmi function
def average_bmi_function(bmis_updated):
    total_bmi = 0
    global average_bmi
    for bmi in bmis_updated:
        total_bmi += bmi
    average_bmi = total_bmi / len(bmis_updated)
    return average_bmi
        
average_bmi = average_bmi_function(bmis_updated)
#print(average_bmi)

#Average Number of Children
def average_num_children_function(ages_updated):
    total_children = 0
    global average_num_children
    for children in num_children_updated:
        total_children += children
    average_num_children = total_children / len(num_children_updated)
    return int(average_num_children)
        
average_num_children = average_num_children_function(num_children_updated)
#print(average_num_children)

def average_insurance_cost_function(insurance_cost_updated):
    total_cost = 0
    global average_insurnace_cost
    for cost in insurance_cost_updated:
        total_cost += cost
    average_insurance_cost = total_cost / len(insurance_cost_updated)
    return average_insurance_cost
        
average_insurance_cost = average_insurance_cost_function(insurance_cost_updated)
#print(average_insurance_cost)


# In[186]:


# Now I want to break down the regions to see what region the majority of people are from, and then rank them
# First we need to find the population of each region
northeast = 0
northwest = 0
southeast = 0
southwest = 0

def region_breakdown(regions):
    global northeast, northwest, southeast, southwest
    for region in regions:
        if region == 'northeast':
            northeast = northeast + 1
        elif region == 'northwest':
            northwest = northwest + 1
        if region == 'southeast':
            southeast = southeast + 1
        else:
            southwest = southwest + 1

# Now that we have the population of each region we need to find region rank 1.
region_ranking_1 = []
region_ranking_2 = []
region_ranking_3 = []
region_ranking_4 = []

def region_ranking_1_function(northeast, northwest, southeast, southwest):
    global region_ranking_1, region_ranking_2, region_ranking_3, region_ranking_4
    if northeast > northwest and northeast > southeast and northeast > southwest:
        region_ranking_1.append('Northeast')
    elif northwest > northeast and northwest > southeast and northwest >southwest:
        region_ranking_1.append('Northwest')
    elif southeast > northeast and southeast > northwest and southeast > southwest:
        region_ranking_1.append('Southeast')
    elif southwest > northeast and southwest > northwest and southwest > southeast:
        region_ranking_1.append('Southwest')

# Now that we have the population of each region we need to find region rank 2.
def region_ranking_2_function(northeast, northwest, southeast, southwest):
    global region_ranking_1, region_ranking_2, region_ranking_3, region_ranking_4
    if northeast > northwest and northeast > southeast:
        region_ranking_2.append('Northeast')
    elif northwest > northeast and northwest > southeast:
        region_ranking_2.append('Northwest')
    elif southeast > northeast and southeast > northwest:
        region_ranking_2.append('Southeast')

# Now that we have the population of each region we need to find region rank 3 and 4.
def region_ranking_3_function(northeast, northwest, southeast, southwest):
    global region_ranking_1, region_ranking_2, region_ranking_3, region_ranking_4
    if northeast > northwest:
        region_ranking_3.append('Northeast')
    else:
        region_ranking_3.append('Northwest')
        region_ranking_4.append('Northeast')

region_breakdown(regions)
#print(northeast)
#print(northwest)
#print(southeast)
#print(southwest)

region_ranking_1_function(northeast, northwest, southeast, southwest)
print(region_ranking_1)
region_ranking_2_function(northeast, northwest, southeast, southwest)
print(region_ranking_2)
region_ranking_3_function(northeast, northwest, southeast, southwest)
print(region_ranking_3)
print(region_ranking_4)


# In[187]:


# Now I need to figure out cost averages for each number of children. 

# First we need to find the max number of children that someone has so that we can use it to create some functions
# num_children_updated.sort() tells us that the highest number of children is 5

# Fist we need to calculate the total cost for each number of children collectivly, so we can divide that number to find the average
children_cost = list(zip(num_children_updated, insurance_cost_updated))
total_cost_0_child = 0
total_cost_1_child = 0
total_cost_2_child = 0
total_cost_3_child = 0
total_cost_4_child = 0
total_cost_5_child = 0

for child in children_cost:
    if child[0] == 0:
        total_cost_0_child += child[1]
    elif child[0] == 1:
        total_cost_1_child += child[1]
    elif child[0] == 2:
        total_cost_2_child += child[1]
    elif child[0] == 3:
        total_cost_3_child += child[1]
    elif child[0] == 4:
        total_cost_4_child += child[1]
    elif child[0] == 5:
        total_cost_5_child += child[1]
#print(total_cost_1_child)
#print(total_cost_2_child)
#print(total_cost_3_child)
#print(total_cost_4_child)
#print(total_cost_5_child)

# Now we need to find out how many people have each number of children
num_ppl_with_0 = 0
num_ppl_with_1 = 0
num_ppl_with_2 = 0
num_ppl_with_3 = 0
num_ppl_with_4 = 0
num_ppl_with_5 = 0

for child in num_children_updated:
    if child == 0:
        num_ppl_with_0 = num_ppl_with_0 + 1
    elif child == 1:
        num_ppl_with_1 = num_ppl_with_1 + 1
    elif child == 2:
        num_ppl_with_2 = num_ppl_with_2 + 1
    elif child == 3:
        num_ppl_with_3 = num_ppl_with_3 + 1
    elif child == 4:
        num_ppl_with_4 = num_ppl_with_4 + 1
    elif child == 5:
        num_ppl_with_5 = num_ppl_with_5 + 1
#print(num_ppl_with_0)
#print(num_ppl_with_1)
#print(num_ppl_with_2)
#print(num_ppl_with_3)
#print(num_ppl_with_4)
#print(num_ppl_with_5)

# Now we need to find the total averages using these new variables that we created
average_cost_0_children = total_cost_0_child / num_ppl_with_0
average_cost_1_children = total_cost_1_child / num_ppl_with_1
average_cost_2_children = total_cost_2_child / num_ppl_with_2
average_cost_3_children = total_cost_3_child / num_ppl_with_3
average_cost_4_children = total_cost_4_child / num_ppl_with_4
average_cost_5_children = total_cost_5_child / num_ppl_with_5
#print(average_cost_0_children)
#print(average_cost_1_children)
#print(average_cost_2_children)
#print(average_cost_3_children)
#print(average_cost_4_children)
#print(average_cost_5_children)

# Now we can find the average cost per child
average_cost_per_child = (average_cost_0_children + average_cost_1_children + average_cost_2_children + average_cost_3_children + average_cost_4_children + average_cost_5_children) / 6
#print(average_cost_per_child)


# In[189]:


# Now we can figure out the ratio of male:female and the respective average cost for each gender

# First we need to calculate the number of males and females that we have respectivly
sex_costs = list(zip(sexes, insurance_cost_updated))
num_males = 0
num_females = 0

for sex in sex_costs:
    if sex[0] == 'male':
        num_males = num_males + 1
    elif sex[0] == 'female':
        num_females = num_females + 1
#print(num_males)
#print(num_females)

# Now we need to calculate the total cost of males and females so that we then devide it to find the average
total_male_cost = 0
total_female_cost = 0

for sex in sex_costs:
    if sex[0] == 'male':
        total_male_cost += sex[1]
    elif sex[0] == 'female':
        total_female_cost += sex[1]
#print(total_male_cost)
#print(total_female_cost)

# Now we're going to calculate the avergae cost per gender 
average_male_cost = total_male_cost / num_males
average_female_cost = total_female_cost / num_females
#print(average_male_cost)
#print(average_female_cost)
#print(average_insurance_cost)


# In[191]:


# Now we can figure out the number of smokers vs non-smokers and how much their insurance costs respectavly.

# First we need to figure out the number of smokers and non-smokers
smoker_costs = list(zip(smokers, insurance_cost_updated))
num_smoker = 0
num_non_smoker = 0

for smoke in smoker_costs:
    if smoke[0] == 'yes':
        num_smoker += 1
    elif smoke[0] == 'no':
        num_non_smoker += 1
#print(num_smoker)
#print(num_non_smoker)

# Now we have to calculate the total cost for smokers and non-smokers so that we can use it to find the average.
total_smoker_cost = 0
total_non_smoker_cost = 0

for smoke in smoker_costs:
    if smoke[0] == 'yes':
        total_smoker_cost = total_smoker_cost + smoke[1]
    elif smoke[0] == 'no':
        total_non_smoker_cost = total_non_smoker_cost + smoke[1]
#print(total_smoker_cost)
#print(total_non_smoker_cost)

# Now we can calculate the average for smokers and non-smokers respectivly
average_smoker_cost = total_smoker_cost / num_smoker
average_non_smoker_cost = total_non_smoker_cost / num_non_smoker
print(average_smoker_cost)
print(average_non_smoker_cost)


# ### Conclusions
# 
# #### Topline Averages
# 
# NOTE: All costs are reflected in USD.
# 
# 1. Find the average age, children, bmi, and charges
#     1. **Average Age:** 
#         1. The average age of a patient is 39 years old
#     2. **Average Number of Children**
#         1. The average number of children of a patient is 1 child
#     3. **Average BMI**
#         1. The average BMI of a patient is 30.66
#     4. **Average Cost of Insurance**
#         1. The average cost of health insurance is 13,270.42
# 
# 2. What region has the majority of people 
#     1. The region where the most patients live in is the _Southwest_ with _974 patients_.
#     2. The ranking of the regions from most patients, 1, to lowest number of patients, 4.
#         1. Southwest
#         2. Southeast
#         3. Northwest
#         4. Northeast
#             * Based on this information we should tell our marketing team and sales teams to work on growing the number of patients we have starting in the _Northeast where we have the highest potential for new customers_.
#             
# 3. Average cost of 0, 1, 2, 3, 4 children
#     1. **Average Cost for 0 Children**
#         * 12,365.98
#     2. **Average Cost for 1 Child**
#         * 12,731.17
#     3. **Average Cost for 2 Children**
#         * 15,073.56
#     4. **Average Cost for 3 Children**
#         * 15,355.32
#     5. **Average Cost for 4 Children**
#         * 13,850.66
#     6. **Average Cost for 5 Children**
#         * 8,786.04
#     7. **Average cost increased per adding a _single child_**
# 
# 
# 4. Male:Female Ratio and Average Cost Per Sex
#     1. **Male:** 676 with an average cost of 13,956.75, 
#         1. 686.33 _higher_ than the average.
#     2. **Female:** 662 with an average cost of 12,569.58, 
#         1. 700.84 _lower_ than the average.
#     
# 
# 5. Smoker:Non-Smoker Ratio and Average Cost Per Smoking/Non_Smoking
#     1. **Smokers:** 274 with an average cost of 32050.23
#         1. 18,779.81 _higher_ than the average cost
#     2. **Non-Smokers:** 1064 with an average cost of 8434.27
#         1. 4,836.15 _lower_ than the average cost
# 
