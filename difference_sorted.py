# Name: Konstantinos Vardakas 
# AM: 522

from utils import read_tsv_line
import sys

def difference_sorted(R_file, S_file, output_file="RdifferenceS.tsv"):
    """Υλοποίηση της Διαφοράς μεταξύ δύο ταξινομημένων αρχείων."""
    R = read_tsv_line(R_file)
    S = read_tsv_line(S_file)

    # Δημιουργία νέου αρχείου (καθάρισμα περιεχομένων αν υπάρχει)
    with open(output_file, 'w') as f:
        pass

    # Αρχικοποίηση
    r = next(R, None)
    s = next(S, None)
    last_written = None

    # Άνοιγμα αρχείου εξόδου για αποθήκευση των αποτελεσμάτων
    with open(output_file, "a") as f:
        while r:
            if not s or r < s:
                if r != last_written:
                    f.write(f"{r[0]}\t{r[1]}\n")
                    last_written = r
                r = next(R, None)
            elif s < r:
                s = next(S, None)
            else:  # r == s
                r = next(R, None)
                s = next(S, None)

def main():
    """Handles command-line arguments."""
    args = sys.argv[1:]  # command-line arguments

    if len(args) < 2 or len(args) > 3:
        print("Usage: python difference_sorted.py <R_file> <S_file> [output_file]")
        sys.exit(1)

    if not all(arg.endswith(".tsv") for arg in args):
        print("Error: All filenames must have a '.tsv' extension")
        sys.exit(1)

    difference_sorted(*args)

if __name__ == "__main__":
    main()