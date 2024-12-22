import itertools

# Input string
input_str = "4CkP8f6KlN9{Mz!Gr?g_QTi3lcFtFw$(jRGVuih%mMRbXQ3{_yYxB}cy=nJmD(PrP@t[CVem3CR4zsB{RyC0FKREwIxwzqnvuuhl"

# Remove any characters that should remain fixed (i.e., CTF{ and })
fixed_prefix = "CTF{"
fixed_suffix = "}"
core_str = input_str.replace(fixed_prefix, "").replace(fixed_suffix, "")

# Generate permutations (you can limit the number of permutations using itertools.islice if the number is too large)
permutations = itertools.permutations(core_str)

# Generate rearranged strings starting with CTF{ and ending with }
count = 0
for perm in permutations:
    result = fixed_prefix + "".join(perm) + fixed_suffix
    print(result)
    
    # Stop after a reasonable number of permutations (e.g., 10 or 1000) to avoid an enormous output
    count += 1
    if count >= 10:  # Change this to control how many permutations you want
        break
