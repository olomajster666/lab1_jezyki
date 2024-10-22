from functools import reduce


class Task:
    def __init__(self, name, execution_time, reward):
        self.name = name
        self.execution_time = execution_time
        self.reward = reward


def calculate_waiting_time(tasks):
    waiting_times = []
    current_time = 0

    for task in tasks:
        waiting_times.append(current_time)
        current_time += task.execution_time

    return waiting_times, sum(waiting_times)


def main():
    tasks = [
        Task("Task 1", 3, 10),
        Task("Task 2", 1, 5),
        Task("Task 3", 4, 8),
        Task("Task 4", 2, 7),
    ]


    tasks.sort(key=lambda task: task.execution_time)


    waiting_times_proc, total_waiting_time_proc = calculate_waiting_time(tasks)

    print("Procedural Approach - Optimal order of tasks:")
    for task in tasks:
        print(f"{task.name} (Execution Time: {task.execution_time}, Reward: {task.reward})")

    print(f"Total Waiting Time (Procedural): {total_waiting_time_proc}\n")


    sorted_tasks_func = sorted(tasks, key=lambda task: task.execution_time)


    waiting_times_func, total_waiting_time_func = calculate_waiting_time(sorted_tasks_func)

    print("Functional Approach - Optimal order of tasks:")
    for task in sorted_tasks_func:
        print(f"{task.name} (Execution Time: {task.execution_time}, Reward: {task.reward})")

    print(f"Total Waiting Time (Functional): {total_waiting_time_func}")


if __name__ == "__main__":
    main()
