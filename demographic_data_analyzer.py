import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education']=='Bachelors']['education'].count()/df['education'].count())*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    salary_BMD=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]['salary'].value_counts()
    salary_BMD_morethan50k= round(((salary_BMD['>50K']/salary_BMD.sum())*100),1)
    # What percentage of people without advanced education make more than 50K?
    salary_other=df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]['salary'].value_counts()
    salary_other_morethan50k= round(((salary_other['>50K']/salary_other.sum())*100),1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((df[df['education'].isin(['Bachelors','Masters','Doctorate'])]['education'].count()/df['education'].count())*100,1)
    lower_education = 100-higher_education

    # percentage with salary >50K
    higher_education_rich = salary_BMD_morethan50k
    lower_education_rich = salary_other_morethan50k

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_sal=df[df['hours-per-week'] == df['hours-per-week'].min()]['salary']
    num_min_workers = df_min_sal.count()

    rich_percentage = round((df_min_sal == '>50K').sum()/df_min_sal.count()*100,1)

    # What country has the highest percentage of people that earn >50K?
    df_l50k=df[df['salary']=='>50K']
    df_50k_country = df_l50k['native-country'].value_counts()
    df_country= df['native-country'].value_counts()
    country_percent= round((df_50k_country/df_country)*100,1)
    highest_earning_country = country_percent.sort_values(ascending=False).idxmax()
    highest_earning_country_percentage =   country_percent.sort_values(ascending=False).max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df_l50k[df_l50k['native-country']=='India']['occupation'].value_counts().idxmax()

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
