from lumen.plan import plan

for layout in ('radial', 'layered'):
    print(layout, plan(['n1'], layout=layout))
