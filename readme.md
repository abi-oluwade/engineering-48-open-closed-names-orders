# Opening reading, writing files & error handling

Topics covered:
- open()
- try & except
- with & finally
- exceptions and error handling

    ``
    (...)All that can go wrong, will go wrong -Mr Murphy
    ``
## Error handling
Mean assuming things will break and handling your errors when they do. Providing adequate feedback while failing with grace.
When you handle your error, you code can continue to run.    

## Definitions

### try: / except/ finally:
These blocks of code are used in conjunction to error handle. 
````
    try:
        block of code
        block of code
    except <exception> as 
   place_holder:
        block of code
        block of code
        print(place_holder)
    finally:
        block that runs after
````

### using the open() and with()
When using open() you need to close the files you actually open!.

you can skip this step using 'with':
````
with open() as <placeholder>:
    <placeholder>:
        placeholder.readlines
````

### Exceptions
These occur when an error occurs.