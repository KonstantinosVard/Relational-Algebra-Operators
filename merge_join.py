# Name: Konstantinos Vardakas 
# AM: 522

from utils import read_tsv_line
import sys

def merge_join(R_file, S_file, output_file="RjoinS.tsv"):
    """Υλοποίηση του Merge-Join μεταξύ δύο ταξινομημένων αρχείων."""
    # Αρχικοποίηση των generator
    R = read_tsv_line(R_file)
    S = read_tsv_line(S_file)

    # Αρχικοποίηση του output file
    with open(output_file, 'w') as f: 
        pass 
    
    # Αρχικοποίηση των σειρών που συγκρίνονται
    r = next(R, None)
    s = next(S, None)
    max_buffer_size = 0
    with open(output_file, "a") as f:
        while r and s:
            if r[0] < s[0]:
                r = next(R, None)  # Προχωράμε τον δείκτη του R
            elif r[0] > s[0]:
                s = next(S, None)  # Προχωράμε τον δείκτη του S
            else:  # r[0] == s[0]
                # Γεμίζουμε τον buffer με όλες τις γραμμές του S που ταιριάζουν με το r[0]
                buffer = []
                key = s[0]
                while s and s[0] == key:
                    buffer.append(s)
                    s = next(S, None)
                
                # Υπολογίζουμε το μέγιστο μέγεθος του buffer
                max_buffer_size = max(max_buffer_size, len(buffer))
                
                # Κάνουμε το Join για όλες τις πλειάδες του R που έχουν την ίδια τιμή με τον buffer
                while r and r[0] == key:
                    for b in buffer:
                        # Χωρίς αποθήκευση λίστας
                        f.write(f"{r[0]}\t{r[1]}\t{b[1]}\n")
                    r = next(R, None)
    
    print("Max buffer size:", max_buffer_size)


def main():
    """Handles command-line arguments."""
    args = sys.argv[1:]  # command-line arguments

    if len(args) < 2 or len(args) > 3:
        print("Usage: python merge_join.py <R_file> <S_file> [output_file]")
        sys.exit(1)

    if not all(arg.endswith(".tsv") for arg in args):
        print("Error: All filenames must have a '.tsv' extension")
        sys.exit(1)

    merge_join(*args)

if __name__ == "__main__":
    main()
