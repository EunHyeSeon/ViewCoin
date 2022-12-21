from dto import coinDTO
from dao import coinDAO

def test_coininsert():
  newcoin = coinDTO('LTC','Litecoin','14-08-2013', 2.66, 2.76, 2.62, 2.74)
  coinDAO.coininsert(newcoin)
  result = coinDAO.selectbydate('14-08-2013', 'LTC')
  print('test_coininsert result :' + result)

def test_allcoin():
  result = coinDAO.allcoin('Litecoin')
  print('test_allcoin result : ' + result)

def test_deletecoin():
  coinDAO.deletecoin('14-08-2013', 'LTC')
  result = coinDAO.selectbydate('14-08-2013', 'LTC')
  print('test_deletecoin result : ' + result)

def test_minmax():
  result = coinDAO.minmax('Litecoin')
  print('test_minmax result : ' + result)

def test_selectname():
  result = coinDAO.selectname()
  print('test_selectname : ' + result)

def test_selectbydate():
  result = coinDAO.selectbydate('13-08-2013', 'LTC')
  print('test_selectbydate result : ' + result)