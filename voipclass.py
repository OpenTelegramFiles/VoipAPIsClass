from voipAPIs import five_sim
apikey_fivesim = input("my 5sim api_key: ")
voipPlatform = five_sim(apikey_fivesim)
print("my balance is: "+ voipPlatform.get_balance())
print("my frozen balance is: "+ voipPlatform.get_frozen_balance())
print("my rating is: "+ str(voipPlatform.get_rating()))
