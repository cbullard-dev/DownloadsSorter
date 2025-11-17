from time import localtime, strftime

def info(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : INFO :", "".join(details))

def debug(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : DEBUG :", " : " "".join(details))

def warn(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : WARN :", "".join(details))

def error(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : ERROR :", "".join(details))

