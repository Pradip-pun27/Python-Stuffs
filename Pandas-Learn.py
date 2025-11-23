import pandas as pd
        # Series Section
# s= pd.Series([1,9,12,121], index=['n1','n2','n3','n4'])
# for n in s:
#     print(n)
# print(s[s%2 ==1])
# s.loc['n3']+=100
# print(s.loc[['n3','n1']])

        # DataFrame Section
# d= {
#     'name':['Ram','Shyam','hai'],
#     'age':[11,21,20]
# }
# df= pd.DataFrame(d, index=['p1','p2','p3'])
# # Add new column
# df['job'] = ['Doctor','Engineer','C.A.']

# # Add new row
# new_row = pd.DataFrame([{'name':'Anu','age':18,'job':'Nurse'},
#                         {'name':'Anish','age':19,'job':'Manager'}],index=['p4','p5'])
# df = pd.concat([df,new_row])

# print(df[df['age']>=19])
# print(df[df.age<=18])

    # csv section
df =pd.read_csv('data.csv', index_col = "Name")
# Selection by cols
# print(df['Name'])
# print(df[['Height','Weight']])

# Selection by rows
# print(df.loc['Pikachu', ['Height','Weight']]) # Seclecting rows with only 2 cols: Ht & Wt
# # print(df.iloc[1])
# print(df.loc['Charizard':'Blastoise', ['Height','Weight']]) # idx slicing
# print(df.iloc[0:11:2, 0:3]) # idx slicing from 0:11 with 2 step and  with 3 cols only

# pokemon = input("Enter the Pokeman's name:")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} doesn't exist.")

  # Filtering : Keeping the rows that matched the condition
# tall_p =df[df['Height']>=2]
# fat_p = df[df.Weight>100]
# legend_p = df[df['Legendary']==1]
# water_p= df[(df.Type1=="Water") | (df.Type2 =="Water")]
# ff_p = df[(df.Type1=="Fire") & (df.Type2=="Flying")]
# print(ff_p)

# Aggregate Function
# Whole DataFrame(All cols)
# print(df.mean(numeric_only= True))
# print(df.min(numeric_only= True))
# print(df.max(numeric_only= True))
# print(df.sum(numeric_only= True))
# print(df.count())

# Single col
# print(df['Height'].mean())
# print(df['Height'].min())
# print(df['Height'].max())
# print(df['Height'].sum())
# print(df['Height'].count())

# groupby functions
# group = df.groupby('Type1')
# print(group['Height'].sum())
# print(group['Height'].min())
# print(group['Height'].max())
# print(group['Height'].count())

# Data Cleaning : Process of fixing/removing:
        # incomplete, irrelevant or incorrect data.
        # ~ 75% work done with pandas is data cleaning
 # Drop irrelevant cols
df.reset_index(inplace = True)
# df= df.drop(columns=['Legendary','No'])
# print(df)

 # Handle missing data
# print(len(df))
# df = df.dropna(subset=['Type2'])
# print(df.to_string())
# print(len(df))
# df = df.fillna({'Type2':'None'})
# print(df.to_string())

 # Fix the inconsistent values
# df['Type1'] = df['Type1'].replace({'Grass':'GRASS',
#                                    'Fire':'FIRE',
#                                    'Water':'WATER'})
# print(df.to_string())
 # Standardize the text
# df['Name'] = df['Name'].str.lower()
# print(df.to_string())

# Fix the data types
# df['Legendary'] = df['Legendary'].astype(bool)
# print(df.to_string())
#  #Remove the duplicate rows
# df = df.drop_duplicates()
# print(df)
# print(df.drop_duplicates())