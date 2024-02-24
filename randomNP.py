import numpy as np

# Set seed for reproducibility .ie, every thime it gernerates the same number 
np.random.seed(42)

# Generate a random array of shape (3, 3) from a standard normal distribution
random_array = np.random.randn(3, 3)
print("Random Array (Normal Distribution):\n", random_array)

# Generate a random array of shape (3, 3) from a uniform distribution over [0, 1)
uniform_array = np.random.rand(3, 3)
print("\nRandom Array (Uniform Distribution):\n", uniform_array)

# Generate a random integer between 0 and 9
random_int = np.random.randint(0, 10)
print("\nRandom Integer:", random_int)

# Shuffle a sequence
sequence = [1, 2, 3, 4, 5]
#permutation function return the new shuffled array
permuted_arr = np.random.permutation(sequence)
print("Permuted array (new array):", permuted_arr)

print('original sequence',sequence)
#shuffle function shuffle with in the list or array
np.random.shuffle(sequence)
print("\nShuffled Sequence:", sequence)
