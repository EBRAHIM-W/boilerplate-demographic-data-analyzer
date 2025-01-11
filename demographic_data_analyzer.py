import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read.csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].count_values()

    # What is the average age of men?
    average_age_men = df.loc[df['sex']=='Male']['age'].mean().round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
     bachelors_count= loc[df['education']=='Bachelors'['education'].count()
    total_count=df['education'].count()
    percentage_bachelors=(bachelors_count/total_count*100).round(decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    education_salary_df =df.DataFrame(df.grouby(df['education'])['salary'].count_values()
    education_salary_df =     education_salary_df .rename(columns{'salary' : 'counts'})
    high_salary_df= education_salary_df.loc[(slice(None),'>50k'),:]
    higher_education =education_salary_df.loc[df ['Bachelors', 'Masters', 'Doctorate']].sum()
    lower_education = education_salary_df.sum()-higher_education

    # percentage with salary >50K
    high_education_rich_count = high_salary_df.loc[['Bachelors', 'Masters', 'Doctorate']].sum()
    lower_education_rich_count = high_salary_df.sum() - high_education_rich_count
    higher_education_rich = float((high_education_rich_count/higher_education*100).round(decimals=1)
    lower_education_rich = float((lower_education_rich_count/lower_education*100).round(decimals=1)
                                 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    hours_worked_salary_df=pd.DataFrame(df.groupby(['hours-per-week'])['salary'].count_value
    hours_worked_salary_df=hours_worked_salary_df.rename(columns={"salary" :"counts"})
    min_hours_worked_salary_df=hours_worked_salary_df.loc[min_work_hours,:]
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =  min_hours_worked_salary_df.sum()
    

    rich_percentage =float(( min_hours_worked_salary_df.loc['>50']/num_min_workers*100)).round(decimals=1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
