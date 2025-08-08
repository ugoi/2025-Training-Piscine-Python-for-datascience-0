def all_thing_is_obj(thing: any) -> int:
    if (isinstance(thing, int)):
        print("Type not found")
    else:
        title = "";
        if(isinstance(thing, str)):
            title = f"{thing} is in the kitchen"
        else:
            title = type(thing).__name__.capitalize();
        print(f"{title} : {type(thing)}")
    return 42

