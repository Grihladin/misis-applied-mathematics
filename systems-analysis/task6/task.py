import json
import math

def calculate_mean_squared_difference(row: list[int], mean: float) -> float:
    return (sum(row) - mean) ** 2

def calculate_kendall_coefficient(rank_matrix: list[list[int]], num_of_ratings: int) -> float:
    mean = (num_of_ratings + 1) / (2 * num_of_ratings)
    sum_squares = sum([(num_of_ratings * rating - mean) ** 2 for rating in range(1, num_of_ratings + 1)])
    max_variance = sum_squares / (num_of_ratings - 1)

    variance = sum(calculate_mean_squared_difference(row, mean) for row in rank_matrix) / (num_of_ratings - 1)

    return variance / max_variance

def task(*args: str) -> float:
    rankings = [json.loads(arg) for arg in args]
    num_of_experts, num_of_ratings = len(args), len(rankings[0])

    sorted_ratings = sorted(rankings[0])

    ranked_ratings = [[ranking.index(rating) + 1 for rating in sorted_ratings] for ranking in rankings]

    return calculate_kendall_coefficient(ranked_ratings, num_of_ratings)

if __name__ == "__main__":
    result = task("[2, 3, 1]", "[1, 2, 3]", "[3, 1, 2]")
    print(result)
