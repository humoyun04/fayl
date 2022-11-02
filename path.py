from pathlib import Path

desktop=Path("/Users/HP/Desktop/")

full = desktop / "full" / "yoz.mp3"
empty = desktop / "empty" / "yoz.mp3"
full1 = desktop / "full" / "kor.mp4"
empty1 = desktop / "empty" / "kor.mp4"
full2 = desktop / "full" / "jonat.jpeg"
empty2 = desktop / "empty" / "jonat.jpeg"
full3 = desktop / "full" / "hello.py"
empty3 = desktop / "empty" / "hello.py"

full.replace(empty)
full1.replace(empty1)
full2.replace(empty2)
full3.replace(empty3)

