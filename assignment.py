input_instances = {"us-east":{
                    "large":0.12,
                    "xlarge":0.23,
                    "2xlarge":0.45,
                    "4xlarge":0.774,
                    "8xlarge":1.4,
                    "10xlarge":2.82},
                   "us-west":{
                     "large":0.14,
                     "2xlarge":0.413,
                     "4xlarge":0.89,
                     "8xlarge":1.3,
                     "10xlarge":2.97}}


server_list_map = ["large","xlarge","2xlarge","4xlarge","8xlarge","10xlarge"]

def serverwithboth(no_cpu,sum_li,server_list,cost_list,max_price):
	i = len(server_list)
	ans = [0 for q in range(i)]
	while i >=0 :
		if no_cpu > sum_li:
				if(sum(cost_list[0:i-1]) <= max_price):
					if sum_li > 0:
						incr = no_cpu // sum_li
						no_cpu = no_cpu % sum_li
					ans = [a + incr for a in ans]
				else:
					if server_list[i-1] > 0:
						sum_li = sum_li - server_list[i-1]
					i = i -1
		else:
			if server_list[i-1] > 0:
				sum_li = sum_li - server_list[i-1]
			i = i -1
	return ans

  
def serverwithnoprice(no_cpu,sum_li,server_list):

    i = len(server_list)
    ans = [0 for q in range(i)]
    while i >= 0 :
        if no_cpu > sum_li :
            if sum_li > 0:
                incr = no_cpu//sum_li
                no_cpu = no_cpu % sum_li
            else :
                ans[0] = ans[0] + 1
                break
            ans= [a + incr for a in ans]
        else :
            if server_list[i-1] > 0:
                sum_li = sum_li - server_list[i-1]
            i = i - 1
    return ans

def serverWithnoCPU(price,cost_list,server_list):
    i = len(cost_list)
    ans = [0 for val in range(i)]
    cost  = 0
    rem_price = price
    while i >= 0:
        if cost_list[i-1] < 0:
            i = i-1
        elif cost_list[i-1] <= rem_price:
            rem_price = rem_price - cost_list[i-1]
            if  server_list[i-1] > 0:
                ans[i-1] = ans[i-1] + 1
        else:
            i = i-1
    return ans

def setupServerCostList(server_list_map,hours,cpus,price):
    server_combination_t = []
    server_combination = []
    total_cost = []
    for k,v in input_instances.items():   
        server_list = [0 for s in range(len(server_list_map))]

        cost_list = [0 for s in range(len(server_list_map))]
        
        for i in range(len(server_list_map)):
            if server_list_map[i] in list(v.keys()):
                server_list[i] = 2**i
                cost_list[i] = v[server_list_map[i]]
            else:
                cost_list[i] = -1
        
        cost_list_h = [h*hours for h in cost_list]
        
        if price is None:
            sum_server_list = sum(server_list)
            server_combination_t = (serverwithnoprice(cpus,sum_server_list,server_list))
            
            server_combination_t = [float(val) for val in server_combination_t]
            total_cost.append([a*b for a,b in zip(server_combination_t,cost_list_h)])
            server_combination.append(server_combination_t)
        
        elif cpus is None:
            server_combination_t = serverWithnoCPU(price,cost_list_h,server_list)
            
            server_combination_t = [float(val) for val in server_combination_t]
            total_cost.append([a*b for a,b in zip(server_combination_t,cost_list_h)])
            server_combination.append(server_combination_t)

    return total_cost,server_combination       
        

def get_costs(hours,cpus,price):
    
    totalCost,retServers = setupServerCostList(server_list_map,hours,cpus,price)
    cost_list = []
    ans_list = []
    flag = 0
    for i in range(len(totalCost)):
        cost_list.append(sum(totalCost[i]))

    for k in input_instances.keys():
        ans_dict = {}
        if flag == 0:
            counter = 0
            flag = 1
        else:
            counter += 1
        ans_dict["region"] = k
        ans_dict["total_cost"] = cost_list[counter]
        ans_dict["servers"] = []
        for s in range(len(server_list_map)):
            if retServers[counter][s] > 0:
                sr = (server_list_map[s],retServers[counter][s])
                ans_dict["servers"].append(sr)
        ans_list.append(ans_dict)

    print(sorted(ans_list, key = lambda i:i["total_cost"]))
    

    

get_costs(2,None,30)


        
    


    


