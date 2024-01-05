
# Multiple finished goods with single raw material



In many Manufacturing industries deal with a scenario where they use one RM (Raw Material) & produce multiple Finish goods. Most of the chemical manufacturing industries you can find this business use-case. Now how you can map this use-case in ERPNext? Lets take an example of Oil manufacturing Industry where from Crude oil multiple products are produced like Petrol, Gas, Diesel, Kerosene etc.  
* First create an Item master where crude oil will be RM & Petrol, Gas, Diesel, Kerosene etc. will be your FG. Here every product can also have different UOM.

  
* After creation of item master create a BOM for any of the FG you are going to produce from Crude oil (RM). Here I have created BOM of Petrol for 25 litres where I am going to use Crude oil (RM) of qty. 100 litres. Rest of the FG like Gas, Diesel & Kerosene I have added in Scrap section.

  
  
![](/files/1VHaiPf.png)  
![](/files/mg68Dbr.png)  
* While creating a BOM you can add operations as well & run your production cycle (Work order) accordingly.

  
* After completion of work-order at the time of Back-flush entry your Raw material will get consumed & you will have multiple finish goods.





