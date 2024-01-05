
# Holiday List



**Holiday List is a list which contains the dates of holidays.**

Most organizations have a standard Holiday List for their employees. However, some of them may have different holiday lists based on different Locations or Departments. In ERPNext, you can configure multiple Holiday Lists and assign them to your employees based on your requirements.

To access Holiday List, go to:


> Home > Human Resources > Leaves > Holiday List
> 
> 

## 1. How to create a Holiday List

1. Go to Holiday List, click on New.
2. Enter Holiday List Name. It can be based on the Fiscal Year or Location or Department as per the requirement.
3. Select From Date and To Date for the Holiday List.

![Holiday List](/files/holiday-list-1.png)![]()

## 2. Features

Some of the additional features in the Holiday List are as follows:

### 2.1 Adding Weekly Holidays

You can quickly add Weekly Offs in the Holiday List as follows:

1. In the 'Add Weekly Holidays' section, select the day in the Weekly Off field.
2. Click on the 'Add to Holidays' button.

![Holiday List](/files/holiday-list-2.gif)![]()  


### 2.2 Adding Local Holidays

You can quickly add local holidays to the Holiday List as follows:

1. In the 'Add Local Holidays' section, select the country.
2. Some countries have subdivisions with different or additional holidays. If you like, you can optionally select a specific subdivision.
3. Click on the 'Add to Holidays' button.

### 2.3 Adding Holidays manually

You can also add specific days manually by clicking on the 'Add row' option in the Holidays table.

![Holiday List](/files/holiday-list-3.png)![]()  


## 3. Holiday List in Company

You can set a default Holiday List at the company-level in the Company master in the 'Default Holiday List' field.

![Holiday List](/files/default-holiday-list-company.png)![]()  


## 4. Holiday List in Employee

If you have created multiple Holiday List, select a specific Holiday List for an Employee in the respective master.

When an Employee applies for Leave, the days mentioned in the Holiday List will not be counted, as they are holidays already.


> **Note:** If you have specified a Holiday List in the Employee master, then that Holiday List will be given priority as compared to the default Holiday List of the Company. You can form as many holiday lists as you wish. For example, if you have a factory, you can have one list for the factory workers and another list for office staff. You can manage between many lists by linking a Holiday List to the respective Employee.
> 
> 

## 5. Holiday List in Workstation

You can also set a Holiday List at workstation-level as shown in the screenshot below.

![Holiday List](/files/holiday-list-workstation.png)![]()  


The dates in the Holiday List tagged in the [Workstation](/docs/en/manufacturing/workstation) master will be considered as the days the Workstation will remain closed.

## 6. Related Topics

1. [Leave Allocation](/docs/en/human-resources/leave-allocation)
2. [Leave Period](/docs/en/human-resources/leave-period)
3. [Leave Policy](/docs/en/human-resources/leave-policy)
4. [HR Settings](/docs/en/human-resources/hr-settings)



