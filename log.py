from time import localtime, strftime

def info(details) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : INFO :", details)

def debug(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : DEBUG :", details)

def warn(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : WARN :", details)

def error(*details: str) -> None:
  print(f"{strftime("%Y%m%d - %H:%M:%S %z",localtime())} : ERROR :", details)

