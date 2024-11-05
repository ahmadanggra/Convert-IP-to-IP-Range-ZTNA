import ipaddress
import csv

def remove_duplicates(ip_ranges):
    data_wo_dash = []
    convert_data_wo_dash = []
    data_w_dash = []
    final_data = []
    
    # Split data with "-" into variable data_w_dash and data without "-" into variable data_wo_dash
    for j in ip_ranges:
        if '-' in j:
            data_w_dash.append(j)
        else:
            if '.' not in j:
                data_wo_dash.append(int(j))
            else:
                data_wo_dash.append(j)

    # Remove duplicate data with list(set(data_wo_dash))
    # And combine continious IP with function ip_to_range
    convert_data_wo_dash = ip_to_range(list(set(data_wo_dash)))
    
    # Combine all data
    final_data = convert_data_wo_dash + data_w_dash
    final_data.sort()
            
    return final_data

def ip_to_range(ip_list):
    # Sort the list of IP addresses
    ip_list = sorted(ip_list, key=lambda ip: ipaddress.IPv4Address(ip))

    # Convert each IP to an ipaddress object for easier manipulation
    ip_list = [ipaddress.IPv4Address(ip) for ip in ip_list]

    # Initialize the range list
    ranges = []
    
    # Start with the first IP address in the sorted list
    start_ip = ip_list[0]
    end_ip = ip_list[0]

    # Loop through the IP addresses to find consecutive ranges
    for i in range(1, len(ip_list)):
        if ip_list[i] == end_ip + 1:
            # If the current IP is consecutive, update the end IP of the range
            end_ip = ip_list[i]
        else:
            # If it's not consecutive, save the previous range and start a new one
            if start_ip == end_ip:
                ranges.append(str(start_ip))
            else:
                ranges.append(f"{start_ip}-{end_ip}")
            start_ip = ip_list[i]
            end_ip = ip_list[i]
    
    # Add the final range
    if start_ip == end_ip:
        ranges.append(str(start_ip))
    else:
        ranges.append(f"{start_ip}-{end_ip}")

    return ranges
    
def main():
    
    text = 'data.txt'
    unique_data = []
    try:
        with open(text, 'r', encoding='utf-8') as data_file:
            # Convert csv data into list
            csv_reader = csv.reader(data_file)
            ip_list = [row for row in csv_reader]
            
            # Process data using function unique_data
            unique_data = remove_duplicates(ip_list[0])
            print(','.join(str(element) for element in unique_data))
    except FileNotFoundError:
        print(f"Error: The file '{text}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")    

if __name__ == "__main__":
    main()