# Name: Konstantinos Vardakas 
# AM: 522

def read_tsv_line(filename):
    """Generator που διαβάζει τις γραμμές ενός αρχείου TSV μία-μία."""
    with open(filename, "r") as f:
        for line in f:
            # Δεδομένης της μορφής κάθε Α\tB
            # Αλλιώς Α, *Β = line.strip().split('\t') και return A, *B για διάβασμα αρχείων όπως RjoinS
            A, B = line.strip().split('\t')
            yield A, int(B)


def read_tsv(filename):
    """Διαβάζει το αρχείο TSV και επιστρέφει μια λίστα από πλειάδες."""
    with open(filename, "r") as f:
        data = [line.strip().split('\t') for line in f.readlines()]
    return [(x[0], int(x[1])) for x in data]