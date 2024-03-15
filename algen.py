import random
import streamlit as st

st.title(""" BAHAN MAKANAN UNTUK MPASI """)
st.image("baby.png", output_format="auto")


# Table data for each nutrient category
table_data_karbohidrat = [
    ["No", "Makanan", "Karbohidrat (g)", "Kalori (kcal)"],
    [1, "Pisang", 23, 89],
    [2, "Roti Gandum", 49.5, 265],
    [3, "Kentang", 17, 77],
    [4, "Quinoa", 21.3, 120],
    [5, "Kentang Manis", 20.1, 86],
    [6, "Bubur Bayi (Beras Merah)", 20, 70],
    [7, "Apel", 19, 95],
    [8, "Pasta", 25, 131],
    [9, "Labu", 7, 30],
    [10, "Ubi Jalar", 26, 112],
    [11, "Jeruk", 21, 62],
    [12, "Sereal Sarapan", 26, 117],
    [13, "Melon", 12, 50],
    [14, "Kacang Merah", 24, 130],
    [15, "Beras Merah", 45, 215],
]

table_data_protein = [
    ["No", "Makanan", "Protein (g)", "Kalori (kcal)"],
    [1, "Ayam Dada Tanpa Kulit", 31.2, 135],
    [2, "Daging Sapi (tanpa lemak)", 26.1, 143],
    [3, "Ikan Salmon", 22, 206],
    [4, "Tempe", 19.2, 192],
    [5, "Telur", 13, 155],
    [6, "Tahu", 16, 144],
    [7, "Kacang Hijau", 7, 105],
    [8, "Yogurt", 10, 150],
    [9, "Susu Kedelai", 8, 80],
    [10, "Keju Cottage", 14, 98],
    [11, "Brokoli", 3, 55],
    [12, "Ikan Teri", 19, 132],
    [13, "Daging Ayam Organik", 20, 165],
    [14, "Lentil", 18, 230],
    [15, "Kacang Panjang", 4, 35],
]

table_data_lemak = [
    ["No", "Makanan", "Lemak (g)", "Kalori (kcal)"],
    [1, "Kacang Almond", 49.9, 579],
    [2, "Keju Cheddar", 33.1, 403],
    [3, "Peanut Butter", 50, 588],
    [4, "Coconut Milk", 33, 552],
    [5, "Alpukat", 14.7, 85],
    [6, "Minyak Zaitun", 13.5, 119],
    [7, "Telur Asin", 5, 68],
    [8, "Biskuit Almond", 20, 120],
    [9, "Kacang Tanah", 49, 567],
    [10, "Salmon", 13, 206],
    [11, "Susu Kental Manis", 8, 94],
    [12, "Bibit Kedelai", 15, 120],
    [13, "Mentega", 11, 100],
    [14, "Avocado Oil", 14, 120],
    [15, "Ikan Tuna", 8, 191],
]

# Define the range for the average weight for toddlers (example: 2 kg - 15 kg)
min_baby_weight = 2.0
max_baby_weight = 15.0
min_baby_age = 6.0
max_baby_age = 24.0

# Create the form using Streamlit components
st.title("Informasi tentang Baby")

# Input fields in the form
baby_name = st.text_input("Nama Baby:")
baby_age = st.number_input("Usia Baby (bulan):", min_value=min_baby_age, max_value=max_baby_age)
baby_weight = st.number_input("Berat Badan Baby (kg):", min_value=min_baby_weight, max_value=max_baby_weight)

# Calculate nutritional requirements based on the valid baby weight
if st.button('SAVE'):
    kalori_needed = 100 * baby_weight
    karbohidrat_needed = 0.5 * kalori_needed
    protein_needed = 0.2 * kalori_needed
    lemak_needed = 0.3 * kalori_needed

    # Display the results based on input 
    st.write(f"Nutrisi yang dibutuhkan baby {baby_name} dengan Usia {baby_age} dan Berat Badan {baby_weight}")
    st.write(f"Kalori : {kalori_needed} kcal/hari")
    st.write(f"Krbohidrat : {karbohidrat_needed} g")
    st.write(f"Protein : {protein_needed} g")
    st.write(f"Lemak : {lemak_needed} g")

# Create a class to represent an individual in the population
    class Individu:
        def __init__(self, karbohidrat, protein, lemak, karbohidrat_needed, protein_needed, lemak_needed):
            self.karbohidrat = karbohidrat
            self.protein = protein
            self.lemak = lemak
            self.karbohidrat_needed = karbohidrat_needed
            self.protein_needed = protein_needed
            self.lemak_needed = lemak_needed
            self.fitness = self.calculate_fitness()

        def calculate_fitness(self):
            penalti = abs(self.karbohidrat_needed - self.karbohidrat) + \
                    abs(self.protein_needed - self.protein) + \
                    abs(self.lemak_needed - self.lemak)
            return 100 / (1 + penalti)

    # Inisialisasi populasi
    population_size = 10
    population = []

    # Nilai acak untuk individu
    karbohidrat_value = random.randint(1, 100)
    protein_value = random.randint(1, 100)
    lemak_value = random.randint(1, 100)

    # Membuat objek Individu
    individu = Individu(karbohidrat_value, protein_value, lemak_value, karbohidrat_needed, protein_needed, lemak_needed)

    # Genetic Algorithm
    def crossover(parent1, parent2):
        # crossover_point = random.randint(1, 2)  # 1-point crossover
        child1 = Individu(parent1.karbohidrat, parent1.protein, parent1.lemak, parent1.karbohidrat_needed, parent1.protein_needed, parent1.lemak_needed)
        child2 = Individu(parent2.karbohidrat, parent2.protein, parent2.lemak, parent2.karbohidrat_needed, parent2.protein_needed, parent2.lemak_needed)

        return child1, child2

    def mutate(individu):
        mutation_prob = 0.1  # 10% mutation probability
        if random.random() < mutation_prob:
            individu.karbohidrat = random.randint(1, 15)
        if random.random() < mutation_prob:
            individu.protein = random.randint(1, 15)
        if random.random() < mutation_prob:
            individu.lemak = random.randint(1, 15)

    def print_meal_info(individual, table_data_karbohidrat, table_data_protein, table_data_lemak):
        karbohidrat_info = table_data_karbohidrat[individual.karbohidrat]
        protein_info = table_data_protein[individual.protein]
        lemak_info = table_data_lemak[individual.lemak]
        jumlah = lemak_info[3]+karbohidrat_info[3]+protein_info[3]

        table_hasil = [
                    ["Makanan", "Amount (g)", "Kalori (kcal)"],
                    [karbohidrat_info[1], karbohidrat_info[2], karbohidrat_info[3]],
                    [protein_info[1], protein_info[2], protein_info[3]],
                    [lemak_info[1], lemak_info[2], lemak_info[3]]]
        st.write(f"Total Kalori : {jumlah} kcal")
        st.table(table_hasil)



    tab1, tab2, tab3 = st.tabs(["Pilihan 1", "Pilihan 2", "Pilihan 3"])

    with tab1:
        num_plans = 3

        # Run the genetic algorithm multiple times
        for plan_num in range(1, num_plans + 1):

            # Initial population
            population_size = 10
            population = [Individu(random.randint(1,15), random.randint(1, 15), random.randint(1, 15), karbohidrat_needed, protein_needed, lemak_needed) for _ in range(population_size)]

            # Genetic Algorithm iterations
            generations = 1000
            for generation in range(generations):
                # Calculate fitness values
                for individu in population:
                    individu.fitness = individu.calculate_fitness()

                # Roulette Wheel Selection
                total_fitness = sum(individu.fitness for individu in population)
                probabilities = [individu.fitness / total_fitness for individu in population]
                selected_indices = random.choices(range(population_size), weights=probabilities, k=2)
                selected_parents = [population[i] for i in selected_indices]

                # Crossover
                if random.random() < 0.6:
                    child1, child2 = crossover(selected_parents[0], selected_parents[1])
                    population.extend([child1, child2])

                # Mutation
                for individu in population:
                    mutate(individu)

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

            # Initialize meal compositions for morning, noon, and night
            morning_meal = []
            noon_meal = []
            night_meal = []

            # Store the best individuals for each mealtime
            best_morning_list = []
            best_noon_list = []
            best_night_list = []

            # Genetic Algorithm iterations
            for generation in range(generations):

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

                # Store the best individual for each mealtime
                best_morning_list.append(population[0])
                best_noon_list.append(population[1])
                best_night_list.append(population[2])

            
            # Display the results for each mealtime
            st.title(f"\nKomposisi Makanan Hari ke-{plan_num}:")

            # Pagi
            for i in range(1, population_size, 3):
                st.header("Bahan Makanan Pagi")
                print_meal_info(best_morning_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Siang
            for i in range(2, population_size, 3):
                st.header("Bahan Makanan Siang")
                print_meal_info(best_noon_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Malam
            for i in range(3, population_size, 3):
                st.header("Bahan Makanan Malam")
                print_meal_info(best_night_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

    with tab2:
        num_plans = 3

        # Run the genetic algorithm multiple times
        for plan_num in range(1, num_plans + 1):

            # Initial population
            population_size = 10
            population = [Individu(random.randint(1,15), random.randint(1, 15), random.randint(1, 15), karbohidrat_needed, protein_needed, lemak_needed) for _ in range(population_size)]

            # Genetic Algorithm iterations
            generations = 1000
            for generation in range(generations):
                # Calculate fitness values
                for individu in population:
                    individu.fitness = individu.calculate_fitness()

                # Roulette Wheel Selection
                total_fitness = sum(individu.fitness for individu in population)
                probabilities = [individu.fitness / total_fitness for individu in population]
                selected_indices = random.choices(range(population_size), weights=probabilities, k=2)
                selected_parents = [population[i] for i in selected_indices]

                # Crossover
                if random.random() < 0.6:
                    child1, child2 = crossover(selected_parents[0], selected_parents[1])
                    population.extend([child1, child2])

                # Mutation
                for individu in population:
                    mutate(individu)

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

            # Initialize meal compositions for morning, noon, and night
            morning_meal = []
            noon_meal = []
            night_meal = []

            # Store the best individuals for each mealtime
            best_morning_list = []
            best_noon_list = []
            best_night_list = []

            # Genetic Algorithm iterations
            for generation in range(generations):

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

                # Store the best individual for each mealtime
                best_morning_list.append(population[0])
                best_noon_list.append(population[1])
                best_night_list.append(population[2])

            
            # Display the results for each mealtime
            st.title(f"\nKomposisi Makanan Hari ke-{plan_num}:")

            # Pagi
            for i in range(1, population_size, 3):
                st.header("Bahan Makanan Pagi")
                print_meal_info(best_morning_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Siang
            for i in range(2, population_size, 3):
                st.header("Bahan Makanan Siang")
                print_meal_info(best_noon_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Malam
            for i in range(3, population_size, 3):
                st.header("Bahan Makanan Malam")
                print_meal_info(best_night_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

    with tab3:
        num_plans = 3

        # Run the genetic algorithm multiple times
        for plan_num in range(1, num_plans + 1):

            # Initial population
            population_size = 10
            population = [Individu(random.randint(1,15), random.randint(1, 15), random.randint(1, 15), karbohidrat_needed, protein_needed, lemak_needed) for _ in range(population_size)]

            # Genetic Algorithm iterations
            generations = 1000
            for generation in range(generations):
                # Calculate fitness values
                for individu in population:
                    individu.fitness = individu.calculate_fitness()

                # Roulette Wheel Selection
                total_fitness = sum(individu.fitness for individu in population)
                probabilities = [individu.fitness / total_fitness for individu in population]
                selected_indices = random.choices(range(population_size), weights=probabilities, k=2)
                selected_parents = [population[i] for i in selected_indices]

                # Crossover
                if random.random() < 0.6:
                    child1, child2 = crossover(selected_parents[0], selected_parents[1])
                    population.extend([child1, child2])

                # Mutation
                for individu in population:
                    mutate(individu)

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

            # Initialize meal compositions for morning, noon, and night
            morning_meal = []
            noon_meal = []
            night_meal = []

            # Store the best individuals for each mealtime
            best_morning_list = []
            best_noon_list = []
            best_night_list = []

            # Genetic Algorithm iterations
            for generation in range(generations):

                # Select the fittest individuals for the next generation
                population = sorted(population, key=lambda x: x.fitness, reverse=True)[:population_size]

                # Store the best individual for each mealtime
                best_morning_list.append(population[0])
                best_noon_list.append(population[1])
                best_night_list.append(population[2])

            
            # Display the results for each mealtime
            st.title(f"\nKomposisi Makanan Hari ke-{plan_num}:")

            # Pagi
            for i in range(1, population_size, 3):
                st.header("Bahan Makanan Pagi")
                print_meal_info(best_morning_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Siang
            for i in range(2, population_size, 3):
                st.header("Bahan Makanan Siang")
                print_meal_info(best_noon_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break

            # Malam
            for i in range(3, population_size, 3):
                st.header("Bahan Makanan Malam")
                print_meal_info(best_night_list[i], table_data_karbohidrat, table_data_protein, table_data_lemak)
                break
