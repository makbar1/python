import random

# Input string
input_str = "4CkP8f6KlN9{Mz!Gr?g_QTi3lcFtFw$(jRGVuih%mMRbXQ3{_yYxB}cy=nJmD(PrP@t[CVem3CR4zsB{RyC0FKREwIxwzqnvuuhl"

# Fixed prefix and suffix
fixed_prefix = "CTF{"
fixed_suffix = "}"

# Extract the core part between CTF{ and }
core_str = input_str.replace(fixed_prefix, "").replace(fixed_suffix, "")

# Function to generate a shuffled string
def generate_shuffled_string(core, prefix, suffix):
    # Convert the core string to a list of characters, shuffle it, and join it back
    core_list = list(core)
    random.shuffle(core_list)
    return prefix + "".join(core_list) + suffix

# Generate a set of unique shuffled strings
num_variations = 100  # Number of different permutations to generate
generated_permutations = set()

while len(generated_permutations) < num_variations:
    # Generate a new shuffled string
    shuffled_string = generate_shuffled_string(core_str, fixed_prefix, fixed_suffix)
    
    # Add the new permutation to the set (automatically avoids duplicates)
    generated_permutations.add(shuffled_string)

# Print the unique shuffled strings
for perm in generated_permutations:
    print(perm)
