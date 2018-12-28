import os

# a test to compare file size information retrieved
# by os.path.getsize() and os.stat().st_size,
# and to check with the real file size


def get_real_size(path):
    with open(path, "rb") as f:
        return len(f.read())


total_counter = 0
difference_counter = 0

for dir_tuple in os.walk(os.curdir):
    dir_path = dir_tuple[0]
    for basename in os.listdir(dir_path):
        fullname = os.path.join(dir_path, basename)
        if os.path.isfile(fullname):
            total_counter += 1
            getsize_size = os.path.getsize(fullname)
            stat_st_size = os.stat(fullname).st_size
            real_size = get_real_size(fullname)
            if not (getsize_size == stat_st_size == real_size):
                print(fullname, getsize_size, stat_st_size, real_size)
                difference_counter += 1
    # limit number of files (not to get stuck in a huge dir)
    if total_counter > 1000:
        break

print("{} files tested.\n{} differences found."
      .format(total_counter, difference_counter))
