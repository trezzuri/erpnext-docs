
# Managing Multi-level BOM



Consider a scenario where your manufacturing process involves producing sub-assembly items before the final product. In this case, how should you manage the BOM?


First of all, you need to have BOMs for the sub-assemblies, then these BOMs should be linked to the BOM of the final finished product. In the following screenshot, you can see that the BOM for Brush Bristles (subassembly) is linked to the BOM of the Shaving Brush (final product). This is seen in the Materials table in the Bill of Materials master.


![Multi-level BOM](/files/multi-bom.png)


The 'Materials' table will only show the sub-assemblies while the 'Materials Required (Exploded)' table will show all the raw materials required to manufacture the final product.


BOM materials table where sub-assembly is shown:
![Multi-level BOM](/files/bom-materials.png)


In the exploded view only the raw materials are shown:
![Multi-level BOM](/files/bom-materials-exploded.png)


To use multi-level BOM in a Work Order, enable the 'Use Multi-Level BOM' checkbox. This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately disable this checkbox.


Let's consider another example to understand this better where a computer is being assembled. The hard disk and DVD drive are also being manufactured and are the sub-assemblies. The multi-level or nested BOM will look like this:


* Personal Computer (FG Item)
	+ Mother Board
	+ SMTP
	+ Accessories and wires
	+ Hard Disk (sub-assembly)
		- Item A
		- Item B
		- Item C
	+ DVD Drive (sub-assembly)
		- Item X
		- Item Y
		- Item Z


## Caution


Exercise caution when updating the BOM of a sub-assembly. The part which includes the sub assembly with an updated BOM will need to be updated to reference the updated BOM for that part. The practical outcome of this is that changing a screw on a low level assembly will lead to a ripple of updated Bills of Material up through the BOM structure.


Using the example of the personal computer above.
Personal Computer (PC-001 with BOM-PC-001) uses Hard Disk (HDD-001 with BOM-HDD-001).
BOM-HDD-001 includes the three items shown (Item A, B and C).


If we need to exchange Item C for a new item (Item D) then we must update create BOM-HDD-002 (with Items A, B and D). The Hard Disk (HDD-001) is then updated to reference the new BOM-HDD-002. But, BOM-PC-001 is still referencing HDD-001 with BOM-HDD-001. The change from Item C to Item D will not be updated in the Exploded BOM for PC-001.


BOM-PC-002 must be created referencing HDD-001 with BOM-HDD-002 to make this update.




