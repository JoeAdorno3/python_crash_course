# goal of program is to try out looking for name values across a dictionary and then adding those into a list


brand_dict = {
	"brand_account_1": {"id": "brand_account_1", "name": "dunkin donuts",}, 
	"brand_account_2": {"id": "brand_account_2", "name": "mcdonald's",},
	"brand_account_3": {"id": "brand_account_3", "name": "papa johns",},
}


account_dict = {
	"account_1": {"id": "account_1", "name": "papa johns corporate", "sales_notes": "corporate account for papa johns", "display_name": ""}, 
	"account_2": {"id": "account_2", "name": "fresh_pizza_inc", "sales_notes": "papa johns franchisee", "display_name": ""}, 
	"account_3": {"id": "account_3", "name": "golden arches site account", "sales_notes": "", "display_name": "mcdonald's"}, 
	"account_4": {"id": "account_4", "name": "massachuset's favorite coffee inc.", "sales_notes": "dunkin donuts franchisee with 20 sites", "display_name": ""}, 
	}

existing_relationships = [{"id": "account_1", "brand_id": "brand_account_3"}]

new_relationships = []

for i in account_dict:
	for b in brand_dict:
		if brand_dict[b]["name"] in account_dict[i]["sales_notes"] or brand_dict[b]["name"] in account_dict[i]["name"] or brand_dict[b]["name"] in account_dict[i]["display_name"]:
			if {"id": account_dict[i]["id"], "brand_id": brand_dict[b]["id"]} not in existing_relationships:
				new_relationships.append({"id": account_dict[i]["id"], "brand_id": brand_dict[b]["id"]})




print(new_relationships)






