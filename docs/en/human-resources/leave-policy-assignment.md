
# Leave Policy Assignment




> Introduced in Version 13
> 
> 

Leave Policy Assignment in Frappe HR is used to assign leaves to employees based on created policies. To access Leave policy assignment, go to:


> Home > Human Resources > Leaves > Leave Policy Assignment
> 
> 

## 1. Prerequisites

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](/docs/en/human-resources/employee)
* [Leave Policy](/docs/en/human-resources/leave-policy)

## 2. How to create a Leave Policy Assignment

1. Go to Leave Policy Assignment, click on New.
2. Select Employee and Leave Policy.
3. Select Assignment based on the following as needed:


	* If "Assignment based on" is set to Leave Period, you need to select the applicable Leave Period. The Effective From and Effective To dates will be set automatically based on the Leave Period selected.
	* If "Assignment based on" is set to Joining Date, the Effective From date will be set to the employee's Date of Joining.
	* If "Assignment based on" is left blank, then you will have to set the Effective From and Effective To date manually.
4. Save and Submit.

![Leave Policy Assignment](/files/leave-policy-assignment.png)

On submission, Leave Allocation documents would be created automatically based on the [Leave Policy](/docs/en/human-resources/leave-policy) as shown below.

![Leave Allocations](/files/granted-leaves.png)

## 3. Features

### 3.1 Bulk Leave Policy Assignment


> From Version 15 onwards: Use the [Leave Control Panel](https://frappehr.com/docs/v14/en/leave-control-panel) for Bulk Leave Policy Assignment
> 
> 

Frappe HR also allows creating multiple Leave Policy Assignment for multiple employees.

1. Go to Leave Policy Assignment list, click on Bulk Leave Policy Assignment.
2. Dialog Will appear, Select Employee. You can filter Employee based on Company and Department or You can also use standard filters by clicking Add Filters.
3. Select Leave Policy and Effective From and Effective To dates.
4. Click on Assign.

![Bulk Leave Policy Assignment](/files/bulk-leave-policy-assignment.png)




