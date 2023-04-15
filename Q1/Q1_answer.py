# Function to check the valid size of the shirt
def size_to_index(size):
    base = size[-1]
    x_count = len(size) - 1

    if base == "S":
        return x_count
    elif base == "M":
        return 1001 + x_count
    elif base == "L":
        return 1002 + x_count
    else:
        raise ValueError("Invalid size")


def main():
    # Read the number of shirts in the shop
    n = int(input())
    shop_sizes = input().split()
    # Read the number of shirts requested
    m = int(input())
    request_sizes = input().split()

    # Count the number of shirts of each size
    shop_size_counts = {}
    for size in shop_sizes:
        index = size_to_index(size)
        shop_size_counts[index] = shop_size_counts.get(index, 0) + 1

    # Check if the shop can fulfill all the requests
    can_fulfill_all = True
    for request in request_sizes:
        found = False
        request_index = size_to_index(request)
        # Check if the shop has a shirt of the same size
        for index in range(request_index, 2003):
            if index in shop_size_counts and shop_size_counts[index] > 0:
                shop_size_counts[index] -= 1
                found = True
                break

        if not found:
            can_fulfill_all = False
            break

    if can_fulfill_all:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
