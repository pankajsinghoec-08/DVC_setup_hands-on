import os

# We also need to create data_given folder which is intented to act as remote resource
dirs = [
        os.path.join("data","raw"),
        os.path.join("data","processed"),
        "notebooks",
        "saved_models",
        "src"
]

# Now create the above directory one by one
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"), "w") as f:
        pass

# Files that we need
files = [
         "dvc.yaml",
         "params.yaml",
         ".gitingnore",
         os.path.join("src","__init__.py")
]

# Now creating the above listed files
for file_ in files:
    with open(file_, 'w') as f:
        pass