"""
Task 2.1 Sequence
"""

__author__ = "Kasra Asarroodi"


def main():
    MEDALS_AVAILABLE = 348 # 116 events x 3 medals per event

    print("2026 Winter Olympics Medal Summary")
    print()

    nation: str = input("Enter the name of the nation: ")
    gold_medals: int = int(input(f"Enter the number of gold medals for {nation}: "))
    silver_medals: int = int(input(f"Enter the number of silver medals for {nation}: "))
    bronze_medals: int = int(input(f"Enter the number of bronze medals for {nation}: "))
    total_medals: int = gold_medals + silver_medals + bronze_medals
    percentage: float = (total_medals / MEDALS_AVAILABLE) * 100


    print(f"{nation}'s performance at the 2026 Winter Olympics was as follows:")
    print(f"- {gold_medals} Gold")
    print(f"- {silver_medals} Silver")
    print(f"- {bronze_medals} Bronze")
    print(f"That's a total of {total_medals} medals.")
    print(f"Or {percentage}% of the {MEDALS_AVAILABLE} medals on offer.")


if __name__ == "__main__":
    main()