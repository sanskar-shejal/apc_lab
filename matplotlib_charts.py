import matplotlib.pyplot as plt


def main(show_plots=False):
    try:
        students = ["A", "B", "C", "D", "E"]
        marks = [75, 85, 60, 90, 70]

        print("Dataset -> Students:", students, "| Marks:", marks)

        plt.figure(figsize=(6, 4))
        plt.plot(students, marks, marker='o', color='b', linestyle='-', linewidth=2)
        plt.title("Student Marks - Line Graph")
        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.grid(True, linestyle='--', alpha=0.6)
        if show_plots:
            plt.show()
        plt.close()
        print("Line Graph generated.")

        plt.figure(figsize=(6, 4))
        plt.bar(students, marks, color=['#4285F4', '#EA4335', '#FBBC05', '#34A853', '#9C27B0'])
        plt.title("Student Marks - Bar Chart")
        plt.xlabel("Students")
        plt.ylabel("Marks")
        if show_plots:
            plt.show()
        plt.close()
        print("Bar Chart generated.")

        plt.figure(figsize=(6, 4))
        plt.scatter(students, marks, color='red', s=100, edgecolors='black')
        plt.title("Student Marks - Scatter Plot")
        plt.xlabel("Students")
        plt.ylabel("Marks")
        if show_plots:
            plt.show()
        plt.close()
        print("Scatter Plot generated.")

        plt.figure(figsize=(6, 4))
        plt.hist(marks, bins=5, color='teal', edgecolor='black', alpha=0.7)
        plt.title("Marks Distribution - Histogram")
        plt.xlabel("Marks Range")
        plt.ylabel("Frequency")
        if show_plots:
            plt.show()
        plt.close()
        print("Histogram generated.")

        plt.figure(figsize=(5, 5))
        plt.pie(marks, labels=students, autopct='%1.1f%%', startangle=140,
                colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#D1C4E9'])
        plt.title("Marks Share - Pie Chart")
        if show_plots:
            plt.show()
        plt.close()
        print("Pie Chart generated.")
        print("Note: To visually display plot windows, call main(show_plots=True)")

    except ImportError:
        print("Matplotlib is not installed. Run 'pip install matplotlib' to test this section.")


if __name__ == "__main__":
    main(show_plots=False)
