from scapy.all import *
import pandas as pd
import os


def create_csv(path_s, path_d):
    packets_list = rdpcap(path_s)
    table = {}
    s_ip = []
    s_port = []
    d_ip = []
    d_port = []
    p_proto = []
    p_time = []
    p_lenght = []
    for packet in packets_list:
        if 'IP' and 'TCP' in packet:
            s_ip.append(packet['IP'].src)
            s_port.append(packet['TCP'].sport)
            d_ip.append(packet['IP'].dst)
            d_port.append(packet['TCP'].dport)
            p_proto.append(packet.proto)
            p_lenght.append(packet.wirelen)
            p_time.append(packet.time)
    table['Source IP'] = s_ip
    table['Source Port'] = s_port
    table['Destination IP'] = d_ip
    table['Destination Port'] = d_port
    table['Protocol'] = p_proto
    table['Lenght'] = p_lenght
    table['Time'] = p_time

    data_frame = pd.DataFrame(data=table)
    data_frame.to_csv(path_or_buf=path_d + os.path.split(path_s)[1] + '.csv', index_label='index')
    return 0
