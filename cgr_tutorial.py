import sys
from py_cgr_lib.py_cgr_lib import Contact
from py_cgr_lib.py_cgr_lib import Route
from py_cgr_lib.py_cgr_lib import Bundle
from py_cgr_lib.py_cgr_lib import cp_load
from py_cgr_lib.py_cgr_lib import cgr_dijkstra
from py_cgr_lib.py_cgr_lib import cgr_anchor
from py_cgr_lib.py_cgr_lib import cgr_yen
from py_cgr_lib.py_cgr_lib import cgr_depth
from py_cgr_lib.py_cgr_lib import cgr_depleted
from py_cgr_lib.py_cgr_lib import cgr_ended
from py_cgr_lib.py_cgr_lib import fwd_candidate
from py_cgr_lib.py_cgr_lib import plot_routes
from py_cgr_lib.py_cgr_lib import plot_contact_graph
from random import randint
source = 9      # source node Houston
destination = 1 # destination node ISS
curr_time = 0   # Current time

contact_plan = cp_load('./contact_plans/9node_mars.txt',1000)
print(contact_plan)
print("---dijkstra---")
root_contact = Contact(source, source, 0, sys.maxsize, 100, 1.0, 0)  # root contact
root_contact.arrival_time = curr_time
route = cgr_dijkstra(root_contact, destination, contact_plan)
print(route)
# dijkstra returns a single (best) route from contact plan
# print("---dijkstra---")
# for curr_time in range(4401, 151296, 200):
#     root_contact = Contact(source, source, 0, sys.maxsize, 100, 1.0, 0)  # root contact
#     root_contact.arrival_time = curr_time
#     route = cgr_dijkstra(root_contact, destination, contact_plan)
#     print(route)

# anchor is a failed attempt to find all routes
# print("---anchor---")
# for contact in contact_plan:
#     contact.clear_dijkstra_working_area()
#     contact.clear_management_working_area()
# routes = cgr_anchor(source, destination, curr_time, contact_plan)
# for route in routes:
#     print(route)

# yens returns the best K=10 routes, or less
print("---yen---")
for curr_time in range(4401, 151296, 200):
    for contact in contact_plan:
        contact.clear_dijkstra_working_area()
        contact.clear_management_working_area()
    routes = cgr_yen(source, destination, curr_time, contact_plan, 10)
    plot_routes('cgryen_route', contact_plan, routes, source, destination)
    # for route in routes:
    #     print(route)
    print("---candidate---")
    excluded_nodes = []
    bundle = Bundle(src=2, dst=5, size=randint(100, 1000), deadline=72000, priority=0)
    candidate_routes = fwd_candidate(curr_time=curr_time, curr_node=source, contact_plan=contact_plan,
                                     bundle=bundle, routes=routes, excluded_nodes=excluded_nodes)
    for route in candidate_routes:
        print("current_time", curr_time, route)
#
# # deph first returns all routes in the plan
# print("---depth---")
# for contact in contact_plan:
#     contact.clear_dijkstra_working_area()
#     contact.clear_management_working_area()
# routes = cgr_depth(source, destination, contact_plan)
# for route in routes:
#     print(route)
#
# # depleted removes first depleted contact between dijkstra calls
# print("---depleted---")
# for contact in contact_plan:
#     contact.clear_dijkstra_working_area()
#     contact.clear_management_working_area()
# routes = cgr_depleted(source, destination, curr_time, contact_plan)
# for route in routes:
#     print(route)
#
# # ended removes first ending contact between dijkstra calls
# print("---ended---")
# for contact in contact_plan:
#     contact.clear_dijkstra_working_area()
#     contact.clear_management_working_area()
# routes = cgr_ended(source, destination, curr_time, contact_plan)
# for route in routes:
#     print(route)

# get candidate routes to forward bundle
# print("---candidate---")
# excluded_nodes = []
# bundle = Bundle(src=2, dst=5, size=2, deadline=50, priority=0)
# candidate_routes = fwd_candidate(curr_time=curr_time, curr_node=2, contact_plan=contact_plan,
#                                  bundle=bundle, routes=routes, excluded_nodes=excluded_nodes)
# plot_routes('candidata_route', contact_plan, candidate_routes, 2, 5)
# for route in candidate_routes:
#     print(route)

