import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Read in dataframe from Excel document
    df = pd.read_excel('Baby Names Dataset.xlsx')

    # Rename columns
    df.columns = ['year', 'name', 'sex', 'count']

    # Add column containing number of letters in name
    df['letter_count'] = df['name'].apply(lambda x: len(x))

    print(df)

    plot_letter_count(df)
    most_popular_name(df)


def plot_letter_count(df):
    word_count_df = df.groupby('year')['letter_count'].mean().to_frame(name='avg_letter_count')

    plt.figure()
    word_count_df.plot()
    plt.title('Average Number of Letters Per Name')
    plt.xlabel('Year')
    plt.ylabel('Letters')
    plt.show()


def most_popular_name(df):
    # Dataframe showing which names have appeared on the list the most times
    name_appearances_df = df.groupby(['name', 'sex'])['count'].count().to_frame()
    name_appearances_df = name_appearances_df.reset_index()
    name_appearances_df = name_appearances_df.sort_values(by=['count', 'name'], ascending=True)

    # Male name listed the most times
    male_apps_df = name_appearances_df[name_appearances_df['sex'] == 'M']

    male_136_df = male_apps_df[male_apps_df['count'] == 136]    # 136 is the total number of years recorded
    print('\nMale names appearing every year (total: {}):'.format(male_136_df['name'].count()))
    print(male_136_df['name'].tolist())

    # Female name listed the most times
    female_apps_df = name_appearances_df[name_appearances_df['sex'] == 'F']

    female_136_df = female_apps_df[female_apps_df['count'] == 136]  # 136 is the total number of years recorded
    print('\nFemale names appearing every year (total: {}):'.format(female_136_df['name'].count()))
    print(female_136_df['name'].tolist())

    # Dataframe showing the total number of people given each name
    name_count_df = df.groupby(['name', 'sex'])['count'].sum().to_frame()
    name_count_df = name_count_df.reset_index()

    print('\n')

    # Male name with highest count
    male_totals_df = name_count_df[name_count_df['sex'] == 'M']
    male_totals_df = male_totals_df.sort_values(['count'], ascending=False)
    male_totals_df = male_totals_df.reset_index()
    male_totals_df.index = male_totals_df.index + 1
    male_totals_df = male_totals_df.drop(columns=['index', 'sex'])
    print('Top 50 male names:')
    print(male_totals_df[:50])

    print()

    # Female name with highest count
    female_totals_df = name_count_df[name_count_df['sex'] == 'F']
    female_totals_df = female_totals_df.sort_values(['count'], ascending=False)
    female_totals_df = female_totals_df.reset_index()
    female_totals_df.index = female_totals_df.index + 1
    female_totals_df = female_totals_df.drop(columns=['index', 'sex'])
    print('Top 50 female names:')
    print(female_totals_df[:50])


main()
