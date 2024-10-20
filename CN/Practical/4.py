import ipaddress
import math
def calculate_subnet_mask(ip_address, num_subnets):
 # Convert IP address to an IPv4Network object
 ip_network = ipaddress.IPv4Network(ip_address, strict=False)
 
 # Get the base subnet mask in CIDR notation
 base_mask = ip_network.prefixlen
 
 # Calculate the new subnet mask by finding how many additional bits are needed
 # log2(num_subnets) gives the number of bits to borrow for subnetting
 bits_to_borrow = math.ceil(math.log2(num_subnets))
 new_mask = base_mask + bits_to_borrow
 
 # Calculate the new subnet mask in dotted decimal notation
 subnet_mask = ipaddress.IPv4Network(f'0.0.0.0/{new_mask}').netmask
 
 # Calculate the number of subnets and hosts per subnet
 num_hosts_per_subnet = 2**(32 - new_mask) - 2 # Minus 2 for network and broadcast address
 
 return new_mask, subnet_mask, num_hosts_per_subnet
def main():
 print("Subnetting Demonstration Program")
 
 # Input IP address and the number of subnets
 ip_address = input("Enter the IP address with CIDR (e.g., 192.168.1.0/24): ")
 num_subnets = int(input("Enter the number of subnets required: "))
 
 # Calculate subnet mask and related information
 new_mask, subnet_mask, num_hosts_per_subnet = calculate_subnet_mask(ip_address, num_subnets)
 
 # Display the results
 print(f"\nCalculated Subnet Mask Information:")
 print(f"Original IP Address and CIDR: {ip_address}")
 print(f"New Subnet Mask (CIDR Notation): /{new_mask}")
 print(f"New Subnet Mask (Dotted Decimal Notation): {subnet_mask}")
 print(f"Number of Hosts per Subnet: {num_hosts_per_subnet}")
 
if __name__ == "__main__":
 main()
