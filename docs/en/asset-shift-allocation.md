
# Asset Shift Allocation



The Asset Shift Allocation feature lets you change the shifts of an asset (with [shift depreciation](https://docs.erpnext.com/docs/user/manual/en/asset-asset#3-1-depreciation:~:text=Depreciate%20based%20on%20shifts) enabled) for a particular period and the remaining shifts are automatically adjusted by the system.

Let's go through an example.

The following is the depreciation schedule of an asset with shift depreciation enabled, depreciation method as Straight Line, total number of depreciations as 12 and frequency of depreciation as 1. All the shifts were single by default and depreciation entries have been made for the first 5 months.

![](/files/00creuc.png)![]()

Here are the shift factors defined:

![](/files/WXQYhRA.png)![]()  


Next, we'll go to the Asset Shift Allocation doctype, enter the asset's name and save. The current depreciation schedule is fetched so that we can edit the shifts. Let's change the shift for the 6th row to Triple.

![](/files/HZDN3lo.png)![]()  


When you hit save after changing, notice the last row getting removed automatically in order to preserve the total number of shifts.

![](/files/RgfAzrs.png)![]()  


If you had changed the shift in the 6th row to Double, the shift in the last row would have changed to Half.

Once you're sure about the depreciation schedule created, hit submit and a new depreciation schedule is generated for the asset.




