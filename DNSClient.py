import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '127.0.0.1'
real_name_server = '8.8.8.8'  # Public DNS server for testing

# Create a list of domain names to query - use the same list from the DNS Server
domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']


# Define a function to query the local DNS server for the IP address of a given domain name
def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answers = resolver.resolve(domain, question_type)  # provide the domain and question_type
    ip_addresses = [answer.to_text() for answer in answers]
    return ip_addresses


# Define a function to query a public DNS server for the IP address of a given domain name
def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.resolve(domain, question_type)  # provide the domain and question_type
    ip_addresses = [answer.to_text() for answer in answers]
    return ip_addresses


# Define a function to compare the results from the local and public DNS servers for each domain name in the list
def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_ip_addresses = query_local_dns_server(domain_name, question_type)
        public_ip_addresses = query_dns_server(domain_name, question_type)
        if set(local_ip_addresses) != set(public_ip_addresses):
            return False
    return True


# Define a function to print the results from querying both the local and public DNS servers for each domain name in the domainList
def local_external_DNS_output(question_type):
    print("Local DNS Server")
    for domain_name in domainList:
        ip_addresses = query_local_dns_server(domain_name, question_type)
        print(f"The IP address(es) of {domain_name} on local DNS is {', '.join(ip_addresses)}")

    print("\nPublic DNS Server")
    for domain_name in domainList:
        ip_addresses = query_dns_server(domain_name, question_type)
        print(f"The IP address(es) of {domain_name} on public DNS is {', '.join(ip_addresses)}")


if __name__ == '__main__':
    # Set the type of DNS query to be performed
    question_type = 'A'

    # Call the function to print the results from querying both DNS servers
    local_external_DNS_output(question_type)

    # Call the function to compare the results from both DNS servers and print the result
    match_result = compare_dns_servers(domainList, question_type)
    print("Do local and public DNS servers return the same results for all domains?", match_result)
