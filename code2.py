import numpy as np
import matplotlib.pyplot as plt

def f(n):
    """
    For a given n, this function iterates through starting points j (from 2 to n-1).
    For each j, it applies a transformation rule to a variable k (initially j)
    and counts the steps (m) until k returns to j. It returns a list of these
    cycle lengths.
    """
    cycle_lengths = []
    # We must iterate through all possible starting points j from 2 up to n-1.
    for j in range(2, n):
        k = j
        # Add a safeguard for sequences that might not terminate quickly
        max_steps = 10000
        for m in range(1, max_steps + 1):
            if k % 2 != 0:  # If k is odd
                k = (k + 1) / 2
            else:  # If k is even
                k = (n + k) / 2

            # The sequence can produce non-integer values if n is odd.
            # We must ensure k is an integer for the % operator to work in the next iteration.
            k = int(k)

            if k == j:
                cycle_lengths.append(m)
                break
        else: # This 'else' belongs to the 'for' loop; it runs if the loop finishes without a 'break'
            # This indicates the cycle was not found within max_steps. We mark it as invalid.
            cycle_lengths.append(-1)
            
    return cycle_lengths

def find_special_n(max_n_to_check):
    """
    Tests all values of n from 3 up to max_n_to_check to find the ones
    where all starting points j have the same cycle length.
    """
    print(f"Searching for special 'n' values up to {max_n_to_check}...")
    special_n_values = []
    for n in range(3, max_n_to_check + 1):
        # Get the list of cycle lengths for this n
        lengths = f(n)

        # --- FIXED LOGIC ---
        # Check that the list has at least 2 elements (to avoid trivial cases like n=3)
        # and that all elements in the list are the same.
        if len(lengths) > 1 and lengths.count(lengths[0]) == len(lengths):
            # Also check that no cycle failed to terminate (marked as -1)
            if lengths[0] != -1:
                print(f"--> Found a special value: n = {n}. All cycles have a length of {lengths[0]}.")
                special_n_values.append(n)

    if not special_n_values:
        print("\nNo special 'n' values found in the checked range.")
    else:
        print(f"\nSummary: The special 'n' values found are: {special_n_values}")

    return special_n_values

# --- Run the search ---
# We will check for n up to a reasonable limit, e.g., 200
special_ns = find_special_n(200)

# --- Optional: Plot the results for a special n to visualize it ---
if special_ns:
    # Use the first special n we found for the plot
    n_to_plot = special_ns[0]
    y = f(n_to_plot)
    x = range(2, n_to_plot)
    
    # Use a non-interactive backend to reliably save the plot to a file
    plt.switch_backend('Agg')
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, 'o-', label=f"Cycle Length (all are {y[0]})")
    ax.set_title(f"Cycle Lengths for the Special Case n = {n_to_plot}")
    ax.set_xlabel("Starting Number 'j'")
    ax.set_ylabel("Cycle Length 'm'")
    ax.legend()
    ax.grid(True)
    
    # Save the figure to a file instead of trying to show it interactively
    fig.savefig("special_n_plot.png")
    print("\nPlot for the first special n has been saved as 'special_n_plot.png'")

