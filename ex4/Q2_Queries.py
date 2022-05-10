import pandas as pd
df = pd.read_csv("national-budget.csv", encoding='utf-8') # gloabl
pd.set_option('display.max_columns', None)

"""
    Question 1 
"""
def education_budget(year:int)->int:
    return df.loc[(df['שם רמה 2']=='חינוך') & (df['שנה']==year) ]['הוצאה נטו'].sum() ## My friend Samuel explained me how to get exactly the budget...

    #-------example-------
budget=education_budget(2000)## example for education budget in 2020
print(budget , "ILS")


"""
    Question 2
"""
def security_budget_ratio(year:int)->float:
    return df.loc[(df['שם תחום'] =='בטחון') & (df['שנה']==year) ]['הוצאה נטו'].sum() / df[(df['שנה']==year) ]['הוצאה נטו'].sum()   *100

    #-------example-------
print("The security budget of 2000 is",security_budget_ratio(2000),"%")

"""
    Question 3
"""
def largest_budget_year(office:str)->int:
    largest_sum = df[df['שם סעיף']== office]['הוצאה נטו'].idxmax()
    return df.loc[largest_sum]['שנה']

        #-------examples-------
print(largest_budget_year("משרד הבטחון"))
print(largest_budget_year("חינוך"))
print(largest_budget_year("הכנסות המדינה"))


"""
    Question 4:
 smallest budget year
"""
def Smallest_budget_year(office:str)->int:
    largest_sum = df[df['שם סעיף']== office]['הוצאה נטו'].idxmin()
    return df.loc[largest_sum]['שנה']

        #-------examples-------
print(Smallest_budget_year("משרד הבטחון"))
print(Smallest_budget_year("חינוך"))
print(Smallest_budget_year("משרד התיירות"))
print(Smallest_budget_year("משרד לבטחון פנים"))
print(Smallest_budget_year("משרד התחבורה"))
