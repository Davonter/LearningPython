#!/usr/bin/python3

'''
ping
'''

import os, sys, socket, struct, select, time

if sys.platform == "win32":
	# On windows, the best timer is time.clock()
	default_timer = time.clock
else:
	# On the most other platform, the best timer is time.time()
	default_timer = time.time
	
ICMP_ECHO_REQUEST = 8

def checksum(source_string):
	sum = 0
	countTo = (len(source_string)/2)*2
	count = 0
	while count < countTo:
		thisVal = ord(source_string[count+1]*256 + ord(source_string[count]))
		sum += thisVal
		sum = sum & 0xffffffff
		count = count + 2
		
	if countTo < len(source_string):
		sum = sum + ord(source_string[len(source_string) - 1])
		sum = sum & 0xffffffff
		
	sum = (sum >> 16) + (sum & 0xffff)
	sum = sum+ (sum >> 16)
	
	answer = ~sum
	answer = answer & 0xFFFF
	
	answer = answer >> 8 | (answer << 8 & 0xff00)
	
	return answer
	
def receive_one_ping(my_socket, ID, timeout):
	'''
	Receive the ping from the socket
	'''
	timeLeft = timeout
	while True:
		startedSelect = default_timer()
		whatReady = select.select([my_socket], [], [], timeLeft)
		howLongInSelect = (default_timer() - startedSelect)
		
		if whatReady = []:	# timeout
			return 
		
		
		
		
		
	
def send_one_ping(my_socket, dest_addr, ID):
	'''
	Send one ping to the given >dest_addr<
	'''
	dest_addr = socket.gethostbyname(dest_addr)
	
	# Header is type(8), code(8), checksum(8), id(16), sequence(16)
	my_checksum = 0
	
	# Make a  dummy header with a 0 checksum
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
	bytesInDouble = struct.calcsize("d")
	data = (192 - bytesInDouble) * "Q"
	data = struct.pack("d", default_timer()) + data
	
	#Calculate the checksum on the data and the dummy header
	my_checksum = checksum(header + data)
	
	# Now that wo have the right checksum, we put that in. It's just easier
	# to make up a new header than to stuff it into the dummy
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1)
	packet = header + data
	my_socket.sendto(packet, (dest_addr, 1))
	
	
def do_one(dest_addr, timeout):
	icmp = socket.getprotobyname("icmp")
	try:
		my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
	except socket.error, (errno, msg):
		if errno == 1:
			msg = msg + (
				" - Note that ICMP messsage can only be sent from success"
				" running as root"
			)
			raise socket.error(msg)
		raise
		
	my_ID = os.getpid() & 0xFFFF
	send_one_ping(my_socket, my_ID, timeout)
	
	my_socket.close()
	return delay
	
def verbose_ping(dest_addr, timeout=2, count=4):
	for i in xrange(count):
		print("ping %s..." % dest_addr)
		try:
			delay = do_one(dest_addr, timeout)
		except socket.gaierror, e:
			print("Failed. (socket error: '%s')" % e[1])
			break
			
		if delay == None:
			print("failed. (timeout within %ssec.)" % timeout)
		else:
			### 成功则返回延时时间
			delay = delay * 1000
			print("Get ping in %0.4fms" % delay)
	print("\n")
	
if __name__ == "__main__":
	verbose_ping("baidu.com")