lst = ['a', 'b', 'c']
d = {}

index = 0
for i in lst:
    d[i] = index
    index += 1

print(d)
333333333333333333333333333
d = {'a': 10, 'b': 20}
pair_list = []

for k in d:
    pair_list.append([k, d[k]])

print(pair_list)

def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 5

import os
folder_path ="C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hamsa"
for item in os.listdir(folder_path):
 full_path = os.path.join(folder_path,item)
 if os.path.isfile(full_path):
  print(item)

  import subprocess

  subprocess.Popen([
      r"C:\Program Files\Google\Chrome\Application\chrome.exe"
  ])

  import pytest


  @pytest.mark.parametrize(
      "a,b,result",
      [
          (1, 2, 3),
          pytest.param(2, 3, 5, marks=pytest.mark.skip(reason="Skipping this case")),
          (3, 4, 7),
      ]
  )
  def test_add(a, b, result):
      assert a + b == result

