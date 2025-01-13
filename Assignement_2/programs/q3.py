import gc

def simulate_memory_allocation_and_gc(num_objects):
    objects = []
    for i in range(num_objects):
        obj = [i] * 100000
        objects.append(obj)
        print(f"Allocated object {i+1}, memory usage: {get_memory_usage()}")
    gc.collect()
    objects = []
    gc.collect()

def get_memory_usage():
    import psutil
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024

if __name__ == "__main__":
    num_objects = 10
    simulate_memory_allocation_and_gc(num_objects)