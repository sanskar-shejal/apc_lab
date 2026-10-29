import os
import pandas as pd


def main():
    try:
        print("Pandas Series with Custom Labels:")
        series_data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
        print(series_data)
        print("Value at index 'C':", series_data['C'])

        print("\nPandas DataFrame from Dictionary:")
        student_data = {
            'RollNo': [101, 102, 103, 104],
            'Name': ['Viraj', 'Raj', 'Rahul', 'Sneha'],
            'Marks': [85, 92, 78, 88],
            'Branch': ['CSE', 'IT', 'CSE', 'ENTC']
        }
        df = pd.DataFrame(student_data)
        print(df)

        print("\nSummary Statistics:\n", df.describe())
        print("\nFiltered (Marks > 80):\n", df[df['Marks'] > 80])

        sample_csv = "temp_students.csv"
        df.to_csv(sample_csv, index=False)
        print(f"\nSaved DataFrame to '{sample_csv}' and reading it back:")
        df_from_csv = pd.read_csv(sample_csv)
        print(df_from_csv)

        if os.path.exists(sample_csv):
            os.remove(sample_csv)

    except ImportError:
        print("Pandas is not installed. Run 'pip install pandas' to test this section.")


if __name__ == "__main__":
    main()
