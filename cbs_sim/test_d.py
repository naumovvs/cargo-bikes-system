import net
import route
import stochastic

size = 7
sender_code = size**2
s_weight = stochastic.Stochastic(law=1, location=0.03, scale=0.005)
s_dist = stochastic.Stochastic(law=0, location=0.05, scale=0.15)

f = open("tw_diag_300_05.txt", "w")
total_TW = []
for _ in range(300):
    n = net.Net()
    n.gen_rect(size=size, s_weight=s_dist)
    clients = []
    for nd in n.nodes:
        if nd.code < size**2:
            clients.append(nd)
    n.gen_requests(sender=n.get_node(sender_code), nodes=clients, prob=0.5, s_weight=s_weight)
    rts = n.clarke_wright(sender_code=sender_code, requests=n.demand, capacity=0.15)
    tw = sum([rt.transport_work for rt in rts])
    total_TW.append(tw)
    f.write(str(tw) + "\n")

f.close()
