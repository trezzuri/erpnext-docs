
# Shift Request



Shift Request is used by an employee to request for a particular Shift Type.

### 1. Prerequisites

To create a Shift Request, these need to be created first:

* [Employee](/docs/en/human-resources/employee)
* [Shift Type](/docs/en/human-resources/shift_type)

### 2. How to create a Shift Request

To create a new Shift Request go to: > Human Resources > Shift Management > Shift Request

1. Go to Shift Request List, Click on New.
2. Select Employee and Shift Type.
3. Set the Shift duration using From Date and To Date.
4. Select the Approver. If the selected approver does not have access to the Shift Request document, it is shared with the approver with "submit" permission.
5. Save.
6. Once the Shift Request is Approved and submitted, it creates a [Shift Assignment](/docs/en/human-resources/shift_assignment)

![Shift Request](/files/shift-requestae7f8e.png)

### 3. Setting Shift Request Approver

A Shift Request Approver is a user who can approve a Shift Request of an Employee. Shift Request Approver can be set at two levels:

* **Department Level:** Shift Request Approvers for each department can be configured in the [Department](/docs/en/human-resources/department) master. Multiple Shift Request Approver can be set in a Department.

![Shift Request Approvers](/files/department-shift-request-approvers.png)

When an Employee belonging to a particular department request for Shift Type, the Shift Request Approver set in that Employee's department master will be considered as his Shift Type Approvers.
* **Employee Level:** Shift Request Approver can also be set in the employee master.

![Shift Request Approvers](/files/employee-shift-request-approver.png)

If Shift Request Approver are set at both employee and department level, the employee level Shift Request Approver will be considered as the default Leave Approver in this case.




