# traceroute

[Source](https://www.nanog.org/meetings/nanog47/presentations/Sunday/RAS_Traceroute_N47_Sun.pdf)

## Problems

* Networks be complicated
* People choose wrong interpretations of traceroute output

## How traceroute works
* Send a package with TTL=1, after 1 hop package is dropped, router sends ICMP TTL Exceeded back to source with original packet as payload
* Increment TTL and repeat
* Uses UDP on UNIX, Windows ICMP Echo Requests, or all of those via configuration
* TCP is not recommended because frequently filtered
* Most implementations: 3 probes per hop (hence 3*latency or ***)
* Unique code in probe: IMCP sequence number or TCP/UDP port
* Load balancing might be visible (ECMP) or not (LAG/port-channel)
* Latency: measure round trip is measured (meaning delays on reverse path affect results!)
* You see only the IP of the *Ingress* Interfaces, meaning you can and will recieve private IP ranges, giving you *no* indication of the Egress Interface IP (this is non-standard behaviour but seen everywhere)

## Interpreting DNS in traceroute
* Important because it helps you identify incorrect or suboptimal routing and know if the latency seems justified
* Location identifiers might be IATA Airport Codes, CLLI Codes, non-standard abbreviations of a city name …
* Often there is interface info in the dns, some generate this automatically, others are sloppy. You might be able to find out the type of interface and even router model in use
* but be careful, there are different conventions and even those are not always followed. 
* Context: Core (CP, Core, GBR, BB, CCR, EBR), Peering (BR, Border, Edge, IR, IGR, Peer), Customer (AR, Aggr, Cust, CAR, HSA, GW)
* Identify network boundaries by naming conventions etc, to single out probably problem areas. Try to figure out the relationship of those networks (transit provider, peer or customer)
* If you are not sure, try looking up the other side of the /30 net with nslookup

## Understanding network latency
* three types:
    * Serialization Delay: delay caused by having to transmit data through devices in packet sized chunks
    * Queuing Delay: Time spent in router queues waiting for transmission when congestion occurs
    * Propagation Delay: time spent between hops, limited by speed of light and other laws of physics
* Utilization is basically the chance that queueing will occur, because in reality an interface is either utilized or not, not 50% utilized
* latency is normal if it fits with geographical data. For reference: one fiber straight around the equator would send a round trip packet in 440ms


## ICMP prioritizationand rate-limiting
* cosmetic delys affect the traceroute: Time to generate the TTL Exceed message needs to be factored in, which does not impart 'real' traffic, *and* ICMP generation requires software based handling which is slow and *not* a priority
* ICMP generation is also often rate limited, sometimes hard coded
* **Therefore latency spikes in the middle of a traceroute mean nothing if they do not continue forward** (worst case: asymmetric path)


## Asymmetric forwarding paths
* traceroute only shows forward path, but routing is asymmetrical in most cases
* the reverse path is completely invisible and could be different for every hop
* only practical solution is to look at both forward and reverse path traceroutes and try to spot issues
* even that will not catch asymmetrical paths in the middle
* asymmetrical paths often start at network boundaries due to policy changes


## Load balancing across multiple paths
* When in doubt, only look at a single path (but be aware that this may not be the path which your actual traffic forwards over)


## Tracerout and MPLS
* If MPLS is used … there might be ICMP tunneling. Weeeeird.

## Factoids
* default starting probe port is 33434 = 2¹⁵ + 666
