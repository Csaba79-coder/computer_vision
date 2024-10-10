import pandas as pd

class DataTableOperation:
    def __init__(self):
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'Age': [25, 30, 35, 28, 22],
            'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
        }
        self.df = pd.DataFrame(data)
        self.display_table()
        self.filter_data()
        self.add_salary_column()
        self.rename_columns()
        self.summarize_data()

    def display_table(self):
        print("Eredeti adattábla:")
        print(self.df)

    def filter_data(self):
        # Adatok szűrése (Filtering data)
        filtered_data = self.df[self.df['Age'] > 25]
        print("\n25 év feletti személyek:")
        print(filtered_data)

    def add_salary_column(self):
        self.df['Salary'] = [50000, 60000, 75000, 48000, 55000]
        print("\nAdattábla az új 'Salary' oszloppal:")
        print(self.df)

    def rename_columns(self):
        self.df.rename(columns={'Age': 'Életkor', 'City': 'Város'}, inplace=True)
        print("\nÁtnevezett oszlopok:")
        print(self.df)

    def summarize_data(self):
        summary = self.df.describe()
        print("\nStatisztikai összegzés:")
        print(summary)

if __name__ == '__main__':
    table_op = DataTableOperation()