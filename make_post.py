import datetime
import os

PATH = os.path.dirname(os.path.realpath(__file__))
SUBDIR = "_posts"


def make_post_name(title: str) -> str:
    date = datetime.datetime.now()
    name = f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}-{title.title().replace(' ', '-')}.md"
    return name


def make_file(filename: str) -> "File":
    FILEPATH = os.path.join(PATH, SUBDIR, filename)
    try:
        F = open(FILEPATH, 'w')
    except IOError:
        print("Wrong Path.")
    return F


def write_to_post(file: "File", title: str) -> None:
    file.writelines(f"""---
layout: post
title:  "{title}"
categories: post
---""")
    file.close()


if __name__ == "__main__":
    title = input("[Title?]\t")
    filename = make_post_name(title)
    F = make_file(filename)
    write_to_post(F, title)
