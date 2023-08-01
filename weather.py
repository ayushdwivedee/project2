import requests
apiKey="d6f21c55f021d51d45562190de0c5bf7"
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input("Enter your city : ")
completeURL=baseURL+cityName+"&APPID="+apiKey
response=requests.get(completeURL)
data=response.json()
#print(data)

if(data["cod"]==200):
    temp = data["main"]["temp"] - 273.15
    print("Current temperature of the city is : ",temp)
elif(data["cod"]=="404"):
    print("Invalid City or Error in fetching data")
