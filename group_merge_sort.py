# Name: Konstantinos Vardakas 
# AM: 522

from utils import read_tsv
import sys

def merge_sort(data):
    """Εφαρμόζει το merge-sort στην είσοδο δεδομένων."""
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)
    
def merge(left, right):
    """Συγχωνεύει δύο ταξινομημένα υποσύνολα (left, right) βάσει του πρώτου πεδίου (key) και επιστρέφει λίστα."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append((left[i][0], left[i][1]))
            i += 1
        elif left[i][0] > right[j][0]:
            result.append((right[j][0], right[j][1]))
            j += 1
        else:
            result.append((left[i][0], left[i][1] + right[j][1]))
            i += 1
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def group_merge_sort(filename, output_file="Rgroupby.tsv"):
    """Ομαδοποιεί και συγχωνεύει τις εγγραφές του αρχείου εισόδου."""
    data = read_tsv(filename)
    sorted_data = merge_sort(data)
    with open(output_file, "w") as f:
        for key, value in sorted_data:
            f.write(f"{key}\t{value}\n")

def main():
    """Handles command-line arguments."""
    args = sys.argv[1:]  # command-line arguments

    if len(args) < 1 or len(args) > 2:
        print("Usage: python intersection_sorted.py <R_file> [output_file]")
        sys.exit(1)

    if not all(arg.endswith(".tsv") for arg in args):
        print("Error: All filenames must have a '.tsv' extension")
        sys.exit(1)

    group_merge_sort(*args)

if __name__ == "__main__":
    main()