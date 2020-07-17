import collections
import heapq
from typing import List


# Have a heap / priority queue with max count of task work at top
# Greedy
def least_time_needed(tasks: List[str], n: int):
    task_count = {}
    for t in tasks:
        task_count[t] = task_count.get(t, 0) + 1

    task_q = []
    for t, c in task_count.items():
        heapq.heappush(task_q, (-c, t))  # so it becomes a max heap

    total_time = 0
    while task_q:
        time_till_cooldown = n + 1
        task_unfinished = {}
        while time_till_cooldown and task_q:
            c, t = heapq.heappop(task_q)
            time_till_cooldown -= 1
            task_count_left = -c - 1
            if task_count_left > 0:
                task_unfinished[t] = task_count_left

        total_time += n + 1
        if not task_unfinished:
            total_time -= time_till_cooldown
        for t, c in task_unfinished.items():
            heapq.heappush(task_q, (-c, t))

    return total_time


# after all is max * N + 1
def leastInterval(tasks: List[str], n: int) -> int:
    freq = collections.Counter(tasks)
    max_number = max(freq.values())

    counter = 0
    for i, num in enumerate(freq.values()):
        if num == max_number:
            counter += 1
    ret = (max_number - 1) * (n + 1) + counter
    return max(ret, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(least_time_needed(tasks, n))
print(leastInterval(tasks, n))

tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
print(least_time_needed(tasks, n))
print(leastInterval(tasks, n))

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(least_time_needed(tasks, n))
print(leastInterval(tasks, n))
