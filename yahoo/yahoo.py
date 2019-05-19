
import unirest
import json
import pandas 



def get_yahoo_movers_resp():    # invoked th restapi with given yahoo fininca API
	print "getting yahoo data"    # expose rest get api
	response = unirest.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers?region=US&lang=en",
  		headers={
    		"X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    		"X-RapidAPI-Key": "d9267fb998mshf60d0ee8774f8ecp1ed320jsna74debfe8f71",
    		"Content-Type" : "application/json",
    		"Accept" : "application/json"
#output : response of json data
  		}
  	)
  	if (response.code == 200):
  		return response.raw_body

  	else:
  		print response.code, response.body
  		return None

def write_to_xslx(file_name,json_string):
	print "wrintg to xslx file"
	obj = json.loads(json_string)
	result = obj['result']
	#print result
	

	quotes=[]
	categories=[]

	for category in result:
		data = category['id']+","\
				+ category['title']+ ","\
				+ category['canonicalName'] + ","\
				+ str(category['start']) + ","\
				+ str(category['count']) + ","\
				+ str(category['total']) + ","\
				+ str(len(category['quotes']))

		category_id = {
			'ID' : category['id'],
			'Title' : category['title'],
			'count' : str(category['count']),
			'Total' : str(category['total']),
			'#Quotes' : str(len(category['quotes']))
		}

		categories.append(category_id)
		

		for quote in category['quotes']:
			quo = {
				'Title' : category['title'],
				'Quote' : quote['quoteType'],
				'Name' : category['canonicalName'],
				'Market' : quote['market'],
				'Market_state' : quote['marketState'],
				'priceHint' : quote['priceHint'],
				'symbol' : quote['symbol']
			  
			}

			quotes.append(quo)

	pandas.read_json(json.dumps(categories)).to_excel("markets.xlsx")
	pandas.read_json(json.dumps(quotes)).to_excel("quotes.xlsx")
	#print categories

		

def process_yahoo_data():
	resp_data = get_yahoo_movers_resp()
	if(resp_data):
		write_to_xslx("yahooout.csv",resp_data)

