一个网页 从zoomeye上获取到可用的xiaoya集合，每6个小时更新一次，然后发布出来

```
先创建镜像

docker build -t xiaoyalist .

运行容器  5679是清单  5678是反代的xiaoya
docker run -d --restart=unless-stopped -p 5679:5000 -p 5678:80 --name xiaoyalist xiaoyalist
```

```
awk -F'[][]' '{print $2}' /var/log/nginx/access.log | awk '{print $1}' | cut -d: -f1 | sort | uniq -c | awk '{print $2 ": " $1 " 次访问"}'

```

![image](https://github.com/meteoryxx/xiaoyalist/assets/11530764/d50de230-5e38-4c55-ad13-447327d2c1ac)
不用担心自己的token是否有用和过期、封号

![image](https://github.com/meteoryxx/xiaoyalist/assets/11530764/09226ad0-276f-4b48-99fd-804a5517cc81)
