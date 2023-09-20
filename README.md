# IDS706_Python_Week3
Certainly! Here's a README for your project based on the provided details:

---

# Grade Analysis Tool

This project offers tools to analyze students' grades from a dataset. Leveraging the power of the `polars` library, we can derive insightful statistical measures such as the mean, median, and standard deviation of the grades. Additionally, we provide a simple histogram visualization to visually understand the grade distribution.

## Files:

1. **lib.py** 
   - Contains core functions to compute:
     - Median of grades
     - Mean of grades
     - Standard deviation of grades

2. **main.ipynb**
   - Jupyter notebook showcasing:
     - Import and utilization of the functions from `lib.py`
     - Visualization of the grades distribution as a histogram.
     - A concise report outputting the mean, median, and standard deviation.

3. **test_main.ipynb**
   - A Jupyter notebook dedicated to:
     - Testing the correctness of the `mean` function from `lib.py` against a known value.
   
4. **test.csv**
   - A dataset containing:
     - Student ID
     - Student Name
     - Grade (out of 100)
   - Contains records for 50 students.

## Setup and Usage:

### Prerequisites:
- Ensure you have Python 3 installed.
- Required libraries: `polars`, `matplotlib`. Install them using pip:
  ```
  pip install polars matplotlib
  ```

### Running the Analysis:

1. Clone the repository.
2. Navigate to the project directory.
3. Open and run `main.ipynb` using Jupyter Notebook or Jupyter Lab for a comprehensive analysis and visualization.
4. For testing the correctness of the `mean` function, open and run `test_main.ipynb`.

## Contributing:

Contributions are welcome! If you have suggestions, improvements, or spot any discrepancies, please submit a pull request or open an issue.

## License:
