import random

# Durasi kegiatan (dalam jam)
durasi = {
    'A': 2,
    'B': 3,
    'C': 2,
    'D': 4
}

# Syarat-syarat
TARGET_TOTAL_DURATION = 8
# A harus sebelum B
MUST_BEFORE = ('A', 'B')
# C dan D tidak boleh bersamaan
NO_CONCURRENT = ('C', 'D')

# Populasi dan parameter genetika
POP_SIZE = 6
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.1
CHROMOSOME_LENGTH = 4  # A, B, C, D

# Fungsi untuk membuat kromosom acak
def create_chromosome():
    return random.sample(['A', 'B', 'C', 'D'], CHROMOSOME_LENGTH)

# Fungsi untuk menghitung fitness (menghitung pelanggaran syarat)
def fitness(chromosome):
    score = 0
    
    # 1. A harus sebelum B
    if chromosome.index('A') > chromosome.index('B'):
        score -= 1
    
    # 2. C dan D tidak boleh bersamaan
    if 'C' in chromosome and 'D' in chromosome:
        if abs(chromosome.index('C') - chromosome.index('D')) == 1:
            score -= 1
    
    # 3. Durasi total tidak boleh melebihi 8 jam
    total_duration = sum(durasi[k] for k in chromosome)
    if total_duration > TARGET_TOTAL_DURATION:
        score -= 1
    
    return score

# Fungsi untuk membuat populasi awal
def create_population():
    return [create_chromosome() for _ in range(POP_SIZE)]

# Fungsi crossover
def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Fungsi mutasi
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(CHROMOSOME_LENGTH), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Fungsi utama algoritma genetika
def genetic_algorithm():
    population = create_population()  # Membuat populasi awal
    generation = 0

    while generation < MAX_GENERATIONS:
        # Evaluasi fitness dan urutkan populasi
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        
        # Jika individu pertama memenuhi semua syarat, selesai
        if fitness(population[0]) == 3:  # Fitness terbaik (nilai tertinggi)
            print(f"Solusi ditemukan pada generasi {generation}: {population[0]}")
            break
        
        # Seleksi dua individu terbaik untuk crossover
        parent1 = population[0]
        parent2 = population[1]
        
        # Crossover menghasilkan dua anak
        child1, child2 = crossover(parent1, parent2)
        
        # Mutasi anak-anak
        child1 = mutate(child1)
        child2 = mutate(child2)
        
        # Populasi baru
        population = population[:POP_SIZE//2]  # Seleksi setengah populasi terbaik
        population.extend([child1, child2])  # Menambahkan anak-anak baru
        
        generation += 1
        if generation % 100 == 0:
            print(f"Generasi {generation}: {population[0]}")

    # Jika solusi tidak ditemukan dalam 1000 generasi
    if fitness(population[0]) != 3:
        print("Solusi tidak ditemukan setelah 1000 generasi.")

# Menjalankan algoritma genetika
genetic_algorithm()
