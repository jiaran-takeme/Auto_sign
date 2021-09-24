# Auto_sign For zzu
@jiaran_takeme

此程序专为郑州大学健康打卡设计

selenium
* pip  install selenium

webdriver
* http://chromedriver.storage.googleapis.com/index.html

## 2021.9.24 更新
* 修改了错误的xpath
```python
browser.find_element_by_xpath('/html/body/form/div/div[13]/div[5]/div[4]/span').click()
```
改为
```python
browser.find_element_by_xpath('/html/body/form/div/div[13]/div[3]/div[4]/span').click()
```
## 2021.8.24 更新
* 增加了对健康码颜色的选择，使用如下代码
```python
select.select_by_value("g")  # "g" 绿码,"r" 红码,"y" 黄码
```
