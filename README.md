一个网页 从zoomeye上获取到可用的xiaoya集合，每6个小时更新一次，然后发布出来

```
先创建镜像

docker build -t xiaoyalist .

运行容器
docker run -d -p 5678:5000 --restart unless-stopped xiaoyalist
```

![image](https://github.com/meteoryxx/xiaoyalist/assets/11530764/d50de230-5e38-4c55-ad13-447327d2c1ac)
