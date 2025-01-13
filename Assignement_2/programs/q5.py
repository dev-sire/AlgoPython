import gc
import psutil

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)

def simulate_memory_allocation():
    data = [i for i in range(1000000)]
    return data

if __name__ == "__main__":

    initial_memory = get_memory_usage()
    print(f"Initial Memory Usage: {initial_memory:.2f} MB")

    large_list = simulate_memory_allocation()
    post_allocation_memory = get_memory_usage()
    print(f"Memory Usage After Allocation: {post_allocation_memory:.2f} MB")

    gc.collect()

    post_gc_memory = get_memory_usage()
    print(f"Memory Usage After Garbage Collection: {post_gc_memory:.2f} MB")

    if post_gc_memory < post_allocation_memory:
        print("Garbage collection reclaimed memory.")
    else:
        print("Garbage collection did not reclaim memory.")