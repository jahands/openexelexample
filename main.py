filters = [
  ['col0', 5],
  ['col1', 7]
]
data = [
  # col0, col1
  [1, 3],
  [5, 9],
  [2, 7]
]
colMap = {
  'col0': 0,
  'col1': 1
}
results = []
for d in data:
  for f in filters:
    filterColName = f[0]
    filterColValue = f[1]
    if(d[colMap[filterColName]] == filterColValue):
      results += [d]
      break # A row can match multiple filters, only match once.

print(results)

from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active
