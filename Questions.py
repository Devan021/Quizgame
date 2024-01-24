
Q_and_A = [['The IETF standards documents are called ________:', ["RFC", "RCF", "ID", "DFC"], "RFC"],
		   ['In the layer hierarchy as the data packet moves from the upper to the lower layers, headers are ___________ ', ["Added","Removed","Rearranged", "Modified"], "Added"],
		   ['A _______ is the physical path over which a message travels.', ["Path", "Medium", "Protocol", "Route"], "Medium"],
		   ['Which of this is not a network edge device?', ["PC", "Smartphones", "Servers", "Switches"], "Switches"],
		   ['A _________ set of rules that governs data communication.', ["Protocols", "Standards", "RFCs", "Servers"], "Protocols"],
		   ['In computer network nodes are _________ ', ["the computer that originates the data", "the computer that routes the data", "the computer that terminates the data", "all of the mentioned"], "all of the mentioned"],
		   ['A __________ is a device that forwards packets between networks by processing the routing information included in the packet.', ["bridge", "firewall", "router", "hub"], "router"],
		   ['Network congestion occurs _________ ', ["in case of traffic overloading", "when a system terminates", "when connection between two nodes terminates", "in case of transfer failure"], "in case of traffic overloading"],
		   ['HFC contains _______ ', ["Fibre cable", "Coaxial cable", "A combination of Fibre cable and Coaxial cable", "Twisted Pair Cable"], "A combination of Fibre cable and Coaxial cable"],
		   ['How many layers are present in the Internet protocol stack (TCP/IP model)?',["5", "7", "6", "10"], "5"],
		   ['The number of layers in ISO OSI reference model is __________ ', ["5", "7", "6", "10"], "7"],
		   ['Which of the following layers is an addition to OSI model when compared with TCP IP model?',["Application layer", "Presentation layer", "Session layer", "Session and Presentation layer"],"Session and Presentation layer"],
		   ['Application layer is implemented in ____________ ', ["End system", "NIC", "Ethernet", "Packet transport"], "End system"],
		   ['Transport layer is implemented in ______________', ["End system", "NIC", "Ethernet", "Signal transmission"], "End system"],
		   ['The functionalities of the presentation layer include ____________', ["Data compression", "Data encryption", "Data description", "All of the mentioned"], "All of the mentioned"],
		   ['Delimiting and synchronization of data exchange is provided by __________ ', ["Application layer", "Session layer", "Transport layer", "Link layer"], "Session layer"],
		   ['In OSI model, when data is sent from device A to device B, the 5th layer to receive data at B is _________  ', ["Application layer", "Transport layer", "Link layer", "Session layer"], "Session layer"],
		   ['In TCP IP Model, when data is sent from device A to device B, the 5th layer to receive data at B is ____________ ', ["Application layer", "Transport layer", "Link layer", "Session layer"], "Application layer"],
		   ['In the OSI model, as a data packet moves from the lower to the upper layers, headers are _______ ', ["Added", "Removed", "Rearranged", "Randomized"], "Removed"],
		   ['OSI stands for __________', ["open system interconnection", "operating system interface", "optical service implementation", "open service Internet"], "open system interconnection"],
		   ['Which layer is responsible for process to process delivery in a general network model? ', ["network layer", "transport layer", "session layer", "data link layer"], "transport layer"],
		   ['Which address is used to identify a process on a host by the transport layer?', ["physical address", "logical address", "port address", "specific address"], "port address"],
		   ['Transmission data rate is decided by ____________ ', ["network layer", "physical layer", "data link layer", "transport layer"], "physical layer"],
		   ['Which is not a application layer protocol?', ["HTTP", "SMTP", "FTP", "TCP"], "TCP"],
		   ['The packet of information at the application layer is called __________ ', ["Packet", "Message", "Segment", "Frame"], "Message"],
		   ['Which one of the following is an architecture paradigm?', ["Peer to peer", "Client-server", "HTTP", "Both Peer-to-Peer & Client-Server"], "Both Peer-to-Peer & Client-Server"],
		   ['Application layer offers _______ service.', ["End to end", "Process to process", "Both End to end and Process to process", "None of the mentioned"], "End to end"],
		   ['E-mail is _________', ["Loss-tolerant application", "Bandwidth-sensitive application", "Elastic application", "None of the mentioned"], "Elastic application"],
		   ['Which of the following is an application layer service?', ["Network virtual terminal", "File transfer, access, and management", "Mail service", "All of the mentioned"], "All of the mentioned"],
		   ['To deliver a message to the correct application program running on a host, the _______ address must be consulted.', ["IP", "MAC", "Port", "None of the mentioned"], "Port"],
		   ['Electronic mail uses which Application layer protocol?', ["SMTP", "HTTP", "FTP", "SIP"], "SMTP"],
		   ['The ____________ translates internet domain and host names to IP address.', ["domain name system", "routing information protocol", "network time protocol", "internet relay chat"], "domain name system"],
		   ['Application layer protocol defines ____________', ["types of messages exchanged", "message format, syntax and semantics", "rules for when and how processes send and respond to messages", "all of the mentioned"], "all of the mentioned"],
		   ['Which one of the following protocol delivers/stores mail to reciever server?', ["simple mail transfer protocol", "post office protocol", "internet mail access protocol", "hypertext transfer protocol"], "simple mail transfer protocol"],
		   ['Which one of the following is an internet standard protocol for managing devices on IP network?', ["dynamic host configuration protocol", "simple network management protocol", "internet message access protocol", "media gateway protocol"], "simple network management protocol"],
		   ['Which one of the following is not an application layer protocol?', ["media gateway protocol", "dynamic host configuration protocol", "resource reservation protocol", "session initiation protocol"], "resource reservation protocol"],
		   ['Which one of the following is not correct?', ["Application layer protocols are used by both source and destination devices during a communication session", "HTTP is a session layer protocol", "TCP is an application layer protocol", "All of the mentioned"], "All of the mentioned"],
		   ['When displaying a web page, the application layer uses the _____________', ["HTTP protocol", "FTP protocol", "SMTP protocol", "TCP protocol"], "HTTP protocol"],
		   ['A DNS client is called _________ ', ["DNS updater", "DNS resolver", "DNS handler", "none of the mentioned"], "DNS resolver"],
		   ['DNS database contains _______ ', ["name server records", "hostname-to-address records", "hostname aliases", "all of the mentioned"], "all of the mentioned"],
		   ['If a server has no clue about where to find the address for a hostname then _______ ', ["server asks to the root server", "server asks to its adjcent server", "request is not processed", "none of the mentioned"], "server asks to the root server"],
		   ['Which one of the following allows client to update their DNS entry as their IP address change?', ["dynamic DNS", "mail transfer agent", "authoritative name server", "none of the mentioned"], "dynamic DNS"],
		   ['The right to use a domain name is delegated by domain name registers which are accredited by _______ ', ["internet architecture board", "internet society", "internet research task force", "internet corporation for assigned names and numbers"], "internet corporation for assigned names and numbers"],
		   ['The domain name system is maintained by _______', ["distributed database system", "a single server", "a single computer", "none of the mentioned"], "distributed database system"],
		   ['The time taken by a packet to travel from client to server and then back to the client is called __________ ', ["STT", "RTT", "PTT", "JTT"], "RTT"],
		   ['The HTTP request message is sent in _________ part of three-way handshake.', ["First", "Second", "Third", "Fourth"], "Third"],
		   ['In the process of fetching a web page from a server the HTTP request/response takes __________ RTTs.', ["2", "1", "4", "3"], "1"],
		   ['The first line of HTTP request message is called _____________ ', ["Request line", "Header line", "Status line", "Entity line"], "Request line"],
		   ['The values GET, POST, HEAD etc are specified in ____________ of HTTP message', ["Request line", "Header line", "Status line", "Entity body"], "Request line"],
		   ['The __________ method when used in the method field, leaves entity body empty.', ["POST", "SEND", "GET", "PUT"], "GET"],
		   ['The conditional GET mechanism ', ["Imposes conditions on the objects to be requested", "Limits the number of responses from a server", "Helps to keep a cache upto date", "None of the mentioned"], "Helps to keep a cache upto date"],
		   ['HTTP is ________ protocol.', ["application layer", "transport layer", "network layer", "data link layer"], "application layer"],
		   ['In the network HTTP resources are located by ', ["uniform resource identifier", "unique resource locator", "unique resource identifier", "union resource locator"], "uniform resource identifier"],
		   ['FTP server listens for connection on port number ____________ ', ["20", "21", "22", "23"], "21"],
		   ['Expansion of FTP is __________ ', ["Fine Transfer Protocol", "File Transfer Protocol", "First Transfer Protocol", "Fast Transfer Protocol"], "File Transfer Protocol"],
		   ['FTP is built on _____ architecture.', ["Client-server", "P2P", "Data centric", "Service oriented"], "Client-server"],
		   ['The password is sent to the server using ________ command ', ["PASSWD", "PASS", "PASSWORD", "PWORD"], "PASS"],
		   ['Expansion of SMTP is ________ ', ["Simple Mail Transfer Protocol", "Simple Message Transfer Protocol", "Simple Mail Transmission Protocol", "Simple Message Transmission Protocol"], "Simple Mail Transfer Protocol"],
		   ['User agent does not support this ___________ ', ["Composing messages", "Reading messages", "Replying messages", "Routing messages"], "Routing messages"],
		   ['Which of the following is false with respect to TCP?', ["Connection-oriented", "Process-to-process", "Transport layer protocol", "Unreliable"], "Unreliable"],
		   ['In TCP, sending and receiving data is done as _______ ', ["Stream of bytes", "Sequence of characters", "Lines of data", "Packets"], "Stream of bytes"],
		   ['To achieve reliable transport in TCP, ___________ is used to check the safe and sound arrival of data.', ["Packet", "Buffer", "Segment", "Acknowledgment"], "Acknowledgment"],
		   ['The receiver of the data controls the amount of data that are to be sent by the sender is referred to as ___________', ["Flow control", "Error control", "Congestion control", "Error detection"], "Flow control"],
		   ['Connection establishment in TCP is done by which mechanism? ', ["Flow control", "Three-Way Handshaking", "Forwarding", "Synchronization"], "Three-Way Handshaking"],
		   ['The sizes of source and destination port address in TCP header are ___________ respectively.', ["16-bits and 32-bits", "16-bits and 16-bits", "32-bits and 16-bits", "32-bits and 32-bits"], "16-bits and 16-bits"],
		   ['Which of the following is false with respect to UDP?', ["Connection-oriented", "Unreliable", "Transport layer protocol", "Low overhead"], "Connection-oriented"],
		   ['What is the main advantage of UDP?', ["More overload", "Reliable", "Low overhead", "Fast"], "Low overhead"],
		   ['What is the header size of a UDP packet?', ["8 bytes", "8 bits", "16 bytes", "124 bits"], "8 bytes"],
		   ['The term that is used to place packet in its route to its destination is called __________ ', ["Delayed", "Urgent", "Forwarding", "Delivering"], "Forwarding"],
		   ['What is WPA?', ["wi-fi protected access", "wired protected access", "wired process access", "wi-fi process access"], "wi-fi protected access"],
		   ['What is internet?', ["a single network", "a vast collection of different networks", "interconnection of local area networks", "interconnection of wide area networks"], "a vast collection of different networks"],
		   ['To join the internet, the computer has to be connected to a _________ ', ["internet architecture board", "internet society", "internet service provider", "different computer"], "internet service provider"],
		   ['The size of an IP address in IPv6 is _________ ', ["32 bits", "64 bits", "128 bits", "265 bits"], "128 bits"],
		   ['Internet works on _______ ', ["packet switching", "circuit switching", "both packet switching and circuit switching", "data switching"], "packet switching"],
		   ['Multiple processes on destinations at transport layer are identified by __________', ["Mac address", "Port number", "Host number", "Host address"], "Port number"],
		   ['Range of port numbers in Internet model is __________', ["0 and 32,765(8-bit)", "0 and 32,765(16-bit)", "0 and 65,535(32-bit)", "0 and 65,535(16-bit)"], "0 and 65,535(16-bit)"],
		   ['The combination of an IP address and port number is called as ________ ', ["Socket address", "Port address", "MAC address", "Host address"], "Socket address"],
		   ['Which of the following is false with respect to Connectionless service of transport layer protocol?', ["Packets are not numbered", "Packets are not delayed", "No acknowledgement", "Packet may arrive out of sequence"], "Packets are not delayed"],
		   ['URL stands for ________ ', ["unique reference label", "uniform reference label", "uniform resource locator", "unique resource locator"], "uniform resource locator"]]