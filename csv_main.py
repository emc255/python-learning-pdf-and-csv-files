import csv

import pandas as pd


def learning_csv():
    data = open("resources/files/example.csv", encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    for i in data_lines[:5]:
        print(i)
    # using list
    emails = list(a[3] for a in data_lines[1:5])
    print(emails)
    # using map
    names = map(lambda x: x[2], data_lines[1:5])
    print(list(names))

    # WRITING A CSV FILE
    file_to_output = open("resources/files/saving-example.csv", mode="w", newline="")
    csv_writer = csv.writer(file_to_output, delimiter=",")
    csv_writer.writerow(["a", "b", "c"])
    csv_writer.writerows([["1", "2", "3"], ["4", "5", "6"]])
    file_to_output.close()

    # APPENDING A CSV FILE
    file_to_output = open("resources/files/saving-example.csv", mode="a", newline="")
    csv_writer = csv.writer(file_to_output, delimiter=",")
    csv_writer.writerow(["x", "y", "z"])
    file_to_output.close()

    data = open("resources/files/saving-example.csv", encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    print(data_lines)


def learning_panda():
    # Replace "filename.csv" with the name of your CSV file
    df = pd.read_csv("resources/files/example.csv")
    # Set the options to display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # Print the first 5 rows of the DataFrame

    print(df.head())
    print(df.tail())

    print("Dataframe to list")
    dataframe_list = df.values.tolist()

    for index, row in df.head(5).iterrows():
        for key, value in row.items():
            print(f"{key}: {value}")
    emails = list(df.head(5)["email"])
    print(emails)

    # Create a DataFrame
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})

    # Write the DataFrame to a CSV file
    df.to_csv("resources/files/panda-saving-example.csv", index=False)
    # Append the new data to an existing CSV file

    df = pd.DataFrame({'Name': ['Jessica'], 'Age': [22]})
    df.to_csv("resources/files/panda-saving-example.csv", mode='a', header=False, index=False)


def divider(title: str):
    print(f"==========={title.upper()}===========")


if __name__ == '__main__':
    divider("learning csv")
    learning_csv()

    divider("learning panda")
    learning_panda()
