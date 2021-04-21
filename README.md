# AzNetworkTool CLI

AzNetworkTool CLI extends [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) for network operationnal needs.

This CLI helps us daily to:
* Find to which of our Azure resource(s) belong an IP Address, whether public or private. *NIC, (I|E)LB, Redis & Public IPs supported*.
* Find available subnets in a virtual network.
* Find an address space when we to create a virtual Network that not overlap with existing virtual networks. Useful when we need to peer Virtual Networks.

## Installation

```bash
git clone https://github.com/michelin/AzNetworkTool.git
```

### Prerequisites

- Bash
- [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli)
- [Azure CLI Resource Graph extension](https://docs.microsoft.com/en-US/azure/governance/resource-graph/first-query-azurecli#use-azure-cloud-shell)
- [Python 3.9](https://www.python.org/)
- [Python ipaddress library](https://pypi.org/project/ipaddress/)
- [jq](https://stedolan.github.io/jq/download/)
- [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)


## Usage

```bash
./AzNetworkTool

AzNetworkTool
Version: 0.1.0

Usage: AzNetworkTool [command]

Commands:
  what-is-this-ip                 Get Azure Resource associated to a public or private IP address.
  vnet-available-subnets          Get available subnets inside a VNET
  vnet-addrespace-wo-overlap      Get available VNET address spaces that will not overlap with existings
  *                               Help
```

### What Is This Ip
 * Check if an IP address is used. If so, which resource is using it

```bash
./AzNetworkTool what-is-this-ip 10.224.192.53
	-> NIC found:
049118e2-4814-401b-a34d-a67a35abc6a9	myresource_group	myapp-privateendpoint.nic.458ed4c9-85de-412a-bd6c-8361f1aad10c	10.224.192.53

./AzNetworkTool what-is-this-ip 10.224.100.165
	-> Redis found:
52cfe19f-528c-4e57-9a6e-019f546af4d2	myresource_group	myapp2-redis	10.224.100.165

./AzNetworkTool what-is-this-ip 10.224.255.253
IP not found!
```

### Available Subnets inside a Virtual Network
 * Find available subnets inside a Virtual Network.

```bash
$ ./AzNetworkTool vnet-available-subnets /subscriptions/<SUBSCRIPTIONID>/resourceGroups/<RESOURCEGROUP>/providers/Microsoft.Network/virtualNetworks/<VIRTUALNETWORKNAME>
Available ranges - processing in progress ...
['10.224.195.72/29', '10.224.195.96/27', '10.224.118.0/23']
```



### Available Address Spaces that will not overlap with existing VNETs
 * Get available VNET address spaces that will not overlap with existings. `10.224.0.0/24` is here the address range of an Azure Virtual Datacenter

```bash
$ ./AzNetworkTool vnet-addrespace-wo-overlap 10.224.0.0/24

Available Address Space for Virtual Networks - processing in progress ...
['10.224.96.128/26', '10.224.208.0/20', '10.224.224.0/19']
```



## Source

AzNetworkTool is based on [Brot and Games CLI](https://github.com/brotandgames/bagcli).