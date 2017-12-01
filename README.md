# Spider
爬虫使用框架`Scrapy`，数据库使用`MongoDB`。

## GB688
该爬虫对[国家技术标准资源服务平台](http://www.gb688.cn)进行爬取，对以下字段进行存储：
```
  Stardard=Field()
  CNname=Field()
  ENname=Field()
  State=Field()
  CSS=Field()
  ICS=Field()
  Issuedate=Field()
  Enforcedate=Field()
  ResponseDept=Field()
  RelevateDept=Field()
  IssueOrganization=Field()
  Remarks=Field()
```

## IECCH
该爬虫对[IECWebStore](https://webstore.iec.ch/)进行爬取，对以下字段进行存储：
```
  Standard=Field()
  Name=Field()
  PubType=Field()
  PubDate=Field()
  Edition=Field()
  Languages=Field()
  TCSC=Field()
  ICS=Field()
  StabilityDate=Field()
  Abstract=Field()
  Pages=Field()
  Size=Field()
```
