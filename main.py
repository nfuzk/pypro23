import pandas as pd


def show_data(cm, data):
    print("A harom leggyakoribb honap:")
    for month in cm.values:
        print(f"\t{month[0]}\t----\t{int(month[1]) / len(data) * 100:.2f}%")


def main():
    data = pd.read_csv("astronauts.csv")

    birth_months = data["Birth Date"].apply(lambda c: c[0:c.index("/")]).reset_index()

    counted_months = birth_months.groupby(["Birth Date"], sort=False)["Birth Date"].count().reset_index(name="count").nlargest(3, "count")

    show_data(counted_months, data)


if __name__ == "__main__":
    main()
