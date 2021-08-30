
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Got url from data.gov.in
url = "https://data.gov.in/resources/district-wise-total-msme-registered-service-enterprises-till-last-date/api"
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
