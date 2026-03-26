# Task 3 — Bug Fix

The bug was a missing `await` before `client.post()` in the `call_llm` function.

Without `await`, Python does not actually execute the HTTP request — instead it 
returns a coroutine object. So when the next line `resp.json()` runs, it throws 
an `AttributeError: 'coroutine' object has no attribute 'json'` because a 
coroutine object has no `.json()` method. The API crashes at runtime.

Adding `await` before `client.post()` fixes this by telling Python to actually 
wait for the HTTP request to complete and return a real response object before 
moving to the next line.

## The Code Before Fix
```python
resp = client.post(
    'https://api.example-llm.com/generate',
    json={'prompt': query},
    timeout=30.0
)
```

## The Code After Fix
```python
resp = await client.post(
    'https://api.example-llm.com/generate',
    json={'prompt': query},
    timeout=30.0
)
```
