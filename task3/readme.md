# 📊 Searching algorithm performance report

This experiment compares the performance of three searching algorithms on texts of different sizes and formats.

## ⚙️ Searching functions

- `rabin_karp_search()` — Rabin-Karp search
- `boyer_moore_search()` — Boyer-Moore search
- `knuth_morris_pratt_search()` — Knuth-Morris-Pratt search

---

## 🔬 Test file "стаття 1.txt" with pattern "int arrayLength = integers.length;":

```
           Durations and results of searching:
Rabin-Karp search - substring found at index 5429.
    duration - 0.005568999797105789s.
Boyer-Moore search - substring found at index 5429.
    duration - 0.000615299679338932s.
Knuth-Morris-Pratt search - substring found at index 5429.
    duration - 0.0027810996398329735s.

           The current test shows that:
 - Boyer-Moore search is 9.05087388163282 times faster than Rabin-Karp search.
 - Boyer-Moore search is 4.519910757666803 times faster than Knuth-Morris-Pratt search.
```

---

## 🔬 Test file "стаття 2.txt" with pattern "кількість агентів 524288":

```
Durations and results of searching:
Rabin-Karp search - substring found at index 11789.
    duration - 0.010827000252902508s.
Boyer-Moore search - substring found at index 11789.
    duration - 0.0018380004912614822s.
Knuth-Morris-Pratt search - substring found at index 11789.
    duration - 0.005568499676883221s.

           The current test shows that:
 - Boyer-Moore search is 5.890640565319745 times faster than Rabin-Karp search.     
 - Boyer-Moore search is 3.0296508098653283 times faster than Knuth-Morris-Pratt search.
```

---

## ✅ Conclusion

- The Boyer-Moore algorithm consistently showed the best performance among the three algorithms tested.

- Rabin-Karp was the slowest algorithm in both tests. This aligns with the fact that, although it has a good theoretical complexity, it tends to be slower in practice due to hash computations.

- Knuth-Morris-Pratt (KMP) had medium performance — faster than Rabin-Karp but slower than Boyer-Moore.