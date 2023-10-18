#gy7ejg

import pandas as pd
from pathlib import Path


#1
# Chipotle fájl elérési útja
file_to_load = Path.cwd().parent.joinpath('data').joinpath('chipotle.tsv')

# DataFrame létrehozása a chipotle.tsv fájlból
food = pd.read_csv(file_to_load, sep='\t')

#2
def change_price_to_float(input_df):
    # Másold le az eredeti adatokat, hogy ne módosítsuk azokat
    output_df = input_df.copy()

    # Az item_price oszlopban lévő értékeket konvertáljuk float típusra
    output_df['item_price'] = output_df['item_price'].replace('[\$,]', '', regex=True).astype(float)

    return output_df


#3
def number_of_observations(input_df):
    # Megszámoljuk az adatok számát
    count = len(input_df)
    return count

# Függvény hívása a 'food' DataFrame-mel
observations_count = number_of_observations(food)

#4
def items_and_prices(input_df):
    # Válogatjuk ki a 'item_name' és 'item_price' oszlopokat
    result_df = input_df[['item_name', 'item_price']]
    return result_df

# Függvény hívása a 'food' DataFrame-mel
items_prices_df = items_and_prices(food)

# Eredmény kiírása
print(items_prices_df)

#5
import pandas as pd

def sorted_by_price(input_df):
    # Használjuk az előző függvényt az 'item_name' és 'item_price' oszlopok kiválasztására
    items_prices_df = items_and_prices(input_df)

    # Sorba rendezzük az árak alapján csökkenő sorrendben
    sorted_df = items_prices_df.sort_values(by='item_price', ascending=False)

    return sorted_df

# Függvény hívása a 'food' DataFrame-mel
sorted_food = sorted_by_price(food)

# Eredmény kiírása
print(sorted_food)

#6
import pandas as pd

def avg_price(input_df):
    # Konvertáljuk az 'item_price' oszlopot float típusra
    input_df['item_price'] = input_df['item_price'].replace('[\$,]', '', regex=True).astype(float)

    # Számoljuk ki az átlagos árat
    average_price = input_df['item_price'].mean()

    return average_price

# Függvény hívása a 'food' DataFrame-mel
average_price = avg_price(food)

# Eredmény kiírása
print(f"Az átlagos ár: {average_price}")

#7
import pandas as pd

def unique_items_over_ten_dollars(input_df):
    # Konvertáljuk az 'item_price' oszlopot float típusra
    input_df['item_price'] = input_df['item_price'].replace('[\$,]', '', regex=True).astype(float)

    # Szűrjük az ár alapján
    filtered_df = input_df[input_df['item_price'] > 10]

    # Szűrjük az egyedi termékeket (név, feltét és ár alapján)
    unique_items_df = filtered_df.drop_duplicates(subset=['item_name', 'choice_description', 'item_price'])

    return unique_items_df

# Függvény hívása a 'food' DataFrame-mel
unique_items_over_ten_dollars_df = unique_items_over_ten_dollars(food)

# Eredmény kiírása
print(unique_items_over_ten_dollars_df)

#8
import pandas as pd

def items_starting_with_s(input_df):
    # Szűrjük azokat a termékeket, amelyek neve 'S'-el kezdődik
    filtered_df = input_df[input_df['item_name'].str.startswith('S', na=False)]

    return filtered_df

# Függvény hívása a 'food' DataFrame-mel
items_starting_with_s_df = items_starting_with_s(food)

# Eredmény kiírása
print(items_starting_with_s_df)

#9
def first_three_columns(input_df):
    # Az első 3 oszlop kiválasztása
    result_df = input_df.iloc[:, :3]

    return result_df


# Függvény hívása a 'food' DataFrame-mel
cleaned_food = change_price_to_float(food)  # Először tisztítsuk az adatokat
first_three_columns_df = first_three_columns(cleaned_food)

# Eredmény kiírása
print(first_three_columns_df)

#10
def every_column_except_last_two(input_df):
    # Az összes oszlop kiválasztása az utolsó két oszlopon kívül
    result_df = input_df.iloc[:, :-2]

    return result_df


# Függvény hívása a 'food' DataFrame-mel
cleaned_food = change_price_to_float(food)  # Először tisztítsuk az adatokat
every_column_except_last_two_df = every_column_except_last_two(cleaned_food)

# Eredmény kiírása
print(every_column_except_last_two_df)

#11
def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    # Kiválasztjuk a megadott oszlopokat
    selected_columns_df = input_df[columns_to_keep]

    # Szűrjük a sorokat a megadott oszlop alapján
    filtered_rows_df = selected_columns_df[selected_columns_df[column_to_filter].isin(rows_to_keep)]

    return filtered_rows_df

#12
def generate_quartile(input_df):
    # Másoljuk le az eredeti adatokat, hogy ne módosítsuk azokat
    result_df = input_df.copy()

    # Konvertáljuk az 'item_price' oszlopot float típusra
    result_df['item_price'] = result_df['item_price'].replace('[\$,]', '', regex=True).astype(float)

    # Definiáljuk a kvartilis kategóriákat
    quartile_bins = [0, 9.99, 19.99, 29.99, float('inf')]
    quartile_labels = ['low-cost', 'medium-cost', 'high-cost', 'premium']

    # Hozzáadjuk a 'Quartile' oszlopot az ár alapján
    result_df['Quartile'] = pd.cut(result_df['item_price'], bins=quartile_bins, labels=quartile_labels, include_lowest=True)

    return result_df

# Függvény hívása a 'food' DataFrame-mel
food_with_quartile = generate_quartile(food)

# Eredmény kiírása
print(food_with_quartile)

#13
def average_price_in_quartiles(input_df):
    # Csoportosítjuk a DataFrame-et a 'Quartile' oszlop alapján
    grouped_df = input_df.groupby('Quartile')

    # Kiszámoljuk az átlagos árat minden kvartilis értékhez
    avg_price_df = grouped_df['item_price'].mean().reset_index()

    return avg_price_df

# Függvény hívása a 'food_with_quartile' DataFrame-mel
average_prices = average_price_in_quartiles(food_with_quartile)

# Eredmény kiírása
print(average_prices)

#14
def minmaxmean_price_in_quartile(input_df):
    # Csoportosítjuk a DataFrame-et a 'Quartile' oszlop alapján
    grouped_df = input_df.groupby('Quartile')

    # Kiszámoljuk az árak minimális, maximális és átlagos értékét minden kvartilis esetén
    result_df = grouped_df['item_price'].agg(['min', 'max', 'mean']).reset_index()

    return result_df

# Függvény hívása a 'food_with_quartile' DataFrame-mel
minmaxmean_prices = minmaxmean_price_in_quartile(food_with_quartile)

# Eredmény kiírása
print(minmaxmean_prices)

#15
from random import seed, uniform

def gen_uniform_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    # Seed beállítása a reprodukálhatóság érdekében
    seed(42)

    # Az eredmény listája
    result = []

    for _ in range(number_of_trajectories):
        # Belső lista inicializálása
        trajectory = []

        # Kezdeti érték hozzáadása
        current_value = distribution()
        trajectory.append(current_value)

        # Trajektória generálása
        for _ in range(length_of_trajectory - 1):
            current_value += distribution()
            trajectory.append(current_value / (len(trajectory) + 1))

        # Belső lista hozzáadása az eredmény listához
        result.append(trajectory)

    return result


#16
from typing import List
import random
from src.utils import LogisticDistribution

def gen_logistic_mean_trajectories(distribution: LogisticDistribution,
                                    number_of_trajectories: int,
                                    length_of_trajectory: int) -> List[List[float]]:
    # Seed beállítása a reprodukálhatóság érdekében
    random.seed(42)

    # Az eredmény listája
    result = []

    for _ in range(number_of_trajectories):
        # Belső lista inicializálása
        trajectory = []

        # Kezdeti érték hozzáadása
        current_value = distribution.rvs()
        trajectory.append(current_value)

        # Trajektória generálása
        for _ in range(length_of_trajectory - 1):
            current_value += distribution.rvs()
            trajectory.append(current_value / (len(trajectory) + 1))

        # Belső lista hozzáadása az eredmény listához
        result.append(trajectory)

    return result

#17
from src.utils import LaplaceDistribution

def gen_laplace_mean_trajectories(distribution: LaplaceDistribution,
                                  number_of_trajectories: int,
                                  length_of_trajectory: int) -> List[List[float]]:
    # Seed beállítása a reprodukálhatóság érdekében
    random.seed(42)

    # Az eredmény listája
    result = []

    for _ in range(number_of_trajectories):
        # Belső lista inicializálása
        trajectory = []

        # Kezdeti érték hozzáadása
        current_value = distribution.rvs()
        trajectory.append(current_value)

        # Trajektória generálása
        for _ in range(length_of_trajectory - 1):
            current_value += distribution.rvs()
            trajectory.append(current_value / (len(trajectory) + 1))

        # Belső lista hozzáadása az eredmény listához
        result.append(trajectory)

    return result

#18
from typing import List
import random
from src.utils import CauchyDistribution

def gen_cauchy_mean_trajectories(distribution: CauchyDistribution,
                                  number_of_trajectories: int,
                                  length_of_trajectory: int) -> List[List[float]]:
    # Seed beállítása a reprodukálhatóság érdekében
    random.seed(42)

    # Az eredmény listája
    result = []

    for _ in range(number_of_trajectories):
        # Belső lista inicializálása
        trajectory = []

        # Kezdeti érték hozzáadása
        current_value = distribution.rvs()
        trajectory.append(current_value)

        # Trajektória generálása
        for _ in range(length_of_trajectory - 1):
            current_value += distribution.rvs()
            trajectory.append(current_value / (len(trajectory) + 1))

        # Belső lista hozzáadása az eredmény listához
        result.append(trajectory)

    return result

#19
from src.utils import ChiSquaredDistribution

def gen_chi2_mean_trajectories(distribution: ChiSquaredDistribution,
                               number_of_trajectories: int,
                               length_of_trajectory: int) -> List[List[float]]:
    # Seed beállítása a reprodukálhatóság érdekében
    random.seed(42)

    # Az eredmény listája
    result = []

    for _ in range(number_of_trajectories):
        # Belső lista inicializálása
        trajectory = []

        # Kezdeti érték hozzáadása
        current_value = distribution.rvs()
        trajectory.append(current_value)

        # Trajektória generálása
        for _ in range(length_of_trajectory - 1):
            current_value += distribution.rvs()
            trajectory.append(current_value / (len(trajectory) + 1))

        # Belső lista hozzáadása az eredmény listához
        result.append(trajectory)

    return result

