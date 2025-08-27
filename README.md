# Relational Algebra Operators Implementation
### MSc Data Science & Engineering · Complex Data Management · Project 1: Relational Algebra Operators

## Project Overview

This project implements fundamental relational algebra operators using Python, with a focus on efficient memory management and sorted file processing. The operators include Merge-Join, Union, Intersection, Set-Difference, and Grouping with Aggregation.

## Files Structure

### Source Code Files:
- **merge_join.py** - Implements the merge-join algorithm between two sorted files
- **union_sorted.py** - Performs union operation on two sorted files
- **intersection_sorted.py** - Computes intersection of two sorted files
- **difference_sorted.py** - Calculates set difference between two sorted files
- **group_merge_sort.py** - Performs grouping and aggregation using merge-sort
- **utils.py** - Utility functions for reading TSV files

### Input Data Files:
- **R.tsv** - Unsorted relation R
- **S.tsv** - Unsorted relation S
- **R_sorted.tsv** - Sorted relation R
- **S_sorted.tsv** - Sorted relation S

### Output Files (Generated):
- **RjoinS.tsv** - Result of merge-join operation
- **RunionS.tsv** - Result of union operation
- **RintersectionS.tsv** - Result of intersection operation
- **RdifferenceS.tsv** - Result of set-difference operation
- **Rgroupby.tsv** - Result of grouping and aggregation

## Data Format

All files use Tab-Separated Values (TSV) format with the following structure:
- Each row follows the pattern: `A\tB`
- Type(A) = string
- Type(B) = integer

## Implementation Features

### Memory Efficiency
- Uses generator functions to read files line-by-line
- Avoids loading entire files into memory
- Implements efficient buffer management for join operations

### Algorithmic Approach
- **Merge-Join**: Uses sorted files and buffer management for efficient joining
- **Set Operations**: Implements two-pointer technique for union, intersection, and difference
- **Grouping/Aggregation**: Adapts merge-sort algorithm to perform aggregation during merging

### Duplicate Handling
- All operations properly handle duplicate entries
- Uses `last_written` tracking to avoid writing duplicate results

## Installation and Requirements

**Requirements:**
- Python 3.x
- No external dependencies required

## Usage Instructions

### General Execution Pattern:
```bash
python {script_name}.py <input_file1.tsv> <input_file2.tsv> [output_file.tsv]
```

### Specific Commands:

1. **Merge-Join Operation:**
```bash
python merge_join.py R_sorted.tsv S_sorted.tsv RjoinS.tsv
```

2. **Union Operation:**
```bash
python union_sorted.py R_sorted.tsv S_sorted.tsv RunionS.tsv
```

3. **Intersection Operation:**
```bash
python intersection_sorted.py R_sorted.tsv S_sorted.tsv RintersectionS.tsv
```

4. **Set-Difference Operation:**
```bash
python difference_sorted.py R_sorted.tsv S_sorted.tsv RdifferenceS.tsv
```

5. **Grouping and Aggregation:**
```bash
python group_merge_sort.py R.tsv Rgroupby.tsv
```

### Notes:
- Input files must have `.tsv` extension
- Output file parameter is optional (default filenames will be used if omitted)
- For grouping operation, only one input file is required

## Key Features

- **Memory Efficient**: Processes large files without loading them entirely into memory
- **Sorted Input Handling**: Optimized for pre-sorted input files
- **Duplicate Elimination**: Properly handles and eliminates duplicate entries
- **Error Handling**: Includes basic command-line argument validation
- **Buffer Monitoring**: Tracks maximum buffer size used during join operations

## Performance Considerations

- The merge-join algorithm efficiently handles large datasets with O(n) complexity
- Set operations use optimized two-pointer technique for O(n) performance
- Grouping operation uses modified merge-sort with O(n log n) complexity
- All operations minimize disk I/O through efficient file handling

## Author

**Konstantinos Vardakas** 

*This implementation demonstrates the practical advantages of efficient memory management and algorithm optimization when processing large-scale relational data operations.*
