class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0
        self.total_float = 0

def calculate_critical_path(tasks):
    # Calcula el tiempo más temprano (TE) y el tiempo más tardío (TL) para cada tarea
    for task in tasks:
        if not task.dependencies:
            task.early_start = 0
        else:
            task.early_start = max([dependency.early_finish for dependency in task.dependencies])
        task.early_finish = task.early_start + task.duration

    # Calcula el tiempo más tardío (TL) para cada tarea
    tasks.reverse()
    last_task = tasks[0]
    last_task.late_finish = last_task.early_finish
    last_task.late_start = last_task.early_start
    tasks.remove(last_task)

    for task in tasks:
        if task.dependencies:
            task.late_start = min([dependency.late_finish for dependency in task.dependencies]) - task.duration
        else:
            task.late_start = task.early_start
        task.late_finish = task.late_start + task.duration

    # Calcula el margen total (MT) para cada tarea
    for task in tasks:
        task.total_float = task.late_start - task.early_start

def print_critical_path(tasks):
    print("Ruta crítica:")
    for task in tasks:
        if task.total_float == 0:
            print(task.name)

def calculate_min_duration(tasks):
    min_duration = max([task.early_finish for task in tasks])
    print("Duración mínima del proyecto:", min_duration)

# Crear las tareas
tasks = [
    Task("A", 20),
    Task("B", 5),
    Task("C", 40),
    Task("D", 10),
    Task("E", 5),
    Task("F", 10),
    Task("G", 20),
    Task("H", 25),
    Task("I", 35),
    Task("J", 25),
    Task("K", 15),
    Task("L", 5),
    Task("M", 25)
]

# Establecer las dependencias entre las tareas
tasks[0].dependencies.extend([tasks[3], tasks[5]])
tasks[1].dependencies.append(tasks[2])
tasks[2].dependencies.append(tasks[7])
tasks[3].dependencies.extend([tasks[4], tasks[12]])
tasks[4].dependencies.append(tasks[5])
tasks[6].dependencies.append(tasks[7])
tasks[7].dependencies.append(tasks[8])
tasks[8].dependencies.append(tasks[9])
tasks[9].dependencies.extend([tasks[10], tasks[11]])
tasks[10].dependencies.append(tasks[11])
tasks[11].dependencies.append(tasks[12])

# Calcular la ruta crítica y la duración mínima del proyecto
calculate_critical_path(tasks)
print_critical_path(tasks)
calculate_min_duration(tasks)


