# Auto_sign For zzu
@jiaran_takeme

此程序专为郑州大学健康打卡设计

B站视频教程链接
* https://www.bilibili.com/video/BV1rg411M75a

selenium
* pip  install selenium

webdriver
* http://chromedriver.storage.googleapis.com/index.html

## 2022.4.18 更新
* 优化了代码逻辑，另外我求求学校能不能别再改这网站了，就个健康打卡，三天两头改，xpath改几次了orz

## 2022.4.4 更新
* 平台对接了郑好办平台，健康码选择功能已弃用

## 2022.1.17 更新
* 适配了新版本的selenium语法
示例
```python
browser.find_element_by_xpath('/html/body/form/div/div[11]/div[3]/div[4]/span').click()
```
改为
```python
browser.find_element(By.XPATH,'/html/body/form/div/div[11]/div[3]/div[4]/span').click()
```
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
