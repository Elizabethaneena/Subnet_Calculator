import re
import tkinter as tk
win = tk.Tk()
win.geometry("800x600")

def main_fun():
	ipaddr = ip.get() #ip address assigned to variable 
	subnet=int(subnet_add.get())
	sub_net_str=''.join(str("1"*subnet+"0"*(32-subnet))) 
	asd = re.findall('........',sub_net_str)
	lst = []
	for i in asd:
		lst.append(int(i,2)) #decimal form
	subnet_mask_ipv4 =".".join(map(str, lst))
	network_lst = []
	ip_split = list(ipaddr.split("."))
	for i in range(len(ip_split)):
		network_lst.append(int(ip_split[i]) & lst[i])
	network_address = ".".join(map(str, network_lst))
	str_inverted_subnet=''.join(str("0"*subnet+"1"*(32-subnet)))
	inverted= re.findall('........',str_inverted_subnet)
	inver_lst = []
	for i in inverted:
		inver_lst.append(int(i,2))
	broadcast_lst = []
	for i in range(len(ip_split)):
		broadcast_lst.append(int(network_lst[i]) | inver_lst[i])
	broadcast_address = ".".join(map(str, broadcast_lst))
	No_of_available_IP_address= pow(2, 32-subnet)
	useable_ip_address = No_of_available_IP_address - 2
	network_lst[3] = int(network_lst[3]) + 1 #change from 3rd location
	start_range = ".".join(map(str, network_lst))
	broadcast_lst[3] = int(broadcast_lst[3]) - 1
	end_range = ".".join(map(str, broadcast_lst)) #map from broadcast
	range1 = start_range + " - " + end_range
	new = tk.Toplevel(win)
	new.geometry("750x400")
	new.title("Calculated Results :\n")
	tk.Label(new, text="IP address : ").grid(row=0,column=0)
	tk.Label(new, text=ipaddr).grid(row=0,column=1)
	tk.Label(new, text="Subnet mask : ").grid(row=1,column=0)
	tk.Label(new, text=subnet_mask_ipv4).grid(row=1,column=1)
	tk.Label(new, text="Network address : ").grid(row=3,column=0)
	tk.Label(new, text=network_address).grid(row=3,column=1)
	tk.Label(new, text="Broadcast address : ").grid(row=4,column=0)
	tk.Label(new, text=broadcast_address).grid(row=4,column=1)
	tk.Label(new, text="Available no.of IP address :").grid(row=5,column=0)
	tk.Label(new, text=useable_ip_address).grid(row=5,column=1)
	tk.Label(new, text="Range : ").grid(row=6,column=0)
	tk.Label(new, text=range1).grid(row=6,column=1)
def clear():
	ip.set('')
	subnet_add.set('')

win.title('GUI Subnet Calculator')
win.geometry('600x400')
win.config(bg='#FFFFFF') #background color

tk.Label(win, text="Enter IP address : ", fg="black").grid(row=0,column=0) 
tk.Label(win, text="Enter Subnetmask : ", fg="black").grid(row=1,column=0)
ip =tk.StringVar(win)
subnet_add=tk.StringVar(win)
ip_addr = tk.Entry(win, bd =5,textvariable=ip).grid(row=0,column=1) 
sub_net_mask = tk.Entry(win, bd =5,textvariable=subnet_add).grid(row=1,column=1)

tk.Button(win,text="Calculate",command=main_fun).grid(row=2,column=0)
tk.Button(win,text="Clear",command=clear).grid(row=2,column=1) 

win.mainloop()
