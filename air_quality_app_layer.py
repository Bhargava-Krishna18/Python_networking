import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Got url from data.gov.in
url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=1000"
#Requesting the server using GET type
res = requests.request("GET",url)
data = res.json()
data_records = data['records'] #Fetching records key from response

#creating dataframe from json
df = pd.DataFrame(data_records)
print(df)
print(df.info()) #printing columns and other info

#plot the graph
df.plot(kind = "scatter", x = "station", y = "pollutant_avg" , xlabel="Station", ylabel="Pollution")
plt.show()
