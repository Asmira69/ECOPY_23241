#GY7EJG
#felülírás nélkül nem futottak le de biztosan rosszul használtam a new_df = input_df.copy() kódot
#1
euro12 = pd.read_csv('Euro_2012_stats_TEAM.csv')

#2
def number_of_participants(input_df):
    num_participants = input_df['Team'].nunique()

    return num_participants

#3
def extract_goals_columns(euro12):
    """
    Extracts the 'Team' and 'Goals' columns from the euro12 DataFrame.

    Parameters:
    euro12 (pd.DataFrame): The input DataFrame containing the data.

    Returns:
    pd.DataFrame: A new DataFrame containing only the 'Team' and 'Goals' columns.
    """
    required_columns = ['Team', 'Goals']

    for col in required_columns:
        if col not in euro12.columns:
            raise ValueError(f'The "{col}" column is not found in the DataFrame.')

    goals = euro12[required_columns]
    return goals

#4
def sort_teams_by_goals(euro12):
    """
    Sorba rendezi az országokat a lőtt gólok száma alapján csökkenő sorrendben.

    Parameters:
    euro12 (pd.DataFrame): Az input DataFrame, amely tartalmazza az országokat és a lőtt gólok számát.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely az országokat és a lőtt gólok számát tartalmazza csökkenő sorrendben.
    """
    # Használjuk az előző függvényt a 'Team' és 'Goals' oszlopok kinyerésére
    team_goals_data = extract_goals_columns(euro12)

    # Sorba rendezzük csökkenő sorrendben a lőtt gólok alapján
    sorted_teams = team_goals_data.sort_values(by='Goals', ascending=False)

    return sorted_teams
#5
def avg_goal(input_df):
    """
    Visszaadja az átlagos gólszámot az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    float: Az átlagos gólszám.
    """
    # Ellenőrizze, hogy a DataFrame tartalmazza-e a "Goals" oszlopot
    if 'Goals' not in input_df.columns:
        raise ValueError('A "Goals" oszlop nem található a DataFrame-ben.')

    # Számolja meg az összes gólt és osztja el a csapatok számával
    total_goals = input_df['Goals'].sum()
    num_teams = len(input_df)
    avg_goals = total_goals / num_teams

    return avg_goals

#6
def countries_over_six(input_df):
    """
    Visszaadja azokat az országokat, amelyek 6 vagy több gólt rúgtak az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely azokat az országokat tartalmazza, amelyek 6 vagy több gólt rúgtak.
    """
    # Ellenőrizze, hogy a DataFrame tartalmazza-e a "Team" és "Goals" oszlopokat
    required_columns = ['Team', 'Goals']
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Szűrjük az országokat, amelyek 6 vagy több gólt rúgtak
    selected_countries = input_df[input_df['Goals'] >= 6][required_columns]

    return selected_countries

#7
def countries_starting_with_g(input_df):
    """
    Visszaadja azon országok neveit, amelyek neve 'G'-vel kezdődik az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely azon országok neveit tartalmazza, amelyek 'G'-vel kezdődnek.
    """
    # Ellenőrizze, hogy a DataFrame tartalmazza-e a "Team" oszlopot
    if 'Team' not in input_df.columns:
        raise ValueError('A "Team" oszlop nem található a DataFrame-ben.')

    # Szűrjük az országokat, amelyek neve 'G'-vel kezdődik
    selected_countries = input_df[input_df['Team'].str.startswith('G')]

    return selected_countries[['Team']]

#8
def first_seven_columns(input_df):
    """
    Visszaadja az első 7 oszlopot az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely az első 7 oszlopot tartalmazza.
    """
    # Ellenőrizze, hogy az input DataFrame legalább 7 oszlopot tartalmaz
    if len(input_df.columns) < 7:
        raise ValueError('Az input DataFrame-nek legalább 7 oszlopnak kell lennie.')

    # Kiválasztja az első 7 oszlopot
    selected_columns = input_df.iloc[:, :7]

    return selected_columns

#9
def every_column_except_last_three(input_df):
    """
    Visszaadja az összes oszlopot az utolsó 3-on kívül az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely az összes oszlopot tartalmazza az utolsó 3-on kívül.
    """
    # Ellenőrizze, hogy az input DataFrame legalább 3 oszlopot tartalmaz
    if len(input_df.columns) <= 3:
        raise ValueError('Az input DataFrame-nek több, mint 3 oszlopnak kell lennie.')

    # Kiválasztja az összes oszlopot az utolsó 3-on kívül
    selected_columns = input_df.iloc[:, :-3]

    return selected_columns

#10
def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    """
    Adott oszlopokat és sorokat választ ki a bemeneti DataFrame-ből.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.
    columns_to_keep (list): A kiválasztandó oszlopok neveinek listája.
    column_to_filter (str): Az oszlop neve, amely alapján a sorokat szűrni kell.
    rows_to_keep (list): A kiválasztandó sorok értékeinek listája a szűréshez.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely csak a kiválasztott oszlopokat és sorokat tartalmazza.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a megadott oszlopokat és a szűrő oszlopot
    required_columns = columns_to_keep + [column_to_filter]
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Szűrjük az input DataFrame-et a megadott oszlop és értékek alapján
    filtered_data = input_df[input_df[column_to_filter].isin(rows_to_keep)][columns_to_keep]

    return filtered_data

#11
import random
import  typing
from typing import List

def generate_quartile(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Kiegészíti a bemeneti DataFrame-t egy 'Quartile' oszloppal a lőtt gólok alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely tartalmazza az 'Quartile' oszlopot.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a "Goals" oszlopot
    if 'Goals' not in input_df.columns:
        raise ValueError('A "Goals" oszlop nem található a DataFrame-ben.')

    # Készítse el a kvartilisok alapján az oszlopot
    conditions = [
        (input_df['Goals'] >= 6) & (input_df['Goals'] <= 12),
        (input_df['Goals'] == 5),
        (input_df['Goals'] >= 3) & (input_df['Goals'] <= 4),
        (input_df['Goals'] >= 0) & (input_df['Goals'] <= 2)
    ]

    quartile_values = [1, 2, 3, 4]

    # Hozzáadja az 'Quartile' oszlopot az input DataFrame-hez
    input_df['Quartile'] = pd.Series(random.choices(quartile_values, k=len(input_df)))

    return input_df

#12
def average_yellow_in_quartiles(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Kiszámítja átlagosan hány passzot adtak minden kvartilis értékhez az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely tartalmazza az átlagos passzokat minden kvartilis értékhez.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a megfelelő oszlopokat
    required_columns = ['Quartile', 'Passes']
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Csoportosítsa az adatokat kvartilis és számolja meg az átlagos passzokat
    avg_passes_by_quartile = input_df.groupby('Quartile')['Passes'].mean().reset_index()

    return avg_passes_by_quartile

#13
def minmax_block_in_quartile(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Visszaadja minden kvartilis esetén a blokkok minimális és maximális értékét az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    pd.DataFrame: Egy új DataFrame, amely tartalmazza minden kvartilis esetén a blokkok minimális és maximális értékét.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a megfelelő oszlopokat
    required_columns = ['Quartile', 'Blocks']
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Csoportosítsa az adatokat kvartilis szerint és számolja meg a blokkok minimális és maximális értékét
    minmax_blocks_by_quartile = input_df.groupby('Quartile')['Blocks'].agg(['min', 'max']).reset_index()

    return minmax_blocks_by_quartile

#14
import matplotlib.pyplot as plt

def scatter_goals_shots(input_df: pd.DataFrame) -> plt.Figure:
    """
    Scatter plot-ot készít a gólok és a kaput ért találatok kapcsolatáról az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    plt.Figure: A matplotlib ábra objektuma.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a megfelelő oszlopokat
    required_columns = ['Goals', 'Shots on target']
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Scatter plot létrehozása
    fig, ax = plt.subplots()
    ax.scatter(input_df['Goals'], input_df['Shots on target'])

    # Tengely címkék és ábra cím hozzáadása
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')
    ax.set_title('Goals and Shots on target')

    return fig

#15
def scatter_goals_shots_by_quartile(input_df: pd.DataFrame) -> plt.Figure:
    """
    Scatter plot-ot készít a gólok és a kaput ért találatok kapcsolatáról különböző kvartilisekkel és jelmagyarázattal az input_df DataFrame alapján.

    Parameters:
    input_df (pd.DataFrame): A bemeneti DataFrame, amely tartalmazza az adatokat.

    Returns:
    plt.Figure: A matplotlib ábra objektuma.
    """
    # Ellenőrizze, hogy az input DataFrame tartalmazza-e a megfelelő oszlopokat
    required_columns = ['Goals', 'Shots on target', 'Quartile']
    for col in required_columns:
        if col not in input_df.columns:
            raise ValueError(f'A "{col}" oszlop nem található a DataFrame-ben.')

    # Scatter plot létrehozása kvartilisekkel
    fig, ax = plt.subplots()
    scatter = ax.scatter(input_df['Goals'], input_df['Shots on target'], c=input_df['Quartile'], cmap='viridis')

    # Tengely címkék és ábra cím hozzáadása
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')
    ax.set_title('Goals and Shots on target')

    # Jelmagyarázat hozzáadása
    legend = ax.legend(*scatter.legend_elements(), title='Quartiles')
    ax.add_artist(legend)

    return fig

#16
from src.distributions import ParetoDistribution
import matplotlib.pyplot as plt
import random


def gen_pareto_mean_trajectories(pareto_distribution: ParetoDistribution, number_of_trajectories: int,
                                 length_of_trajectory: int) -> List[List[float]]:
    """
    Generál number_of_trajectories számú belső listát, amelyek kumulatív átlagát tartalmazzák a Pareto eloszlás alapján.

    Parameters:
    pareto_distribution (ParetoDistribution): A Pareto eloszlás osztály, amelyet felhasználunk a véletlen számok generálásához.
    number_of_trajectories (int): A generált belső listák száma.
    length_of_trajectory (int): Minden belső lista hossza.

    Returns:
    List[List[float]]: Egy lista belső listákkal, amelyek a generált számok kumulatív átlagát tartalmazzák.
    """
    # Állítsa be a seed-et
    random.seed(42)

    # Generálja a belső listákat
    trajectories = []
    for _ in range(number_of_trajectories):
        # Generálja a véletlen számokat a Pareto eloszlás alapján
        random_numbers = [pareto_distribution.sample() for _ in range(length_of_trajectory)]

        # Számolja ki a kumulatív átlagokat
        cumulative_means = [sum(random_numbers[:i + 1]) / (i + 1) for i in range(length_of_trajectory)]

        # Adjuk hozzá a belső listát a trajectories listához
        trajectories.append(cumulative_means)

    return trajectories

