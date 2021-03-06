from testOpera.table.demoModels import Demo

demo = Demo()
lj_demo = Demo()
a = demo.orm.find().append('WHERE 1=2').end()
r1 = demo.orm.find().end()
r2 = demo.orm.find().where(id=1).end()
r3 = demo.orm.find().order_by('id').end()
r4 = demo.orm.find('*', h_func=True).alias('d1').left_join(lj_demo, 'd2').on('d1.id', 'd2.id').end()
r5 = demo.orm.find().group_by('id').end()
r6 = demo.orm.find().order_by('id').desc().end()
r7 = demo.orm.find().limit(1).end()
r8 = demo.orm.filter(id__in=[1, 2, 3, 4])
r9 = demo.orm.top().end()
print('r1', type(r1), r1)
print('r2', type(r2), r2)
print('r3', type(r3), r3)
print('r4', type(r4), r4)
print('r5', type(r5), r5)
print('r6', type(r6), r6)
print('r7', type(r7), r7)
print('r8', type(r8), r8)
print('r9', type(r9), r9)
