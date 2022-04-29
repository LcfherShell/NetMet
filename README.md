# NetMet
NetMet Module to Python 2.7 > 3.* and 4

This technique uses scraping technique with the help of beautifullsoup lib, and API Web, and
free API WEB 30 by 1 user. 

###PYWEATHERS
```````````````````````````````````````````````
from NetMet import PyWeathers

weathers = PyWeathers("Hello")
weathers.___create___("5b50f623ddc14b6c91573722222404") #auth

weathers.q_parameter("Jakarta") #set city
weathers.days(2) #1-7 day
weathers.lang #map languages
weathers.lang = "javanese" #set languages

weathers._requests(weathers.urls("forecast"))
```````````````````````````````````````````````


###PYNEWS
```````````````````````````````````````````````
from NetMet import PyNews
#------- Method 1

news = PyNews("The Best Movie")
news.params(country="AS", by_date=news.by_date("2021 12 23", "daterange")) #you cant add parameter tags="sss"
news.official
news.dork("google")
news.post(site='nbcnews.com')
news.result.json() or news.result.text() or news.result.html() or news.result.pdf()

#---OR---- Method 2

parameter = {
'tags':'Healthy',
'q': 'Healthy burger',
'country': 'AS',
'sites': 'nbcnews.com',
'dork': 'yahoo'
}

news = PyNews(params=parameter)
news.official
news.post()
news.result.json() or news.result.text() or news.result.html() or news.result.pdf()

#and  just info : news.post(proxies="AS") and news.params(tags="hotdog")
```````````````````````````````````````````````

Warning if you use the params function (in method 1), you can't do it again and an error will occur except. 
For loading time depends on your internet speed, standard time of page search : google 1.3s, bing 1.42s, duckgo 2.1s and yahoo 1.27s.

you can 

------------------------------------------------------------------------------------------



###IP Calculator
```````````````````````````````````````````````
from NetMet import IPCall_A, IPCall_B

#manipulate Net
child = IPCall_A #Public Class
network = IPCall_B #Private Class

print("Call function using public class")
for i in range(3):
    for ipv4 in child.IPv4(i):
         print("IPv4:", ipv4)
    for ipv6 in child.IPv6(i):
         print("IPv6:", ipv6)
    print("MacAddresss:", child.MacAddresss(),"\n")
i = 0
print("\nCall function using private class")
for i in range(3):
    for ipv4 in network.IPv4(i):
         print("IPv4:", ipv4) 
    for ipv6 in network.IPv6(i):
         print("IPv6:", ipv6)
    print("MacAddresss:", network.MacAddresss(),"\n")

ipv4 = "192.222.02.1"
ipv6 = "f18d:5980:50d1::cf2d"

print("Check Version and Class Ip addresses")
print("IP version:", child.Validate_IP(ipv4))
print("IPv4 Class:",  child.IPv4_Class(ipv4))
print("\nIP version:", child.Validate_IP(ipv6))
print("IPv6 Class:",  child.IPv6_Class(ipv6))
print("\nManipulate IPv4 :")
for x in range(1, 33):
   child.IPv4_Calculator("{}/{}".format(ipv4, x))
   print(child.saving.output)
print("\nManipulate IPv6 :")
ipv6range = "{}/{}".format(ipv6, 21)
child.IPv6_Calculator(ipv6range)
print(child.saving.output)

```````````````````````````````````````````````

###Topologhy Offline
```````````````````````````````````````````````
from NetMet import Topologhy
host = Topologhy
//make token
host._token(ipv4, 12)
//set hostrot
host.server
host.server = "Online"//online
//router
host.router()
//make client v1(vuln token)
host.clients_v1(None, host.saving.pinbus)//vuln by access token and custum client
host.clients_v2()//random private token and auto generate

host.switch_s = "192.222.02.1 192.222.02.3"
host.Hypermedia_Host("192.222.02.2")//test connection
```````````````````````````````````````````````

If you find any bugs/problems, please contact email:
      **LCFHERSHELL@TUTANOTA.COM** or **alfiandecker2@gmail.com**

Happy coding :). Sorry, my English is very bad
