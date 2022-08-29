## DNS Zone Transfer

A DNS Zone Transfer is the replication of a name server record from one DNS server to another. In the late 1990’s it became an industry best practice to only allow Zone Transfers among DNS servers. However there are always late adopters, and you only need one link in the DNS chain to be broken.

With all of the DNS information, it is possible to determine a lot about the network that uses that domain. In addition to discovering internal addressing schemes, it is possible to determine what specific hosts are used for analyzing zone information. Moreover, you can find a target’s primary name server.

This script will allow us to query for an array of name servers (name server) and resolve the IP for a particular target. We will run one query to the name servers and double loop to resolve for a list of IPs in each NS and request a transfer.