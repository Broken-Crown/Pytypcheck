import inspect
from typing import get_type_hints

def pytypcheck(wrapper):
    def simple_validation(*args):
        args_type = list(get_type_hints(wrapper).values())
        if len(args_type) != len(args):
            print("No annotation of the types")
            return
        if inspect.isfunction(wrapper):  # In this case we can use callable(wrapper)
            # print("It's function")
            args_value = vars()['args']
            print(f"{args_type} -- {args_value}") 
            if all([isinstance(args_value[i], args_type[i]) for i in range(len(args_type))]):  # This check don't give us specific information about incorrect type annotation
                print("OK!")
            else:
                print("Warning: wrong type")
            # wrapper(*args)
        else:
            print("It's not a function")
    return simple_validation

@pytypcheck
def print_many_arg(a: int, b: float, c: str, d: int):
    print(f"int: {a}\nfloat: {b}\nstring: {c}")

if __name__ == "__main__":
    print_many_arg(1, 2.0, "three", 4)