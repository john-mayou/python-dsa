from __future__ import annotations
import threading
import time

class User:
    def __init__(self, name: str):
        self.name = name

class Packet:
    _id_counter = 1
    
    def __init__(self, content: str):
        self.content = content
        self.id = Packet._id_counter
        Packet._id_counter += 1

class Internet:
    
    POLL_INTERVAL = 0.1
    
    def __init__(self):
        self.computers = {}
        self.packets = {}
        self.stop_event = threading.Event()
        self.thread = None
    
    def add_computer(self, computer: Computer):
        self.computers[computer.user] = computer
        
    def send_packet(self, recipient: User, packet: Packet):
        if recipient in self.packets:
            self.packets[recipient].append(packet)
        else:
            self.packets[recipient] = [packet]
            
    def poll_packets(self):
        while not self.stop_event.is_set():
            print("Polling packets...")
            if self.packets:
                for recipient, packets in self.packets.items():
                    print(f"Found {len(packets)} packets for {recipient.name}")
                    if recipient not in self.computers:
                        raise RuntimeError(f"recipient does not have a registered computer: {recipient}")
                    computer = self.computers[recipient]
                    for packet in packets:
                        computer.receive_packet(packet)
                self.packets = {}
            time.sleep(Internet.POLL_INTERVAL)
        print("Stop event detected.")
            
    def start_polling(self):
        print("Starting poll.")
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.poll_packets, daemon=True)
        self.thread.start()
        print("Poll started.")
        
    def stop_polling(self):
        print("Stopping poll.")
        self.stop_event.set()
        if self.thread:
            self.thread.join() # wait for it to fully stop
        print("Poll stopped.")
    
class Computer:
    def __init__(self, internet: Internet, user: User):
        self.internet = internet
        self.user = user
        self.packets = {}
        internet.add_computer(self)
        
    def send_packet(self, recipient: User, packet: Packet):
        self.internet.send_packet(recipient, packet)
    
    def receive_packet(self, packet: Packet):
        print(f"Packet #{packet.id} received by {self.user.name}")
        self.packets[packet.id] = packet
    
    def list_packet_ids(self) -> list[Packet]:
        return list(self.packets.keys())
        
    def read_packet(self, id: int) -> str:
        if id not in self.packets:
            raise RuntimeError(f"packet id {id} not in packets")
        return self.packets[id].content
    
    def delete_packet(self, id: int):
        self.packets.pop(id)
    
def main():
    internet = Internet()
    internet.start_polling()
    
    a = User('Alice')
    b = User('Bob')
    
    a_comp = Computer(internet, a)
    b_comp = Computer(internet, b)
    
    a_comp.send_packet(b, Packet('hello'))
    a_comp.send_packet(b, Packet('world'))
    
    time.sleep(Internet.POLL_INTERVAL)
    
    assert(b_comp.list_packet_ids() == [1, 2])
    assert(b_comp.read_packet(1) == 'hello')
    b_comp.delete_packet(1)
    assert(b_comp.read_packet(2) == 'world')
    b_comp.delete_packet(2)
    assert(b_comp.list_packet_ids() == [])
    
    # ensure not re-delivered
    time.sleep(Internet.POLL_INTERVAL)
    assert(b_comp.list_packet_ids() == [])
    
    internet.stop_polling()
    
def test_main(): main()