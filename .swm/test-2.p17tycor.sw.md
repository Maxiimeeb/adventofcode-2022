---
id: p17tycor
title: Test 2
file_version: 1.1.3
app_version: 1.18.17
---

Other doc

<br/>


<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 03/main.py
```python
23     class ItemPriorityCalculator:
24         _test = 123
25         __first_priority_lower = ord("a")
26         __last_priority_lower = ord("z")
27     
28         __first_priority_upper = ord("A")
29         __last_priority_upper = ord("Z")
30     
31         def get_priority(self, item: str) -> int:
32             # get ascii value of item
33             ascii_value = ord(item)
34     
35             if self.__first_priority_lower <= ascii_value <= self.__last_priority_lower:
36                 return ascii_value - self.__first_priority_lower + 1
37             elif self.__first_priority_upper <= ascii_value <= self.__last_priority_upper:
38                 return ascii_value - self.__first_priority_upper + 27
39     
40             raise ValueError(f"Invalid item: {item}")
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBYWR2ZW50b2Zjb2RlLTIwMjIlM0ElM0FNYXhpaW1lZWI=/docs/p17tycor).
