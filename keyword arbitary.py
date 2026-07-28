def display_tags(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}={values}")

display_tags(name="satwik",strength="cricket")