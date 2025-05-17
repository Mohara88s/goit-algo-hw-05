from utilities import boyer_moore_search, knuth_morris_pratt_search, rabin_karp_search
import timeit
import os

def search_alg_analyzing_func(text, pattern, search_func, search_name):
    start_time = timeit.default_timer()
    position = search_func(text, pattern)
    if position != -1:
        print(f"{search_name} - substring found at index {position}.")
    else:
        print(f"{search_name} - substring not found.")
    end_time = timeit.default_timer()
    duration = end_time - start_time
    print(f'    duration - {duration}s.')
    return duration

def test_search_algs(pattern, file_name, encoding):
    print(f'\n   Test file "{file_name}" with pattern "{pattern}":')
    text = load_text_from_file(file_name, encoding=encoding)
    if text:
        print(f'           Durations and results of searching:')
        rk_alg_duration = search_alg_analyzing_func(text, pattern, rabin_karp_search, 'Rabin-Karp search')
        bm_alg_duration = search_alg_analyzing_func(text, pattern, boyer_moore_search, 'Boyer-Moore search')
        kmp_alg_duration = search_alg_analyzing_func(text, pattern, knuth_morris_pratt_search, 'Knuth-Morris-Pratt search')
        print()
        if rk_alg_duration and bm_alg_duration and kmp_alg_duration:
            print('           The current test shows that:')
            print(f' - Boyer-Moore search is {rk_alg_duration/bm_alg_duration} times faster than Rabin-Karp search.')
            print(f' - Boyer-Moore search is {kmp_alg_duration/bm_alg_duration} times faster than Knuth-Morris-Pratt search.')
    else:
        print('File missing')

def load_text_from_file(filename, folder='task3/articles', encoding='cp1251'):
    path = os.path.join(folder, filename)
    try:
        with open(path, 'r', encoding=encoding) as file:
            return file.read()
    except Exception as e:
        print(e)
        return None
    
def main():
    pattern = 'int arrayLength = integers.length;'
    test_search_algs(pattern, 'стаття 1.txt', encoding='cp1251')
    pattern = 'кількість агентів 524288'
    test_search_algs(pattern, 'стаття 2.txt', encoding='utf-8')

 
if __name__ == "__main__":
    main()