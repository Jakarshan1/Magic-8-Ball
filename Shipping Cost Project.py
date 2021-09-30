#Type the weight of the pachage/shipment below after the "="
weight = 10000
premium_ground = 125.00
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 10:
  cost_ground = 4.75 * weight + 20
elif weight >= 6:
  cost_ground = 4.00 * weight + 20.0
elif weight >= 2:
  cost_ground = 3 * weight + 20
print('Cost of Ground Shipping is ', cost_ground)
print('Cost of Premium Ground Shipping is ', premium_ground)
if weight <= 2:
  cost_drone = 4.50 * weight
elif weight > 10:
  cost_drone = 14.25 * weight
elif weight >= 6:
  cost_drone = 12 * weight
elif weight >= 2:
  cost_drone = 9 * weight
print('Cost of Drone Shipping is ', cost_drone)
print('''

Cheapest Method''')
if cost_drone < cost_ground:
  print(cost_drone)
else:
  print(premium_ground)