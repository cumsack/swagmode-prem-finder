import requests

target = input("Target: ")


r=requests.get("https://raw.githubusercontent.com/swagmode/swagmode/main/swagmain")

if target in r.text:
  print("Target has swagmode premium")
else:
  print("Target doesn't have swagmode premium")
