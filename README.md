# Multithreading-in-Python


## Description

This Python script demonstrates concurrent execution using the `threading` module. Two threads run in parallel: one prints numbers (0-4) with a 2-second delay between each print, and the other prints letters (a-e) with a 3-second delay. The total execution time is measured and displayed at the end.

## Features

- **Multithreading**: Uses two threads to run tasks concurrently.
- **Synchronized Delays**: Each thread has a specific delay (2 seconds for numbers, 3 seconds for letters).
- **Execution Time Measurement**: Calculates and prints the total time taken for both threads to complete.

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. Save the code to a file (e.g., `thread_demo.py`).
2. Run the script in a terminal:
   ```bash
   python thread_demo.py
   ```

## Code Explanation

### Functions
- `print_numbers()`:  
  Prints numbers 0 to 4 with a 2-second delay between each print.
- `print_letters()`:  
  Prints letters 'a' to 'e' with a 3-second delay between each print.

### Threads
- **Thread 1 (`t1`)**: Executes `print_numbers()`.
- **Thread 2 (`t2`)**: Executes `print_letters()`.

### Execution Flow
1. Both threads start simultaneously.
2. The main thread waits for `t1` and `t2` to finish using `join()`.
3. The total execution time is calculated and printed.

## Output Explanation

### Example Output
```
Number:0
Letter:a
Number:1
Number:2
Letter:b
Number:3
Letter:c
Number:4
Letter:d
Letter:e
Finished in: 15.02 seconds
```

### Key Observations
- **Interleaved Output**: Due to concurrent execution, numbers and letters appear in a non-sequential order. The exact sequence depends on thread scheduling.
- **Total Time**: The script completes in approximately **15 seconds** (dictated by the slower thread, `print_letters`, which takes `5 iterations × 3 seconds = 15 seconds`). The faster thread (`print_numbers`) finishes earlier but does not block the main thread.

## Time Calculation

- **`print_numbers`** finishes in `5 iterations × 2 seconds = 10 seconds`.
- **`print_letters`** finishes in `5 iterations × 3 seconds = 15 seconds`.
- **Total Time**: Determined by the slower thread (`print_letters`), so the script completes in **~15 seconds**.

## Concurrency Note

This script illustrates how threads allow overlapping execution. While the slower thread (`print_letters`) is sleeping, the faster thread (`print_numbers`) continues its work, optimizing overall runtime.
