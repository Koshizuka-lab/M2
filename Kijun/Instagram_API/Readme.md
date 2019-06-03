# Instagram API Tutorial
Creation Date : 2019/04/17
Created by KIJUN KIM
Copyright © 2019 JDSC All rights reserved.

## Register Information

### Manage Clients
Account = keejunn (private account of kijun)  
Client name = uhw test  
CLENT ID = "9281d305b153429989538b3b5efcf94f"  
CLIENT SECRET = "6279b6ca10c14551891b2914a90fa618"  
CLIENT STATUS = "Sandbox Mode"  

### Client-Side(Implicit) Authentication
ACCESS TOKEN = "2894007885.9281d30.bfd25b8ab34a4208af6246f65ea3287b"

### Check the availability
It is possible to use instagram api if user information pops when you access following URL.  
https://api.instagram.com/v1/users/self/?access_token=2894007885.9281d30.bfd25b8ab34a4208af6246f65ea3287b

## Reference
[1] https://www.superharinezumi.com/entry/instagram-api  
[2] https://www.instagram.com/developer/

## Hashtag Analyzation
APIを利用してハッシュタグを検索するのはSandboxモードだと実行不可能...  
対策➝ APIを通さずにスクレイピングする（Pythonとrequestsで）
