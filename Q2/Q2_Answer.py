def validate_dataset(records):
    all_valid = True
    error_codes = []
    # Check if the dataset is valid
    for record in records:
        if len(record) == 3:
            _, is_valid, error_message = record
        if len(record) == 2:
            _, is_valid = record
        is_valid = is_valid.lower() == "true"
        all_valid = all_valid and is_valid

        if not is_valid:
            error_codes.append(error_message)

    return all_valid, error_codes


def main():
    n = int(input())
    records = [input().split() for _ in range(n)]

    all_valid, error_codes = validate_dataset(records)

    if all_valid:
        print("Yes")
    else:
        print("No")
        print(" ".join(error_codes))


if __name__ == "__main__":
    main()
