
# Desk Page



When you log in, you're presented with the Desk. It features a persistent sidebar sorted into categories. Each sidebar item links to a page called Workspace.


A Workspace represents a module (for example CRM in ERPNext). A Workspace includes the following:


* A dashboard section for that particular module.
* A shortcut section for frequently used masters, transactions or pages.
* A masters section where all the reports and masters are grouped and listed.


## Standard Workspace


Every module in ERPNext has its own Standard Workspace which is generated with appropriate shortcuts and links.


Any customization to be made to the Standard Workspace can be done with Customize Workspace option in the top right corner of the Workspace.



> 
> Note: These customizations will be user-specific and will only be visible to that user.
> 
> 
> 


## Custom Workspace


You can also create your own Workspaces by simply creating a new Workspace document.


1. Go to the Workspace list and click on New.
2. **Name**: The text you enter here will be shown in the sidebar.
3. **Module**: Select the module which the Workspace will represent.
4. ***Is Standard***: If checked, this Workspace will be shown in the sidebar. Otherwise it will be treated as a customized version of a Standard Workspace.
5. ***Extends Another Page***: If checked, this Workspace will be treated as a customized version of another Workspace.
6. ***Is Default***: If checked, this Workspace will be the default Workspace displayed to all users for a particular module.
7. ***Dashboard***: Add a Dashboard to display it on the top of the Workspace.
8. ***Shortcuts***: Add Shortcuts to a specific page, reports or list which will be displayed below the dashboard.
9. ***Link Cards***: You can add cards that will display a list that links to a specific page, report, or list. You must add these in a specific JSON format as displayed in the image below.




