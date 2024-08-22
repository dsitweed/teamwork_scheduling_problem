from typing import List
import heapq


class ParkingRequest:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.slot = None

def schedule_parking(requests: List[ParkingRequest], num_slot: int = 1):
  scheduled_requests = []

  requests.sort(key=lambda x: x.start)

  parking_heap = []

  for request in requests:
    # Remove expired requests from the heap (end time < request.start time)
    while parking_heap and parking_heap[0] <= request.start:
      heapq.heappop(parking_heap)

    if len(parking_heap) < num_slot:
      heapq.heappush(parking_heap, request.end)
      scheduled_requests.append(request)
      request.slot = len(parking_heap)
      print(f"Parking request from {request.start} to {request.end} (slot {request.slot})")

  return scheduled_requests

def find_available_slot(scheduled_requests: List[ParkingRequest], request: ParkingRequest) -> bool:
  last_request = scheduled_requests[-1] if scheduled_requests else None
  if last_request and last_request.end > request.start:
    return False

  return True

# Utility function

def can_parking():
  True

def get_available_slots(scheduled_requests, start, end):
  return True




if __name__ == "__main__":
  requests = [
    ParkingRequest(start=1, end=4),
    ParkingRequest(start=3, end=5),
    ParkingRequest(start=0, end=6),
    ParkingRequest(start=5, end=7),
    ParkingRequest(start=3, end=8),
    ParkingRequest(start=5, end=9),
    ParkingRequest(start=6, end=10),
    ParkingRequest(start=8, end=11),
    ParkingRequest(start=10, end=15),
    ParkingRequest(start=12, end=18),
    ParkingRequest(start=20, end=25),
    ParkingRequest(start=22, end=28),
  ]

  print("Requesting Parking requests...")
  print("Total Requests:", len(requests))
  for request in requests:
    print(f"From: {request.start} to {request.end}")

  scheduled_requests = schedule_parking(requests, 5)
  print("Total Scheduled Requests:", len(scheduled_requests))
  print("Scheduled Parking Requests:")
  for request in scheduled_requests:
    print(f"From {request.start} to {request.end}, at slot: {request.slot}")
