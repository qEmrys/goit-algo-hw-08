import heapq


def min_cost_cables(cable_lengths):
    if not cable_lengths:
        return 0

    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        combined_length = first + second
        total_cost += combined_length
        heapq.heappush(cable_lengths, combined_length)

    return total_cost
