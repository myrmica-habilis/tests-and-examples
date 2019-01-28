import os

# a test to compare file size information returned by os.stat().st_size
# and size calculated manually by len(f.read())


def get_real_size(path):
    with open(path, "rb") as f:
        return len(f.read())


path = os.curdir
total_counter = 0
difference_counter = 0

for dir_path, __, filenames in os.walk(path):
    for filename in filenames:
        fullname = os.path.join(dir_path, filename)
        total_counter += 1
        stat_st_size = os.stat(fullname).st_size
        real_size = get_real_size(fullname)
        if not (stat_st_size == real_size):
            print(fullname, stat_st_size, real_size)
            difference_counter += 1
    # limit number of files (not to get stuck in a huge dir)
    if total_counter > 1000:
        break

print("{} files tested.\n{} differences found."
      .format(total_counter, difference_counter))
