import random

# Konstanta
TARGET = "GA JAGO"  # Kata target yang dicari
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "  # Alfabet termasuk spasi
CHROMOSOME_LENGTH = len(TARGET)  # Panjang kromosom
POP_SIZE = 6  # Ukuran populasi
MAX_GENERATIONS = 1000  # Maksimum jumlah generasi
MUTATION_RATE = 0.1  # Tingkat mutasi

# Fungsi fitness untuk mengukur seberapa dekat individu dengan kata target
def fitness(chromosome):
    return sum(1 for i in range(CHROMOSOME_LENGTH) if chromosome[i] == TARGET[i])

# Fungsi untuk membuat kromosom acak
def create_chromosome():
    return ''.join(random.choice(ALPHABET) for _ in range(CHROMOSOME_LENGTH))

# Fungsi untuk membuat populasi awal
def create_population():
    return [create_chromosome() for _ in range(POP_SIZE)]

# Fungsi untuk melakukan crossover antara dua individu
def crossover(parent1, parent2):
    # Pilih titik potong acak
    crossover_point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Fungsi untuk melakukan mutasi pada individu
def mutate(chromosome):
    mutated_chromosome = list(chromosome)
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:  # Jika mutasi terjadi pada posisi ini
            mutated_chromosome[i] = random.choice(ALPHABET)  # Ganti dengan huruf acak
    return ''.join(mutated_chromosome)

# Fungsi utama untuk menjalankan algoritma genetika
def genetic_algorithm():
    population = create_population()  # Membuat populasi awal
    generation = 0  # Inisialisasi generasi
    
    while generation < MAX_GENERATIONS:
        # Evaluasi fitness setiap individu dalam populasi
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        
        # Jika individu pertama sudah cocok dengan target, selesai
        if fitness(population[0]) == CHROMOSOME_LENGTH:
            print(f"Solusi ditemukan pada generasi {generation}: {population[0]}")
            break
        
        # Seleksi: Pilih dua individu terbaik untuk crossover
        parent1 = population[0]
        parent2 = population[1]
        
        # Crossover: Membuat dua anak baru
        child1, child2 = crossover(parent1, parent2)
        
        # Mutasi: Menerapkan mutasi pada anak-anak baru
        child1 = mutate(child1)
        child2 = mutate(child2)
        
        # Membuat populasi baru dengan anak-anak dan individu terbaik
        population = population[:POP_SIZE//2]  # Ambil setengah dari populasi terbaik
        population.extend([child1, child2])  # Tambahkan anak-anak baru ke populasi
        
        generation += 1
        if generation % 100 == 0:
            print(f"Generasi {generation}: {population[0]}")

    # Jika kita tidak menemukan solusi dalam 1000 generasi
    if fitness(population[0]) != CHROMOSOME_LENGTH:
        print("Solusi tidak ditemukan setelah 1000 generasi.")

# Menjalankan algoritma genetika
genetic_algorithm()
