"""
    Expected o/p:
    This-is-pYthon-class-daY-3
    """
word=" this is  python  class day 3 "
word=word.strip()
word=word.capitalize()
word=word.split()
word="-".join(word)
word=word.replace("y","Y")
word=word.split("-")
print(word)
