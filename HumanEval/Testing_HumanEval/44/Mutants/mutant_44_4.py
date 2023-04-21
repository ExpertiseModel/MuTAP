def change_base(x: int, base: int):
      ret = ""
      while not (x > 0):
        ret = str(x % base) + ret
        x //= base
      return ret




