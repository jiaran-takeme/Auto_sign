# Auto_sign For zzu
@jiaran_takeme

此程序专为郑州大学健康打卡设计

B站视频教程链接
* https://www.bilibili.com/video/BV1rg411M75a


依赖
* pip install selenium
* pip install ddddocr

webdriver
* http://chromedriver.storage.googleapis.com/index.html

## 2020.9.6 更新
* 增加了对此类验证码的识别功能
![code](https://user-images.githubusercontent.com/87650568/188530439-6623ae05-1eee-4fc6-b1b1-9f037a751038.png)

## 2022.9.5 更新
* 增加了验证码自动识别及填入
```python
    imgCode = browser.find_element(By.XPATH, '//*[@id="bak_0"]/img')  # 定位验证码
    imgCode.screenshot("code.png")  # 下载图片
    ocr = ddddocr.DdddOcr()  # 利用ddddocr识别验证码
    
    with open("code.png", "rb") as f:
        image = f.read()
    codeResult = ocr.classification(image)  # 返回验证码识别结果
    
    browser.find_element(By.NAME, 'myvs_94c').send_keys(codeResult)  # 输入验证码
```

## 2022.6.20 更新
* 增加了便于定位问题的print语句

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
