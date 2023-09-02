import requests


def shortenLink(fulllink,linkname):
    
    API_KEY="81c5763b98e197f5f1548fa279be823473d99"
    BASE_URL="https://cutt.ly/api/api.php"
    
    playload={'key':API_KEY,'short':fulllink,'name':linkname}
    request=requests.get(BASE_URL,params=playload)
    data=request.json()
    
    print()
    
    try:
        title=data['url']['title']
        short_link=data['url']['shortLink']
        
        print(f' Title is  {title}')
        print(f"Short Link is : {short_link}")
    except:
        status=data['url']['status']
        print(f"Error Status : {status}")
        
if __name__=="__main__":
           
    link=input("Enter Your Longest Link ")
    name=input("Give name for shotening the link ")
    shortenLink(link,name)

